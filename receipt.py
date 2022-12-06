from web3 import Web3, HTTPProvider
w3 = Web3(HTTPProvider('https://matic-mumbai.chainstacklabs.com'))
print(w3.eth.get_transaction_receipt('0x9443cbe2dbd6601fbe83253bdbfc8593a6000fe3d119ddaf68e20660da3504ab'))
