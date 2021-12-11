// SPDX-License-Identifier: MIT
pragma solidity ^0.6.12;


import "@openzeppelin/contracts/token/ERC20/ERC20Burnable.sol";
import "./swap.sol";

contract ctoken is ERC20Burnable{
    using SafeMath for uint256;

    uint8 public share; //整数，定义多少百分比的收入被拿去做流动性池子
    address payable public creator;
    Swap public pool;

    event Transfer(address from, address to, uint256 value);
    event Approval(address creator, address spender, uint256 value);
    event Deposit(address client, uint256 amount);
    event Pay(address creator, uint256 amount);
    event Exchange(address creator, uint256 amount);

    constructor(
        string memory _name,
        string memory _symbol,
        uint8  _share
    )
        public ERC20(_name, _symbol)
    {
        require(_share<100, "Your don't want to have _share greater than 100%");
        creator= msg.sender;
        share= _share;
        _mint(msg.sender, 100000000* 10**18);
        pool= new Swap(address(this), _name, _symbol);
        emit Transfer(address(0), creator, totalSupply());
    }
    // Function to receive Ether. msg.data must be empty
    //receive() external payable {}

    // 这是一个可以接收ETH的合约
    fallback() external payable {
        deposit();
    }

    // 对这个账户的汇款，其中部分直接进账，部分做流动性
    function deposit() public payable {
        uint256 creator_share= msg.value.mul(share).div(10**2);
        uint256 holder_share= msg.value.sub(creator_share);

        creator.transfer(creator_share); //转账给creator
        uint256 _tokens= pool.swapEthToTokens{value: holder_share}(0);  //去买自己币
        require(_tokens>0, "No Token has been swaped");
        _burn(address(this), _tokens);// 烧掉币

        emit Deposit(msg.sender, msg.value);
        emit Pay(creator, creator_share);
        emit Exchange(creator, holder_share);
    }

    function getPool() public view returns(address){
        return address(pool);
    }
    function dump() public view returns(string memory name, uint eth, uint tokens){
        //return “Token Dump";
    }
}