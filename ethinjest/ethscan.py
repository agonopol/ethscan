import requests

ETHERSCAN_API_URL = 'http://api.etherscan.io/api'

# Fetch balance, doesn't seem like you need the api token so leave it out for now
def balance(address):
    params = {
        'module': 'account',
        'action': 'balance',
        'address': address,
        'tag': 'latest',
    }

    balance = requests.get(ETHERSCAN_API_URL, params).json()
    if balance['status'] == '1' and balance['message'] == "OK":
        return balance['result']
    else:
        raise Exception('Could not fetch balance for address %s\nResponse:\t%s' % (address, balance))


def transactions(address):
    params = {
        'module': 'account',
        'action': 'txlist',
        'address': address,
        'sort': 'asc'
    }
    transactions = requests.get(ETHERSCAN_API_URL, params).json()
    if transactions['status'] == '1' and transactions['message'] == "OK":
        return len(transactions['result'])
    else:
        raise Exception('Could not fetch transaction history for address %s\nResponse:\t%s' % (address, transactions))
