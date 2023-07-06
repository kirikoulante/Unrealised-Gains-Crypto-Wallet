import time
from binance import Client
import keys

api_key=keys.get_api_key()
api_secret=keys.get_api_secret()
client = Client(api_key, api_secret)

un_jour = 3600*24*1000
_90_jour = 7776000000 #ecart max via api binance

todayDate = int(time.time())*1000
beginSearchDate = todayDate-_90_jour

def getAll_fiat_deposit_history(todayDate, beginSearchDate, epoch_date):
    amount = 0
    while todayDate > epoch_date:
        response = client.get_fiat_deposit_withdraw_history(transactionType=0, beginTime=beginSearchDate, endTime=todayDate, timestamp=int(time.time())*1000) #fonctionne
        if response["total"] != 0:
            datas = response["data"]
            print(datas)
            for data in datas:
                amount += float(data['indicatedAmount'])
        todayDate = beginSearchDate
        beginSearchDate -= _90_jour
        time.sleep(30)
    return amount

def getAll_fiat_payments_history(todayDate, beginSearchDate, epoch_date):
    amount = 0
    while todayDate > epoch_date:
        response = client.get_fiat_payments_history(transactionType=0, beginTime=beginSearchDate, endTime=todayDate, timestamp=int(time.time())*1000) # fonctionne
        if response["total"] != 0:
            datas = response["data"]
            print(datas)
            for data in datas:
                amount += float(data['sourceAmount'])
        todayDate = beginSearchDate
        beginSearchDate -= _90_jour
        time.sleep(30)
    return amount

def getAllDeposit(epoch_date):
    total_amount = 0
    total_amount += getAll_fiat_deposit_history(todayDate, beginSearchDate, epoch_date)
    total_amount += getAll_fiat_payments_history(todayDate, beginSearchDate, epoch_date)
    print(total_amount)
    return total_amount
