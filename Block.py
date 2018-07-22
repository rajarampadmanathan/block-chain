'''
Created on Jun 10, 2018

@author: rajaram
'''

from hashlib import sha256
import time
import json


class Block:

    def __init__(self, index, previous_hash, transactions, timestamp):
        self.index = index;
        self.previous_hash = previous_hash;
        self.transactions = transactions;
        self.timestamp = timestamp;

    def compute_hash(self):
        block_str = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_str.encode()).hexdigest()


nb = Block(index=1, previous_hash=None, transactions="transactions-1", timestamp=time.time())
nb1 = Block(index=2, previous_hash=None, transactions="transactions-2", timestamp=time.time())

print("Block1:" + nb.compute_hash())
print("Block2:" + nb1.compute_hash())
print("Block1:" + nb.compute_hash())
print("Block2:" + nb1.compute_hash())
