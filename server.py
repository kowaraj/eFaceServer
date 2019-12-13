import socketserver
import time

class MyTCPSocketHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(str(self.client_address)))
        print(self.data)
        time.sleep(1)

        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    
    HOST, PORT = "localhost", 61009

    # instantiate the server, and bind to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPSocketHandler)

    # activate the server
    # this will keep running until Ctrl-C
    server.serve_forever()