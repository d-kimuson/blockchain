import pytest
from block import Block

@pytest.fixture
def block():
    return Block([], "0")


def test_generate_hash(block):
    res = block.generate_hash()
    assert type(res) is str

def test_set_hash(block):
    block.set_hash()

def test_block_header(block):
    assert type(block.block_header) is str

def test_print_contents(block):
    block.print_contents()
