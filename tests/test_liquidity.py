import brownie

def test_liquidity(accounts, pool, token):
    assert pool.getTokenReserve() == 0

    # First liquidity provider adding liquidity (accounts[0]) with a price ratio
    # of 1000000000 gwei to 200 token:
    token.approve(pool.address, 200, {'from': accounts[0]})
    pool.addLiquidity(200, {'from': accounts[0], 'value': 100})

    assert pool.getTokenReserve() == 200
    assert pool.totalSupply() == 200
    assert pool.balanceOf(accounts[0]) == 100

    # Second liquidity provider adding liquidity (accounts[1]) in a very different rate
    # than first provider (they are giving the token a much lower price: 100 gwei to 100 token):
    token.approve(accounts[0], 200, {'from': accounts[0]})
    token.transferFrom(accounts[0], accounts[1], 200, {'from': accounts[0]})
    token.approve(pool.address, 200, {'from': accounts[1]})
    pool.addLiquidity(200, {'from': accounts[1], 'value': 100})

    assert pool.getTokenReserve() == 200
    assert pool.totalSupply() == 1000000100
    assert pool.balanceOf(accounts[1]) == 100

    # Second liquidity provider trying to remove their liquidity (accounts[1]) get their
    # transaction reverted because they gave the token a much lower price in terms of eth:
    with brownie.reverts():
        pool.removeLiquidity(100, {'from': accounts[1]})

    assert pool.getTokenReserve() == 200
    assert pool.totalSupply() == 1000000100
