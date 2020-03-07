import datetime
import hashlib


class Block:  # every block is an instance of the block class
    blockNumber = 0
    data = None
    next = None  # pointer to a next hash
    hash = None
    nonce = 0
    previousHash = 0x0  # this makes the blockchain immutable
    timestamp = datetime.datetime.now()

    def __init__(self, data):
        self.data = data

    def hash(self):  # calculate the hash of the block
        h = hashlib.sha256()
        h.update(  # make one big string and run this trough sha256 function
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previousHash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNumber).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) \
               + "\nBlock Number: " + str(self.blockNumber) \
               + "\nBlock Data: " \
               + str(self.data) \
               + "\nHashes: " + str(self.nonce) \
               + "\n--------------"
               # Hashes tells how many hashes it took to figure out the block


class Blockchain:

    diff = 20  # shows difficulty, if diff = 0 program accept every block
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("Genesis")
    temp = head = block

    def add(self, block):

        block.previousHash = self.block.hash()
        block.blockNumber = self.block.blockNumber + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):

        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1


blockchain = Blockchain()

for n in range(10):
    blockchain.mine(Block("Block " + str(n+1)))

while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next


