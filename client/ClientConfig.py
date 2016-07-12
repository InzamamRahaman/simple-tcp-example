import json
import socket
import os

class ClientConfig(object):

    def __init__(self, filename='config.json'):
        data = dict()
        if os.path.isfile(filename):
            fp = open(filename, 'r')
            data = json.load(fp)
            fp.close()
        self.port = int(data.get('port', 12345))
        self.host = data.get('host', socket.gethostname())