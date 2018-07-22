'''
Created on Jun 10, 2018

@author: rajaram
'''
from flask import Flask, request
import requests 
import json
from RestTnterface import blockchain
from Block import Block
app = Flask(__name__)
peers = set()


@app.route('/add_nodes', methods=['POST'])
def register_new_peers():
    nodes = request.get_json();
    if not nodes:
        return "Invalid Data", 400
    for node in nodes:
        peers.add(node)
    
    return "Success", 201

    
def consensus():
    global blockchain
    longest_chain = None
    current_len = len(blockchain)
    for node in peers:
        response = requests.get('http://{}/chian'.format(node))
        length = response.json()['length']
        chain = response.json()['chain']
        if length > current_len and blockchain.check_chain_validity(chain):
            current_len = length
            longest_chain = chain
    if longest_chain:
        blockchain = longest_chain
        return True
    return False

    
@app.route('/add_block', methods=['POST'])
def validate_and_add_block():
    block_data = request.get_json()
    block = Block(block_data['index'], block_data['transactions'], block_data["timestamp", block_data["previous_hash"]])
    proof = block_data['hash']
    added = blockchain.add_block(block, proof)
    if not added:
        return "The block was discarded by the node", 400
 
    return "Block added to the chain", 201

     
def announce_new_block(block):
    for peer in peers:
        url = "http://{}/add_block".format(peer)
        requests.post(url, data=json.dumps(block.__dict__, sort_keys=True))
