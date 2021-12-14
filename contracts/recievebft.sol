// SPDX-License-Identifier: MIT
pragma solidity ^0.6.12;

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721Holder.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721Receiver.sol";
import "@openzeppelin/contracts/introspection/ERC165.sol";

contract Receiver721Example is IERC721Receiver, ERC165, ERC721Holder {
    constructor() public {
        _registerInterface(IERC721Receiver.onERC721Received.selector);
    }
    
    function doSomethingWith721Token(IERC721 nftAddress, uint256 tokenId) external {
        // do something here
    }
}