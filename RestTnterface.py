'''
Created on Jun 10, 2018

@author: rajaram
'''

from flask import Flask, request
import time, json
from BlockChain import BlockChain

app = Flask(__name__)
blockchain = BlockChain()


@app.route('/new_transaction', methods=['POST'])
def new_transaction():
    tx_data = request.get_json()
    required_fields = ["author", "content"]
    for field in required_fields:
        if not tx_data.get(field):
            return "Invalid Transaction Data", 404
    tx_data["timestamp"] = time.time();
    blockchain.add_new_transaction(tx_data);
    return "Success", 201


@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length":len(chain_data), "chain":chain_data})


@app.route('/mine', methods=['GET'])
def mine_unconfirmed_transactions():
    result = blockchain.mine()
    if not result:
        return "No Transactions to Mine"
    return "Block #{} is mined.".format(result)


@app.route('/pending_tx', methods=['GET'])
def get_pending_tx():
    return json.dumps(blockchain.unconfirmed_transactions)


app.run(port=8080, debug=True)
    
