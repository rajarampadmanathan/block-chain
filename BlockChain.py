'''
Created on Jun 10, 2018

@author: rajaram
'''

from Block import Block
import time


class BlockChain:
	
	difficulty = 2;
	
	def __init__(self):
		self.unconfirmed_transactions = []
		self.chain = []
		self.create_genesis_block()

	def create_genesis_block(self):
		genesis_block = Block(0, 0, [], time.time());
		genesis_block.hash = genesis_block.compute_hash();
		self.chain.append(genesis_block)
	
	def proof_of_work(self, block):
		block.nonce = 0;
		computed_hash = block.compute_hash()
		while not computed_hash.startswith('0' * BlockChain.difficulty):
			print(computed_hash)
			block.nonce += 1; 
			computed_hash = block.compute_hash() 
		return computed_hash;
	
	def add_block(self, block, proof):
		previous_hash = self.last_block.hash
		if previous_hash != block.previous_hash:
			return False
		if not self.is_valid_hash(block, proof):
			return False
		block.hash = proof;
		self.chain.append(block);
		return True
	
	def is_valid_hash(self, block, block_hash):
		return block_hash.startswith('0' * BlockChain.difficulty) and block_hash == block.compute_hash();
	
	def add_new_transaction(self, transaction):
		self.unconfirmed_transactions.append(transaction);
	
	def mine(self):
		if not self.unconfirmed_transactions:
			return False
		last_block = self.last_block
		
		new_block = Block(index=last_block.index + 1, previous_hash=last_block.hash, transactions=self.unconfirmed_transactions, timestamp=time.time())
		proof = self.proof_of_work(new_block)
		self.add_block(new_block, proof)
		self.unconfirmed_transactions = []
		return new_block.index

	@property
	def last_block(self):
		return self.chain[-1];