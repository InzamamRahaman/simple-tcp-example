import socket
import BlockList


class TcpServer(object):

    def __init__(self, port, host='', block_list=BlockList.BlockList()):
        """
        This is the constructor for the TcpServer object
        :param host: the hostname for this server as a string. Default is empty string ('') to automatically set to localhost
        :param port: the port number for the server to receive connections
        :param block_list: the BlockList to be used to decide whether to process a client or not
        """
        self.host = host # self is the equivalent of "this" in Python. We can create object fields on the fly in any method
        self.port = port
        self.block_list = block_list

        # create a socket
        # socket.AF_INET: uses IPv4
        # socket.SOCK_STREAM: we want to use TCP
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port)) # bind the socket to particular port and hostname
        self.DEFAULT_BACKLOG = 5

    def listen(self, backlog=None):
        """
        Start the listening process on the server end. The server can only queue a set number
        of clients for processing
        :param backlog: the number of clients to queue
        :return: None
        """
        num = self.DEFAULT_BACKLOG
        if backlog:
            num = backlog
        self.sock.listen(num)
        run_server = True
        print 'Listening for connections.....'
        while run_server:
            # an address is a combination of both the host and port
            # as a tuple
            client_sock, client_addr = self.sock.accept()
            self.process_client_socket(client_sock, client_addr)

    def process_client_socket(self, client_socket, client_addr):
        """
        Wrapper to handle client
        :param client_socket: the socket to communicate with the client
        :param client_addr: the address of the client
        :return: None
        """
        fun = self.handle_client
        if self.block_list.block_client(client_addr):
            fun = self.reject_client
        fun(client_socket, client_addr)

    def handle_client(self, client_socket, client_addr):
        """
        Handles the interaction with a client
        :param client_socket: the socket to communicate with the client
        :param client_addr: the address of the client
        :return: None
        """
        max_size = 1024
        print 'Connected to client at ', client_addr
        client_socket.send('Thank you for connected to the Maths server.')
        # the maximum number of bytes is passed as a parameter to recv
        # we recieve a message from the client
        expression = client_socket.recv(max_size)
        our_response = self.process_client_message(expression)
        client_socket.send(our_response)
        client_socket.close()

    def reject_client(self, client_socket, client_addr):
        """
        Handles clients that are not permited to use this server
        :param client_socket: the socket to communicate with the client
        :param client_addr: the address of the client
        :return: None
        """
        block_message = 'You are not allowed to use this server!'
        client_socket.send(block_message)
        client_socket.close()

    def process_client_message(self, message):
        """
        Processes the client's message
        :param message: the client message. In this case, we captailize the string
        :return: a response to the client's message. In this case, we captailize the string
        """
        return message.upper()





