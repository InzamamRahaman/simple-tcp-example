import socket


class TcpClient(object):

    def __init__(self, port, host):
        self.port = port
        self.host = host
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        message_size = 1024
        self.sock.connect((self.host, self.port))
        server_message = self.sock.recv(message_size)
        print server_message
        client_message = raw_input('Please enter a sentence:')
        print 'You entered ', client_message
        self.sock.send(client_message)
        server_message = self.sock.recv(message_size)
        print 'And received ', server_message
        self.sock.close()

