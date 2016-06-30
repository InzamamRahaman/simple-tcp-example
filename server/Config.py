import json
import socket
import os
import BlockList
import collections

class Config(object):

    def __init__(self, filename='config.json'):
        data = dict()
        if os.path.isfile(filename):
            fp = open(filename, 'r')
            data = json.load(fp)
            fp.close()
        print data
        self.port = int(data.get('port', 12345))
        self.host = data.get('host', socket.gethostname())
        xs = data.get('block_list',  [])
        self.block_list = BlockList.BlockList(xs)
        self.use_multithreaded = data.get('use_multithreaded', False)

    @staticmethod
    def select_or_default(x, y):
        if x == None:
            return x
        return y