def test_mint(accounts, token):
    assert token.balanceOf(accounts[0]) == 100000000*10**18