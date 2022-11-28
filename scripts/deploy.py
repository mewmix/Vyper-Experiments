
from web3 import Web3
from web3.middleware import geth_poa_middleware




abi = [] # Put your contract's ABI here by running vyper -f abi <contract_name>.vy



bytecode="" # Put your contract's bytecode here by running vyper (file).vy 
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

print(f'Attempting to deploy from account: { account_from["address"] }')

Incrementer = web3.eth.contract(abi=abi, bytecode=bytecode)



construct_txn = Incrementer.constructor().buildTransaction(
    {
        'from': account_from['address'],
        'nonce': web3.eth.getTransactionCount(account_from['address']),
    }
)

tx_create = web3.eth.account.signTransaction(construct_txn, account_from['private_key'])

tx_hash = web3.eth.sendRawTransaction(tx_create.rawTransaction)
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

print(f'Contract deployed at address: { tx_receipt.contractAddress }')
