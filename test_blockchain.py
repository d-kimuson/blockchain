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

def test_validate_chain(chain):
    chain.add_transactions([
        {'sender': 'taro', 'receiver': 'jiro', 'amount': 300},
        {'sender': 'watanabe', 'receiver': 'jiro', 'amount': 200},
        {'sender': 'tarounosuke', 'receiver': 'taro', 'amount': 1000},
        ])

    chain.create_block()
    assert chain.validate_chain()

