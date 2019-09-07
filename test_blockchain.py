import pytest
from blockchain import Blockchain

@pytest.fixture
def chain():
    return Blockchain()

def test_genesis_block(chain):
    chain.genesis_block()