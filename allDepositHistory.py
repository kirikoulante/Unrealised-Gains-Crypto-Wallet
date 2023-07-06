import time
from binance import Client
import keys

api_key=keys.get_api_key()
api_secret=keys.get_api_secret()
client = Client(api_key, api_secret)
epoch_date = keys.get_epoch_all_deposit()

un_jour = 3600*24*1000
_90_jour = 7776000000

todayDate = int(time.time())*1000
yesterdayDate = todayDate-_90_jour

def getAll_fiat_deposit_history(todayDate, yesterdayDate):
    amount = 0
    while todayDate > epoch_date:
        response = client.get_fiat_deposit_withdraw_history(transactionType=0, beginTime=yesterdayDate, endTime=todayDate, timestamp=int(time.time())*1000) #fonctionne
        #response = client.get_fiat_payments_history(transactionType=0, beginTime=yesterdayDate, endTime=todayDate, timestamp=int(time.time())*1000) # fonctionne
        if response["total"] != 0:
            datas = response["data"]
            print(datas)
            for data in datas:
                amount += float(data['indicatedAmount'])
        todayDate = yesterdayDate
        yesterdayDate -= _90_jour
        time.sleep(30)
    return amount

def getAll_fiat_payments_history(todayDate, yesterdayDate):
    amount = 0
    while todayDate > epoch_date:
        response = client.get_fiat_payments_history(transactionType=0, beginTime=yesterdayDate, endTime=todayDate, timestamp=int(time.time())*1000) # fonctionne
        if response["total"] != 0:
            datas = response["data"]
            print(datas)
            for data in datas:
                amount += float(data['sourceAmount'])
        todayDate = yesterdayDate
        yesterdayDate -= _90_jour
        time.sleep(30)
    return amount

def getAllDeposit():
    total_amount = 0
    total_amount += getAll_fiat_deposit_history(todayDate, yesterdayDate)
    total_amount += getAll_fiat_payments_history(todayDate, yesterdayDate)
    print(total_amount)
    return total_amount
