
from web3 import Web3
from web3.middleware import geth_poa_middleware




abi = [{"stateMutability": "nonpayable", "type": "constructor", "inputs": [], "outputs": []}, {"stateMutability": "payable", "type": "function", "name": "deposit", "inputs": [], "outputs": []}, {"stateMutability": "nonpayable", "type": "function", "name": "makeChoice", "inputs": [{"name": "_choice", "type": "uint256"}], "outputs": []}, {"stateMutability": "nonpayable", "type": "function", "name": "reveal", "inputs": [], "outputs": []}, {"stateMutability": "nonpayable", "type": "function", "name": "kill", "inputs": [], "outputs": []}, {"stateMutability": "view", "type": "function", "name": "player0", "inputs": [], "outputs": [{"name": "", "type": "address"}]}, {"stateMutability": "view", "type": "function", "name": "player1", "inputs": [], "outputs": [{"name": "", "type": "address"}]}, {"stateMutability": "view", "type": "function", "name": "player0Choice", "inputs": [], "outputs": [{"name": "", "type": "uint256"}]}, {"stateMutability": "view", "type": "function", "name": "player1Choice", "inputs": [], "outputs": [{"name": "", "type": "uint256"}]}, {"stateMutability": "view", "type": "function", "name": "player0ChoiceMade", "inputs": [], "outputs": [{"name": "", "type": "bool"}]}, {"stateMutability": "view", "type": "function", "name": "player1ChoiceMade", "inputs": [], "outputs": [{"name": "", "type": "bool"}]}, {"stateMutability": "view", "type": "function", "name": "winner", "inputs": [], "outputs": [{"name": "", "type": "address"}]}, {"stateMutability": "view", "type": "function", "name": "choice_legend", "inputs": [{"name": "arg0", "type": "uint256"}], "outputs": [{"name": "", "type": "string"}]}, {"stateMutability": "view", "type": "function", "name": "player0choice_legend", "inputs": [], "outputs": [{"name": "", "type": "string"}]}, {"stateMutability": "view", "type": "function", "name": "player1choice_legend", "inputs": [], "outputs": [{"name": "", "type": "string"}]}, {"stateMutability": "view", "type": "function", "name": "deposit_balance", "inputs": [], "outputs": [{"name": "", "type": "uint256"}]}]



provider_rpc = {
    'development': 'https://matic-mumbai.chainstacklabs.com',
    'alphanet': '',
}
web3 = Web3(Web3.HTTPProvider(provider_rpc['development']))  # Change to correct network
web3.middleware_onion.inject(geth_poa_middleware, layer=0)



account_from = {
    'private_key': '',
    'address': '',
}


## load contract from address

contract_address = '0xf8b76BB00F3eDe45F6F4b51748C2ad1c16b6C912' # Put your contract's address here

contract = web3.eth.contract(address=contract_address, abi=abi)

print(f'Attempting to deposit from account: { account_from["address"] }')

# deposit

tx_dict = contract.functions.deposit().buildTransaction({
    'from': account_from['address'],
    'nonce': web3.eth.getTransactionCount(account_from['address']),
    'gas': 2000000,
    'gasPrice': web3.toWei('30', 'gwei'),
    'value': web3.toWei('0.01', 'ether'),
})



# sign transaction

signed_txn = web3.eth.account.signTransaction(tx_dict, private_key=account_from['private_key'])

# send transaction

tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

# get transaction receipt

tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

#print block explorer with tx hash to check transaction

print(f'View transaction at: https://explorer-mumbai.maticvigil.com/tx/{tx_hash.hex()}')


print(f'https://mumbai.polygonscan.com/tx/{tx_receipt}')

print(f'Deposit successful at address: { contract.address }')
#

# make choice if 0 = rock 1 = paper and 2 = scissors

choice = 0

## variable to print for choice made

if choice == 1:
    choice_print = "paper"
elif choice == 2:
    choice_print = "scissors"
else:
    choice_print = "rock"


## make choice function

print(f'Attempting to make choice {choice_print} from account: { account_from["address"] }')

# make choice

tx_dict = contract.functions.makeChoice(choice).buildTransaction({
    'from': account_from['address'],
    'nonce': web3.eth.getTransactionCount(account_from['address']),
    'gas': 2000000,
    'gasPrice': web3.toWei('30', 'gwei'),
})


# sign transaction

signed_txn = web3.eth.account.signTransaction(tx_dict, private_key=account_from['private_key'])

# send transaction

tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

# get transaction receipt

tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

print(f'Made choice {choice_print} at address: { contract.address }')

# print block explorer with tx hash to check transaction

print(f'View transaction at: https://explorer-mumbai.maticvigil.com/tx/{tx_hash.hex()}')



# check if both players have made a choice

print(f'Attempting to check if both players have made a choice from account: { account_from["address"] }')

# call player0ChoiceMade function 

player0ChoiceMade = contract.functions.player0ChoiceMade().call()

# call player1ChoiceMade function

player1ChoiceMade = contract.functions.player1ChoiceMade().call()

# check if both players have made a choice

if player0ChoiceMade == True and player1ChoiceMade == True:

    print(f'Both players have made a choice')
    

else:

    print(f'Both players have not made a choice')




# reveal

print(f'Attempting to reveal from account: { account_from["address"] }')

# reveal

tx_dict = contract.functions.reveal().buildTransaction({
    'from': account_from['address'],
    'nonce': web3.eth.getTransactionCount(account_from['address']),
    'gas': 2000000,
    'gasPrice': web3.toWei('30', 'gwei'),
})

# sign transaction

signed_txn = web3.eth.account.signTransaction(tx_dict, private_key=account_from['private_key'])

# send transaction

tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)

# get transaction receipt

tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

print(f'Reveal successful at address: { contract.address }')

# print block explorer with tx hash to check transaction

print(f'View transaction at: https://explorer-mumbai.maticvigil.com/tx/{tx_hash.hex()}')

# get winner

winner = contract.functions.winner().call()

print(f'Winner is: {winner}')



