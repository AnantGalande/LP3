// SPDX-License-Identifier: MIT
pragma solidity 0.8.38;

contract BankAccount {

    mapping(address => uint) public balances;

    function deposit() public payable {
        require(msg.value > 0, "Invalid amount");
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint amount) public {
        require(amount > 0, "Invalid amount");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;

        (bool success, ) = payable(msg.sender).call{value: amount}("");
        require(success, "Transfer failed");
    }

    function getBalance() public view returns (uint) {
        return balances[msg.sender];
    }
}