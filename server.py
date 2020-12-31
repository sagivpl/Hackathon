# import socket
# import struct
#
# from scapy.all import*
#
# def receving_udp_mess():
#     host_config = []
#     UDP_IP = "0.0.0.0"
#     UDP_PORT = 13117
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
#     sock.bind((UDP_IP, UDP_PORT))
#     # while True:
#     data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
#     print("received message: %s" % data)
#     if not (data[:4] == bytes([0xfe, 0xed, 0xbe, 0xef])) or not (data[4] == 0x02):
#         print("Invalid format.")
#     host_ip = addr[0]
#     port_host = struct.unpack('>H', data[5:7])[0]
#     host_config.append(host_ip)
#     host_config.append(port_host)
#     return host_config
#
#
#
# def receving_tcp_mess():
#     # TCP_IP =  get_if_addr('eth1')
#     print('sagiv')
#     TCP_IP = '10.100.102.15'
#     TCP_PORT = 5005
#     BUFFER_SIZE = 100000  # Normally 1024, but we want fast response
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.bind((TCP_IP, TCP_PORT))
#     s.listen(1)
#     conn, addr = s.accept()
#     print('Connection address:', addr)
#     while 1:
#         data = conn.recv(BUFFER_SIZE)
#         if not data:
#             break
#         print("received data:", data.decode('utf_8'))
#         data = data.decode('utf_8')
#         # print(data)
#         data = data.split('\n')
#         data_dict = {data[0]: data[1]}
#         print(data_dict)
#         conn.send('ok'.encode('utf_8'))  # echo
#     # conn.close()

import socket

# def receving_udp_mess():
#     UDP_IP = "10.100.102.4"
#     UDP_PORT = 5005
#     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
#     sock.bind((UDP_IP, UDP_PORT))
#     while True:
#         data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
#         print("received message: %s" % data)



# def receving_tcp_mess():
#     TCP_IP = "10.100.102.11"
#     TCP_PORT = 5005
#     BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.bind((TCP_IP, TCP_PORT))
#     s.listen(1)
#     conn, addr = s.accept()
#     print('Connection address:', addr)
#     while 1:
#         data = conn.recv(BUFFER_SIZE)
#         if not data:
#             break
#         print("received data:", data.decode('utf_8'))
#         data = data.decode('utf_8')
#         # print(data)
#         data = data.split('\n')
#         data_dict = {data[0]: data[1]}
#         print(data_dict)
#         conn.send('ok'.encode('utf_8'))  # echo
    # conn.close()


import client
import server
import concurrent.futures
import time
import threading
from threading import *
import socket
import traceback
import sys
from socket import *
import socket

class group():
    group_name_dict = {}
    group_keyboard_dict = {}

    def add_to_name_dict(self, ip, name):
        self.group_name_dict[ip] = name

    def add_to_keyboard_dict(self, ip, keyboard):
        self.group_keyboard_dict[ip] = keyboard


def create_welcome_massage(my_group):
    my_group_sorted = {k: v for k, v in sorted(my_group.group_name_dict.items(), key=lambda item: item[0])}
    i = 0
    group_1 = []
    group_2 = []
    for key, value in my_group_sorted.items():
        if i % 2 == 0:
            group_1.append(value)
        else:
            group_2.append(value)
        i += 1
    massage = 'Welcome to keyboard Battle Royal.\n' \
              'Group 1:\n' \
              '==\n'
    for group in group_1:
        massage += str(group) + '\n'
    massage += 'Group 2:\n' \
               '==\n'
    for group in group_2:
        massage += str(group) + '\n'
    return massage


def create_win_massage(my_group):
    my_group_sorted = {k: v for k, v in sorted(my_group.group_keyboard_dict.items(), key=lambda item: item[0])}
    my_group_sorted_names = {k: v for k, v in sorted(my_group.group_name_dict.items(), key=lambda item: item[0])}

    i = 0
    group_1 = []
    group_1.append(0)
    group_1_name = []
    group_2 = []
    group_2.append(0)
    group_2_name = []

    for key, value in my_group_sorted.items():
        if i % 2 == 0:
            group_1.append(value)
        else:
            group_2.append(value)
        i += 1
    i = 0
    for key, value in my_group_sorted_names.items():
        if i % 2 == 0:
            group_1_name.append(value)
        else:
            group_2_name.append(value)
        i += 1

    massage = 'Game over!\n' \
              'Group 1 typed in ' + str(group_1[0]) + ' characters. Group 2 typed in ' + str(
        group_2[0]) + ' characters.\n'
    if len(group_1) > len(group_2):

        massage += 'Group 1 wins!\n\n' \
                   'Congratulations to the winners:\n==\n'
        for group in group_1_name:
            massage += str(group) + '\n'
    else:
        massage += 'Group 2 wins!\n\n' \
                   'Congratulations to the winners:\n==\n'
        for group in group_2_name:
            massage += str(group) + '\n'

    return massage


def udp_thread_handler():
    print('send server port')
    # send server port
    num_of_threads = 1
    start_time = time.time()
    while (time.time() - start_time) % 60 < 10:
        # client.sending_udp_mess("192.168.1.22")
        # client.sending_udp_mess("192.168.1.23")
        sending_udp_mess()
        # with concurrent.futures.ThreadPoolExecutor(max_workers=num_of_threads) as executor:
        #     executor.submit(udp_thread_handler)
        # executor.shutdown()
        # print('sleep')
        time.sleep(1)

    # print('receving the team name')
    # receving the team name
    # server.receving_tcp_mess()


def sending_udp_mess():
    # UDP_IP = "10.100.102.4"
    UDP_PORT = 5005
    #sending
    MESSAGE = ('0xfeedbeef'+'0x2'+str(UDP_PORT))
    MESSAGE = bytes(MESSAGE,'utf-8')

    # sock = socket.socket(socket.AF_INET, # Internet
    #                      socket.SOCK_DGRAM) # UDP
    # sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    cs.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    try:
        cs.sendto(MESSAGE, ('255.255.255.255', UDP_PORT))
    except:
        pass


def start_server():
    my_group = group()
    TCP_IP = "192.168.1.14"
    TCP_PORT = 5005  # arbitrary non-privileged port
    BUFFER_SIZE = 100000
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    threads = []
    print("Socket created")
    try:
        soc.bind((TCP_IP, TCP_PORT))
    except:
        print("Bind failed. Error : " + str(sys.exc_info()))
        sys.exit()
    soc.listen(2)
    soc.settimeout(10)
    print("Socket now listening")
    # infinite loop- do not reset for every requests
    start_time = time.time()
    j = 1
    while (time.time() - start_time) % 60 < 10:

        # print('accept')
        try:
            connection, address = soc.accept()
            print('after connection' + str(j))
            ip, TCP_PORT = str(address[0]), str(address[1])
            print("Connected with " + ip + ":" + TCP_PORT)
        except:
            break
        # break
        try:
            print('Thread create' + str(j))
            new_thread = Thread(target=client_thread,
                                args=(connection, ip, TCP_PORT, BUFFER_SIZE, my_group, start_time)).start()
            threads.append(new_thread)
        except:
            print("Thread did not start.")
            traceback.print_exc()
        j += 1
    soc.close()


def client_thread(connection, ip, port, max_buffer_size, my_group, start_time):
    print('thread  ' + ip)
    is_active = True
    num = 1
    while is_active:
        client_input = receive_input(connection, max_buffer_size)
        print('data from client  ', client_input)
        if num == 1:
            group_name = client_input.split('\n')
            my_group.add_to_name_dict(ip, group_name[0])
            current_time = time.time()
            num += 1
            while (time.time() - start_time) % 60 < 10:
                continue
            massage = create_welcome_massage(my_group)
            connection.sendall(massage.encode("utf_8"))
        elif num == 2 and len(client_input) > 0:
            start_time = time.time()
            my_group.add_to_keyboard_dict(ip, len(client_input))
            while (time.time() - start_time) % 60 < 10:
                continue
            massage = create_win_massage(my_group)
            # massage = 'len: ' + str(len(client_input))
            connection.sendall(massage.encode("utf_8"))
            connection.close()
            is_active = False


def receive_input(connection, max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)
    if client_input_size > max_buffer_size:
        print("The input size is greater than expected {}".format(client_input_size))
    decoded_input = client_input.decode("utf8")
    # result = process_input(decoded_input)
    return str(decoded_input)
