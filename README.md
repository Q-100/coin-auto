# 경주마 탐색기 🐎

-----

## ⚡️ [Quick Start]()

### 아나콘다 가상환경

```python
conda install python 3.8
conda install pyupbit
conda install pyjwt
```

### access key, secret key 입력
```python
# main.py
import time 
import pyupbit as p

access = "upbit access key"
secret = "upbit secret key"

login = p.Upbit(access, secret)

```

### 탐색할 코인 등록
```python
coin_list = ["KRW-BTT", "KRW-AHT", "KRW-TT", "KRW-CRE", 'KRW-MFT', 'KRW-RFR', 'KRW-TSHP', 'KRW-OBSR', 'KRW-MVL',
             'KRW-IQ',
             'KRW-QKC', 'KRW-STMX', 'KRW-IOST', 'KRW-QTCON', 'KRW-EDR', 'KRW-LAMB', 'KRW-STPT', 'KRW-PXL', 'KRW-SSX',
             'KRW-JST',
             'KRW-IGNIS', 'KRW-ORBS', 'KRW-HUM', 'KRW-LOOM', 'KRW-UPP', 'KRW-META', 'KRW-MOC', 'KRW-TRX', 'KRW-FCT2',
             'KRW-LBC',
             'KRW-ANKR', 'KRW-CRO', 'KRW-SNT', 'KRW-WAXP', 'KRW-OMG', 'KRW-EOS', 'KRW-SRM', 'KRW-THETA',
             'KRW-GAS',
             'KRW-QTUM', 'KRW-FLOW', "KRW-STRK", "KRW-PUNDIX"]
```

## 💡 증가분, 매도시점, 투입할시드 선택(중요!!)
```python
first_percent = 0.02  # 시작할때 몇퍼센트 이상 증가할시
target_percent = 0.05  # 몇퍼센트 이상 이익날시
money = 5500  # 발견하면 넣을 시드
```
- first_percent : 0.02 입력 시 2초사이에 2퍼센트가 증가한 코인을 탐색합니다
- target_percent : 0.05 입력 시 매수 가격의 5퍼센트가 증가했을 경우 자동 매도합니다.
- money : 탐색 성공한 코인을 구매할 가격을 정합니다.(수수료와 최소 매수 가격이 정해져있어 5500원이 최소)


## ⚠️ 주의사항

- 이 경주마 탐색기는 웹소켓을 기반으로 하기 때문에 실제 시장상황과의 시간 격차가 0.5초정도 존재합니다
- 이 프로그램으로 인해 생긴 손실은 전적으로 사용자에게 있음을 알립니다.