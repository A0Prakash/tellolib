import socket

class tello:
    def _init_(self) :
        self.ip = ''
        self.port = 1111
        self.addr = (self.ip, self.port)
        self.telloport = 8889
        self.telloip = "192.168.10.1"
        self.telloaddr = (self.telloip, self.telloport)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    def sendcommand(self, command):
        try:
            command = command.encode()
            sent = self.sock.sendto(command, self.addr)
        except socket.error as msg:
            print("Error sending message: " + str(msg))
            print(str(sent))
    def connect(self):
        try:
            self.sock.bind(self.addr)
            self.sendcommand('command')
        except socket.error as msg:
            print("error sending message " + str(msg))
    def takeoff(self):
        try:
            self.sendcommand('takeoff')
        except socket.error as msg:
            print("error sending message " + str(msg))
    def land(self):
        try:
            self.sendcommand('land')
        except socket.error as msg:
            print("error sending message " + str(msg))
    
        
        



