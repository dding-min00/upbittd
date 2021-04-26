import time
import pyupbit
import datetime

access = "joyQ8lK1sWnsN3qXVxxamjG6FsRGmNjU8CT9Ox7v"          # 본인 값으로 변경
secret = "AiTbFVLyZU93EPA439xzHIlYS2AuITM3xXqeIkxw"          # 본인 값으로 변경

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0

def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")
buybit_ETC = 0
buybit_XRP = 0
buybit_BTG = 0
buybit_BCH = 0
buybit_BCHA = 0
# 자동매매 시작
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-ETC")
        end_time = start_time + datetime.timedelta(days=1)

        if start_time < now < end_time - datetime.timedelta(seconds=10):
            target_price_ETC = get_target_price("KRW-ETC", 0.6)
            current_price_ETC = get_current_price("KRW-ETC")

            target_price_XRP = get_target_price("KRW-XRP", 0.6)
            current_price_XRP = get_current_price("KRW-XRP")

            target_price_BTG = get_target_price("KRW-BTG", 0.6)
            current_price_BTG = get_current_price("KRW-BTG")

            target_price_BCH = get_target_price("KRW-BCH", 0.6)
            current_price_BCH = get_current_price("KRW-BCH")

            target_price_BCHA = get_target_price("KRW-BCHA", 0.6)
            current_price_BCHA = get_current_price("KRW-BCHA")

            if target_price_ETC < current_price_ETC:
                krw = get_balance("KRW")
                if krw > 5000:
                    if buybit_ETC == 0:
                        upbit.buy_market_order("KRW-ETC", krw*0.9995*0.2)
                        buybit_ETC = 1

            if target_price_XRP < current_price_XRP:
                krw = get_balance("KRW")
                if krw > 5000:
                    if buybit_XRP == 0:
                        upbit.buy_market_order("KRW-XRP", krw*0.9995*0.2)
                        buybit_XRP = 1

            if target_price_BTG < current_price_BTG:
                krw = get_balance("KRW")
                if krw > 5000:
                    if buybit_BTG == 0:
                        upbit.buy_market_order("KRW-BTG", krw*0.9995*0.2)
                        buybit_BTG = 1

            if target_price_BCH < current_price_BCH:
                krw = get_balance("KRW")
                if krw > 5000:
                    if buybit_BCH == 0:
                        upbit.buy_market_order("KRW-BCH", krw*0.9995*0.2)
                        buybit_BCH = 1

            if target_price_BCHA < current_price_BCHA:
                krw = get_balance("KRW")
                if krw > 5000:
                    if buybit_BCHA == 0:
                        upbit.buy_market_order("KRW-BCHA", krw*0.9995*0.2)
                        buybit_BCHA = 1

        else:
            btc = get_balance("ETC")
            p_xrp = get_balance("XRP")
            p_btg = get_balance("BTG")
            p_bch = get_balance("BCH")
            P_bcha = get_balance("BCHA")
            if btc > 0.00008:
                upbit.sell_market_order("KRW-ETC", btc*0.9995)
                buybit_ETC = 0
            if p_xrp > 0.00008:
                upbit.sell_market_order("KRW-XRP", btc*0.9995)
                buybit_XRP = 0
            if p_btg > 0.00008:
                upbit.sell_market_order("KRW-BTG", btc*0.9995)
                buybit_BTG = 0
            if p_bch > 0.00008:
                upbit.sell_market_order("KRW-BCH", btc*0.9995)
                buybit_BCH = 0
            if P_bcha > 0.00008:
                upbit.sell_market_order("KRW-BCHA", btc*0.9995)
                buybit_BCHA = 0

        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)