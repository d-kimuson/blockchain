import pytest
from blockchain import Blockchain

@pytest.fixture
def chain():
    return Blockchain()


def test_genesis_block(chain):
    chain.genesis_block()


def test_add_transaction_s(chain):
    chain.add_transactions(
        [{
            'sender': 'taro',
            'receiver': 'jiro',
            'amount': 300
        }]
    )

def test_create_block(chain):
    chain.add_transactions(
        [{
            'sender': 'taro',
            'receiver': 'jiro',
            'amount': 300
        }]
    )
    chain.create_block()
