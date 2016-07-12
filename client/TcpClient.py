import socket


class TcpClient(object):

    def __init__(self, port, host):
        """
        Constructor for TCP Client
        :param port: the port that the client is going to try and access on the server
        :param host: the host of the sever
        """
        self.port = port
        self.host = host
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """
        Connects to the server and initiates interactions
        :return: None
        """
        self.sock.connect((self.host, self.port))
        self.interact_with_server()


    def interact_with_server(self):
        """
        Handles interaction with the server
        :return: None
        """
        message_size = 1024
        block_message = 'You are not allowed to use this server!'
        server_message = self.sock.recv(message_size)
        print server_message
        if server_message != block_message:
            client_message = raw_input('Please enter a sentence:')
            print 'You entered ', client_message
            self.sock.send(client_message)
            server_message = self.sock.recv(message_size)
            print 'And received ', server_message
            self.sock.close()
        else:
            print 'You have been blocked'
            self.sock.close()

