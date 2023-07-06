# Import the required libraries
import time
from binance import Client
import requests
import re
import keys

def conversion_to_eur(symbol_crypto):
    fiat = 'EUR'
    match = re.match("^LD.{2,}", symbol_crypto)
    if match:
        symbol_crypto = symbol_crypto[2:]
    # Endpoint for the conversion
    url = 'https://min-api.cryptocompare.com/data/price'
    # Parameters for the request
    params = {'fsym': symbol_crypto, 'tsyms': fiat}
    # Make the request
    response = requests.get(url, params=params)
    # Get the JSON response
    data = response.json()
    # Get the conversion rate
    conversion_rate = data[fiat]
    return float(conversion_rate)

def get_cryptocurrencies(snapshot_vos):
    # Initialize an empty list of cryptocurrencies
    cryptocurrencies = 0
    # Iterate over the snapshotVos list
    for snapshot_vo in snapshot_vos:
        # Get the type of wallet (spot, margin, or futures)
        wallet_type = snapshot_vo["type"]
        # Check the wallet type and extract the balances from the data field
        if wallet_type == "spot":
            balances = snapshot_vo["data"]["balances"]
        elif wallet_type == "margin":
            balances = snapshot_vo["data"]["userAssets"]
        elif wallet_type == "futures":
            balances = snapshot_vo["data"]["assets"]
        else:
            # Unknown wallet type, skip this snapshotVo
            continue

        # Iterate over the balances list
        for balance in balances:
            # Get the name and balance of the cryptocurrency
            name = balance["asset"]
            if wallet_type == "spot" or wallet_type == "margin":
                # Spot and margin wallets use the 'free' field for the balance
                amount = balance["free"]
            elif wallet_type == "futures":
                # Futures wallets use the 'walletBalance' field for the balance
                amount = balance["walletBalance"]
            else:
                # Unknown wallet type, skip this balance
                continue

            # Convert and Add the cryptocurrency to the list
            amountEUR = float(amount) * conversion_to_eur(name)
            cryptocurrencies += amountEUR
    # Return the list of cryptocurrencies
    return cryptocurrencies


# Enter your Binance API key and secret
API_KEY=keys.get_api_key()
API_SECRET=keys.get_api_secret()

client = Client(API_KEY, API_SECRET)
todayDate = int(time.time())*1000
yesterdayDate = todayDate-3600*24*1000

def get_binance_wallet_value():
    response = client.get_account_snapshot(type='SPOT', startTime=yesterdayDate, endTime=todayDate)
    # Check the status code
    if response['code'] == 200:
        # Extract the snapshotVos list from the response
        snapshot_vos = response["snapshotVos"]
        # Get the cryptocurrencies
        cryptocurrencies = get_cryptocurrencies(snapshot_vos)
        # Print the cryptocurrencies in €
        print(cryptocurrencies)
        return cryptocurrencies
    else:
        # Print the error message
        print(response["msg"])
        return -9999999999999

#get_binance_wallet_value()
