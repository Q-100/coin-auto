import time
import pyupbit as p

access = "upbit access key"
secret = "upbit secret key"

login = p.Upbit(access, secret)


def get_balance(ticker):
    """잔고 조회"""
    balances = login.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0


first_percent = 0.02  # 시작할때 몇퍼센트 이상 증가할시
target_percent = 0.05  # 몇퍼센트 이상 이익날시
money = 5500  # 발견하면 넣을 시드
print("======== 경주마 탐색기 시작 =========")

coin_list = ["KRW-BTT", "KRW-AHT", "KRW-TT", "KRW-CRE", 'KRW-MFT', 'KRW-RFR', 'KRW-TSHP', 'KRW-OBSR', 'KRW-MVL',
             'KRW-IQ',
             'KRW-QKC', 'KRW-STMX', 'KRW-IOST', 'KRW-QTCON', 'KRW-EDR', 'KRW-LAMB', 'KRW-STPT', 'KRW-PXL', 'KRW-SSX',
             'KRW-JST',
             'KRW-IGNIS', 'KRW-ORBS', 'KRW-HUM', 'KRW-LOOM', 'KRW-UPP', 'KRW-META', 'KRW-MOC', 'KRW-TRX', 'KRW-FCT2',
             'KRW-LBC',
             'KRW-ANKR', 'KRW-CRO', 'KRW-SNT', 'KRW-WAXP', 'KRW-OMG', 'KRW-EOS', 'KRW-SRM', 'KRW-THETA',
             'KRW-GAS',
             'KRW-QTUM', 'KRW-FLOW', "KRW-STRK", "KRW-PUNDIX"]

flag = 0
count = 1
while True:
    try:
        if flag == 0:
            print("탐색시작!", count, "번째 시도 중")
            first_price = p.get_current_price(coin_list)
            for k in first_price:
                first_price[k] = first_price[k] + first_price[k] * first_percent
            time.sleep(0.5)
            check_price = p.get_current_price(coin_list)
            flag = 1
            count += 1
        if flag == 1:
            print("현재상태 : ", flag)
            for c in check_price:
                if check_price[c] >= first_price[c]:
                    login.buy_market_order(c, money * 0.9995)
                    flag = 2
                    print(c, ":", check_price[c], "에 매수")
                    target_price = check_price[c] + check_price[c] * target_percent
                    break

        if flag == 2:
            print("현재상태 : ", flag)
            while True:
                sell_price = p.get_current_price(c)
                time.sleep(0.3)

                if sell_price > target_price:
                    login.sell_market_order(c, get_balance(c[4:]))
                    print(c, "팔았음")
                    flag = 3
                    break
        if flag == 3:
            print("종료합니다")
            break
        print("=== 발견 못함 ===")
        time.sleep(0.1)
        flag = 0

    except Exception as e:
        print("대기")
        time.sleep(1)

# 확인 후 거래
    # - 장점 : 이득을 볼 확률이 높다, 비교적 안전하다
    # - 단점 : 이득이 적다, 거래에 대한 ★불확실성★,물리면 인생 ㅈ됨


# 미리 거래
    # - 장점 : 이득이 극대화됨, 거래에 대한 불확실성이 비교적 낮음,물려도 가능성있음
    # - 단점 : 큰 손해를 볼 수 있음.
