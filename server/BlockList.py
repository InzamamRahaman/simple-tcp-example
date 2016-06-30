
class BlockList(object):

    def __init__(self, to_block=[]):
        self.lst = set(to_block)

    def block_client(self, client_address):
        client_address in self.lst