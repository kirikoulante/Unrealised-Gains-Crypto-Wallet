import requests
import binanceWalletValue
import keys


def get_private_wallet_value():
    total_value = 0
    total_value += get_ETH()
    total_value += get_EGLD()
    total_value += get_ATOM()
    total_value += get_DOT()
    total_value += get_BTC()
    return total_value

def get_BTC():
    btc_addr = keys.get_btc_addr()
    # Endpoint for the api
    url = f'https://blockstream.info/api/address/{btc_addr}'
    # Make the request
    response = requests.get(url)
    # Get the JSON response
    data = response.json()
    # Get the asset value
    value_in_sat = int(data['chain_stats']['funded_txo_sum'])
    value_in_btc = value_in_sat/10**8
    value_in_eur = float(value_in_btc * binanceWalletValue.conversion_to_eur('BTC'))
    print(value_in_eur, " ", value_in_btc)
    return value_in_eur

def get_ETH():
    eth_addr = keys.get_eth_addr()
    api_key = keys.get_api_eth()
    url = f'https://api.etherscan.io/api?module=account&action=balance&address={eth_addr}&tag=latest&apikey={api_key}'
    # Faire la requête
    response = requests.get(url)
    # Obtenir la réponse JSON
    data = response.json()
    # Obtenir le solde en wei (plus petite unité d'Ether)
    balance_in_wei = int(data['result'])
    # Conversion de wei en Ether
    balance_in_ether = balance_in_wei / 10**18
    # Conversion du montant d'Ether en euros
    ether_to_eur_conversion_rate =  binanceWalletValue.conversion_to_eur('ETH')
    value_in_eur = balance_in_ether * ether_to_eur_conversion_rate
    print(value_in_eur)
    return value_in_eur

def get_DOT():
    # dot_addr = keys.get_dot_addr()
    # url = f'https://polkadot.subscan.io/api/scan/account?address={dot_addr}'
    # # Faire la requête
    # response = requests.get(url)
    # # Obtenir la réponse JSON
    # data = response.json()
    # print(data)
    # # Obtenir le solde en DOT
    # balance_in_dot = float(data['data']['balance']) / 10**10
    # Conversion du montant de DOT en euros
    dot_to_eur_conversion_rate = binanceWalletValue.conversion_to_eur('DOT')
    value_in_eur = balance_in_dot * dot_to_eur_conversion_rate
    print(value_in_eur)
    return value_in_eur

def get_ATOM():
    # atom_addr = keys.get_atom_addr()
    # url = f'https://www.mintscan.io/cosmos/account/{atom_addr}'
    # # Faire la requête
    # response = requests.get(url)
    # # Obtenir la réponse JSON
    # data = response.json()
    # print(data)
    # # Obtenir le solde en ATOM
    # balance_in_atom = float(data['balance'])
    # Conversion du montant d'ATOM en euros
    atom_to_eur_conversion_rate = binanceWalletValue.conversion_to_eur('ATOM')
    value_in_eur = balance_in_atom * atom_to_eur_conversion_rate
    print(value_in_eur)
    return value_in_eur

def get_EGLD():
    egld_addr = keys.get_egld_addr()
    url = f'https://api.elrond.com/accounts/{egld_addr}'
    # Faire la requête
    response = requests.get(url)
    # Obtenir la réponse JSON
    data = response.json()
    # Obtenir le solde en EGLD
    balance_in_egld = float(data['balance']) / 10**18
    # Conversion du montant d'EGLD en euros
    egld_to_eur_conversion_rate = binanceWalletValue.conversion_to_eur('EGLD')
    value_in_eur = balance_in_egld * egld_to_eur_conversion_rate
    print(value_in_eur)
    return value_in_eur

#print(get_private_wallet_value())