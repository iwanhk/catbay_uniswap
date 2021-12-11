#!/usr/bin/python3

import pytest

@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture
def token(ctoken, accounts):
    return ctoken.deploy("C1", "C1", 50, {'from': accounts[0]})

@pytest.fixture
def pool(token):
    return token.getPool()