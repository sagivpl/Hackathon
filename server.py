import struct
import time
from threading import *
import traceback
import sys
from socket import *
import socket
import config


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
    total_press_1 = 0
    total_press_2 = 0
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

    for val in group_1:
        total_press_1+=val

    for val in group_2:
        total_press_2+=val

    massage = 'Game over!\n' \
              'Group 1 typed in ' + str(total_press_1) + ' characters. Group 2 typed in ' +  str(total_press_2) + ' characters.\n'

    if total_press_1 > total_press_2:

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
    start_time = time.time()
    while (time.time() - start_time) % 60 < 10:
        sending_udp_mess()
        time.sleep(1)


def sending_udp_mess():
    UDP_IP = config.get_udp_ip_server()
    print("Server started,listening on IP address" + UDP_IP)
    UDP_PORT = config.get_udp_port_server()
    #sending
    frame = [0xfe, 0xed, 0xbe, 0xef]
    type = [0x02]
    s = struct.pack('>H', UDP_PORT)
    msg = bytes(frame) + bytes(type) + bytes(s)


    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    cs.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    try:
        cs.sendto(msg, (UDP_IP, UDP_PORT))

    except:
        pass


def spma_mode(start_time):
    while (time.time() - start_time) % 60 < 10:
        continue

def start_server():
    my_group = group()
    TCP_IP = config.get_tcp_ip_server()
    TCP_PORT = config.get_tcp_port_server()  # arbitrary non-privileged port
    BUFFER_SIZE = config.get_buffer_size()
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
            new_thread = Thread(target=game_mode,
                                args=(connection, ip, TCP_PORT, BUFFER_SIZE, my_group, start_time)).start()
            threads.append(new_thread)
        except:
            print("Thread did not start.")
            traceback.print_exc()
        j += 1
    soc.close()


def game_mode(connection, ip, port, max_buffer_size, my_group, start_time):
    is_active = True
    num = 1
    while is_active:
        client_input = receive_input(connection, max_buffer_size)
        print('data from client  ', client_input)
        if num == 1:
            group_name = client_input.split('\n')
            my_group.add_to_name_dict(ip, group_name[0])
            num += 1
            while (time.time() - start_time) % 60 < 10:
                continue
            massage = create_welcome_massage(my_group)
            connection.sendall(massage.encode("utf_8"))
        elif num == 2 and len(client_input) > 0:
            start_time = time.time()
            my_group.add_to_keyboard_dict(ip, len(client_input))
            spma_mode(start_time)
            massage = create_win_massage(my_group)
            connection.sendall(massage.encode("utf_8"))
            connection.close()
            is_active = False


def receive_input(connection, max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)
    if client_input_size > max_buffer_size:
        print("The input size is greater than expected {}".format(client_input_size))
    decoded_input = client_input.decode("utf8")
    return str(decoded_input)