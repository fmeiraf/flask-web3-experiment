import json
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from dynaconf import settings

# web3.py instance
w3 = Web3(HTTPProvider("http://127.0.0.1:8545"))
print(w3.isConnected())

key="<Private Key here with 0x prefix>"
acct = w3.eth.account.privateKeyToAccount(settings.PRIVATE_KEY)
print(settings.PRIVATE_KEY)

# compile your smart contract with truffle first
truffleFile = json.load(open('build/contracts/greeter.json'))
abi = truffleFile['abi']
bytecode = truffleFile['bytecode']
contract= w3.eth.contract(bytecode=bytecode, abi=abi)
# 

# building transaction
construct_txn = contract.constructor().buildTransaction({
    'from': acct.address,
    'nonce': w3.eth.getTransactionCount(acct.address),
    'gas': 6721975,
    'gasPrice': w3.toWei('21', 'gwei')})

signed = acct.signTransaction(construct_txn)

tx_hash=w3.eth.sendRawTransaction(signed.rawTransaction)
print(tx_hash.hex())
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
print("Contract Deployed At:", tx_receipt['contractAddress'])