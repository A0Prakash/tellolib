import socket

tello_address = ("192.168.10.1", 8889)

class Tello:
    def __init__(self, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.address = ("", port)
    def sendcommand(self, command):
        try:
            command = command.encode()
            sent = self.sock.sendto(command, tello_address)
        except socket.error as msg:
            print("Error sending message: " + str(msg))
            print(str(sent))

    def recieve(self):
        bytes, address = self.sock.recvfrom(1024)
        bytes = bytes.decode('utf-8')
        if address == tello_address:
            print("Recieved message from tello: " + bytes)
        else:
            print("Message from: " + str(address) + bytes)
    def connect(self):
        try:
            self.sock.bind(self.address)
            self.sendcommand('command')
        except socket.error as msg:
            print("Failed to bind: " + str(msg))
    def takeoff(self):
        try:
            self.sendcommand("takeoff")
        except socket.error as msg:
            print("Error sending message: " + str(msg))
    def land(self):
        try:
            self.sendcommand("land")
        except socket.error as msg:
            print("Error sending message: " + str(msg))
    def forward(self, num):
        try:
            self.sendcommand("forward " + num)
        except socket.error as msg:
            print("Error sending message: " + str(msg))
    def backward(self, num):
        try:
            self.sendcommand("back " + num)
        except socket.error as msg:
            print("Error sending message: " + str(msg))
    def left(self, num):
        try:
            self.sendcommand("left " + num)
        except socket.error as msg:
            print("Error sending message: " + str(msg))
    def right(self, num):
        try:
            self.sendcommand("right " + num)
        except socket.error as msg:
            print("Error sending message: " + str(msg))
    def rotatecw(self, num):
        try:
            self.sendcommand("cw " + num)
        except socket.error as msg:
            print("Error sending message: " + str(msg))
    def rotateccw(self, num):
        try:
            self.sendcommand("ccw " + num)
        except socket.error as msg:
            print("Error sending message: " + str(msg))
    def up(self, num):
        try:
            self.sendcommand("up " + num)
        except socket.error as msg:
            print("Error sending message: " + str(msg))
    def down(self, num):
        try:
            self.sendcommand("down " + num)
        except socket.error as msg:
            print("Error sending message: " + str(msg))
    def stop(self):
        try:
            self.sendcommand("stop")
        except socket.error as msg:
            print("Error sending message: " + str(msg))
	