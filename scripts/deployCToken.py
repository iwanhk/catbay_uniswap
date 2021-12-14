from brownie import ctoken, Swap, accounts, network, config

def addr(account):
    return {"from": account}

def b(account):
    return network.web3.fromWei(account, 'ether')

def main():
    if network.show_active() == 'development' :
        iwan=accounts[0]
        guy=accounts[1]
        wow=accounts[2]

        token=ctoken.deploy('c1', 'C1', 50, {'from': iwan})
        pool= Swap.at(token.getPool())

    if network.show_active() == 'kovan' or network.show_active() == 'rinkeby' :
        accounts.add(config['wallets']['iwan'])

        token=ctoken.deploy('c1', 'C1', 50, {'from': accounts[0]})
        pool= Swap.at(token.getPool())
