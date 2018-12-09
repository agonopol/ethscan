import pytest
from ethinjest.ethscan import balance, transactions

def test_balanace_ok():
    eth = balance('0x742d35Cc6634C0532925a3b844Bc454e4438f44e')
    assert int(eth) >= 0

def test_balanace_not_ok():
    with pytest.raises(Exception):
        balance('some-random-bad-address')


def test_transactions_ok():
    eth = transactions('0x742d35Cc6634C0532925a3b844Bc454e4438f44e')
    assert eth >= 0

def test_transcations_not_ok():
    with pytest.raises(Exception):
        transactions('some-random-bad-address')
