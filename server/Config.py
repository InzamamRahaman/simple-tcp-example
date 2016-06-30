import json
import socket
import os

class Config(object):

    def __init__(self, filename='config.json'):
        data = dict()
        if os.path.isfile(filename):
            fp = open(filename, 'r')
            data = json.load(fp)
            fp.close()
        self.port = Config.select_or_default(data['port'], 12345)
        self.host = Config.select_or_default(data['host'], socket.gethostname())
        self.block_list = Config.select_or_default(data['block_list'], [])

    @staticmethod
    def select_or_default(self, x, y):
        if x == None:
            return x
        return y