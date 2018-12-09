from ethinjest.model import Status
from ethinjest.ethscan import balance, transactions
from datetime import datetime


def status(address, asof=datetime.now()):
    return Status(address=address, balance=balance(address), transactions=transactions(address), asof=asof)
