import msvcrt
import socket
import struct
import time

import config
from getch import _Getch


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    F_Default = "\x1b[39m"
    F_Black = "\x1b[30m"
    F_Red = "\x1b[31m"
    F_Green = "\x1b[32m"
    F_Yellow = "\x1b[33m"
    F_Blue = "\x1b[34m"
    F_Magenta = "\x1b[35m"
    F_Cyan = "\x1b[36m"
    F_LightGray = "\x1b[37m"
    F_DarkGray = "\x1b[90m"
    F_LightRed = "\x1b[91m"
    F_LightGreen = "\x1b[92m"
    F_LightYellow = "\x1b[93m"
    F_LightBlue = "\x1b[94m"
    F_LightMagenta = "\x1b[95m"
    F_LightCyan = "\x1b[96m"
    F_White = "\x1b[97m"

def receving_udp_mess():
    UDP_IP = config.get_udp_ip_client()
    UDP_PORT = config.get_udp_port_client()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    sock.bind((UDP_IP, UDP_PORT))
    BUFFER_SIZE = config.get_buffer_size()
    while True:
        data, addr = sock.recvfrom(BUFFER_SIZE)  # buffer size is 1024 bytes
        # data = data.decode('utf_8')
        if not (data[:4] == bytes([0xfe, 0xed, 0xbe, 0xef])) or not (data[4] == 0x02):
            print("Invalid format.")
        print("received message: %s" % data)
        ip_server = addr[0]
        port_server = struct.unpack('>H', data[5:7])[0]
        return [ip_server, port_server]


def sending_tcp_mess(TCP_IP, TCP_PORT):
    BUFFER_SIZE = config.get_buffer_size()
    MESSAGE = "VintKahn\n".encode('utf_8')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    time.sleep(2)
    #game mood
    start_time = time.time()
    while time.time() - start_time < 10:
        s.send(_Getch())
    data = s.recv(BUFFER_SIZE)
    while True:
        try:
            if msvcrt.kbhit():
              MESSAGE = _Getch()
              s.send(MESSAGE)
            data = s.recv(BUFFER_SIZE)
            if len(data) == 0:
                break
            print(bcolors.F_Cyan + data.decode('utf_8'))
        except:
            pass
    print(bcolors.F_Cyan + data.decode('utf_8'))
    val = input(bcolors.F_LightMagenta+"game start\n")
    s.send(val.encode('utf_8'))
    time.sleep(1)
    data = s.recv(BUFFER_SIZE)
    print(bcolors.F_LightYellow+"receiving data:", data.decode('utf_8'))
    s.close()

