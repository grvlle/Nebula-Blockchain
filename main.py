import hashlib as hasher
from datetime import datetime

class BlockHasher:

    def __init__(self, index, ts, data, prev_hash):

        self.index = index
        self.ts = ts
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        clear = f'{self.index} {self.ts} {self.data} {self.prev_hash}'
        clear_bytes = clear.encode('utf-8')
        sha.update(clear_bytes)

        return sha.hexdigest()

    def de_hash_block(self):
        print(f'{self.index} {self.ts} {self.data} {self.prev_hash}')



class NebulaChain:

    nebula_chain = [BlockHasher(0, datetime.now(), 'This is the Genesis Block', '0')] #Creates the Genesis Block
    previous_block = nebula_chain[0]

    @staticmethod
    def create_next_block(last_block, data):
        """Produces the blocks following the Genesis Block"""
        new_index = last_block.index + 1
        new_ts = datetime.now()
        new_data = f'Block #{new_index} {data}'
        new_hash = last_block.hash

        return BlockHasher(new_index, new_ts, new_data, new_hash)

    @classmethod
    def add_block_to_chain(cls, data):
        """Takes the user provided data in msg variable in main(), and stores it on the chain"""
        block_to_add = cls.create_next_block(cls.previous_block, data)
        cls.nebula_chain.append(block_to_add)
        cls.previous_block = block_to_add

        print(f'Block #{block_to_add.index} has been added to the Nebula Chain')
        print(f'Hash: {block_to_add.hash}\n')

    @classmethod
    def inspect_chain(cls, id):
        block = cls.nebula_chain[id]

        return BlockHasher.de_hash_block(block)



def main():

    for x in range(10):
        NebulaChain.add_block_to_chain(x)

    try:
        while True:

            action = int(input('1. Add new block to the Nebula Chain\n2. View existing block on the chain\n >'))

            if action == 1:
                msg = input('Leave your message on the Nebula Blockchain\n > ')
                NebulaChain.add_block_to_chain(msg)
                break

            if action == 2:
                id = int(input('Enter block ID to view:\n > '))
                NebulaChain.inspect_chain(id)
                break
            else:
                break

    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
