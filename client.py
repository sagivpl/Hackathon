# import socket
# import time
#
# # import getch
# # from socket import*
# from msvcrt import getch
#
#
# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKCYAN = '\033[96m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
#     F_Default = "\x1b[39m"
#     F_Black = "\x1b[30m"
#     F_Red = "\x1b[31m"
#     F_Green = "\x1b[32m"
#     F_Yellow = "\x1b[33m"
#     F_Blue = "\x1b[34m"
#     F_Magenta = "\x1b[35m"
#     F_Cyan = "\x1b[36m"
#     F_LightGray = "\x1b[37m"
#     F_DarkGray = "\x1b[90m"
#     F_LightRed = "\x1b[91m"
#     F_LightGreen = "\x1b[92m"
#     F_LightYellow = "\x1b[93m"
#     F_LightBlue = "\x1b[94m"
#     F_LightMagenta = "\x1b[95m"
#     F_LightCyan = "\x1b[96m"
#     F_White = "\x1b[97m"
#
# def sending_udp_mess(UDP_IP):
#     # UDP_IP = "10.100.102.4"
#     UDP_PORT = 5005
#     #sending
#     MESSAGE = ('0xfeedbeef'+'0x2'+str(UDP_PORT))
#     MESSAGE = bytes(MESSAGE,'utf-8')
#     UDP_IP = "10.100.102.11"
#     sock = socket.socket(socket.AF_INET, # Internet
#                          socket.SOCK_DGRAM) # UDP
#     sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
#
#     # cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # cs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     # cs.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#     # try:
#     #     cs.sendto(MESSAGE, ("255.255.255.255", UDP_PORT))
#     #     cs.sendto(MESSAGE, ("255.255.255.255", UDP_PORT))
#     #
#     # except:
#     #     pass
#
#
# def sending_tcp_mess(host_congig):
#
#     BUFFER_SIZE = 100000
#     MESSAGE = "VintKahn\n".encode('utf_8')
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     TCP_IP = host_congig[0]
#     TCP_PORT = host_congig[1]
#     s.connect((TCP_IP, TCP_PORT))
#     s.send(MESSAGE)
#     time.sleep(2)
#     data = (s.recv(BUFFER_SIZE)).decode('utf_8')
#     print(bcolors.F_Cyan + data)
#     val = getch(bcolors.F_LightMagenta+"game start\n")
#     s.send(val.encode('utf_8'))
#     time.sleep(1)
#     data = s.recv(BUFFER_SIZE)
#     print(bcolors.F_LightYellow+"receiving data:", data.decode('utf_8'))
#     s.close()

import socket

def sending_udp_mess(UDP_IP):
    # UDP_IP = "10.100.102.4"
    UDP_PORT = 5005
    #sending
    # MESSAGE = bytes(0xfeedbeef)+bytes(0x2)+bytes(UDP_PORT)
    MESSAGE = ('0xfeedbeef'+'0x2'+str(UDP_PORT)).encode('utf_8')
    # print("UDP target IP: %s" % UDP_IP)
    # print("UDP target port: %s" % UDP_PORT)
    # print("message: %s" % MESSAGE.decode('utf_8'))
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


def sending_tcp_mess():
    TCP_IP = "10.100.102.11"
    TCP_PORT = 5005
    BUFFER_SIZE = 1024
    MESSAGE = "Hello".encode('utf_8')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()
    print("received data:", data.decode('utf_8'))