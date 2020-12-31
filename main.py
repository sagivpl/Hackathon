# import client
# import server
# import concurrent.futures
# import time
# import threading
# from threading import *
# import socket
# import traceback
# import sys
# from scapy.all import*
#
# class group():
#     group_name_dict = {}
#     group_keyboard_dict = {}
#
#     def add_to_name_dict(self, ip, name):
#         self.group_name_dict[ip] = name
#
#
#     def add_to_keyboard_dict(self,ip,keyboard):
#         self.group_keyboard_dict[ip] = keyboard
#
#
# def create_welcome_massage(my_group):
#     my_group_sorted = {k: v for k, v in sorted(my_group.group_name_dict.items(), key=lambda item: item[0])}
#     i = 0
#     group_1 = []
#     group_2 = []
#     for key, value in my_group_sorted.items():
#         if i % 2 == 0:
#             group_1.append(value)
#         else:
#             group_2.append(value)
#         i += 1
#     massage = 'Welcome to keyboard Battle Royal.\n' \
#               'Group 1:\n' \
#               '==\n'
#     for group in group_1:
#         massage += str(group) + '\n'
#     massage += 'Group 2:\n' \
#                '==\n'
#     for group in group_2:
#         massage += str(group) + '\n'
#     return massage
#
#
# def create_win_massage(my_group):
#     my_group_sorted = {k: v for k, v in sorted(my_group.group_keyboard_dict.items(), key=lambda item: item[0])}
#     my_group_sorted_names = {k: v for k, v in sorted(my_group.group_name_dict.items(), key=lambda item: item[0])}
#
#     i = 0
#     group_1 = []
#     group_1_name = []
#     group_2 = []
#     group_2_name = []
#     total_ch_1 = 0
#     total_ch_2 = 0
#     for key, value in my_group_sorted.items():
#         if i % 2 == 0:
#             group_1.append(value)
#         else:
#             group_2.append(value)
#         i += 1
#     i=0
#     for num1 in group_1:
#         total_ch_1 += num1
#     for num2 in group_2:
#         total_ch_2 += num2
#
#     for key, value in my_group_sorted_names.items():
#         if i % 2 == 0:
#             group_1_name.append(value)
#         else:
#             group_2_name.append(value)
#         i += 1
#
#     massage = 'Game over!\n' \
#               'Group 1 typed in ' + str(total_ch_1) +' characters. Group 2 typed in ' + str(total_ch_2) + ' characters.\n'
#     if total_ch_1 > total_ch_2:
#
#         massage += 'Group 1 wins!\n\n' \
#                    'Congratulations to the winners:\n==\n'
#         for group in group_1_name:
#             massage += str(group) + '\n'
#     else:
#         massage += 'Group 2 wins!\n\n' \
#                    'Congratulations to the winners:\n==\n'
#         for group in group_2_name:
#             massage += str(group) + '\n'
#
#     return massage
#
# def udp_thread_handler():
#     print('send server port')
#     # send server port
#     start_time = time.time()
#     while (time.time() - start_time) % 60 < 10:
#         # client.sending_udp_mess("255.255.255.255")
#         # client.sending_udp_mess("10.100.102.11")
#         client.sending_udp_mess("10.100.102.4")
#         time.sleep(1)
#
# def start_server():
#     my_group = group()
#     # TCP_IP =  get_if_addr('eth1')
#     TCP_IP = '10.100.102.15'
#     TCP_PORT = 5005  # arbitrary non-privileged port
#     BUFFER_SIZE = 100000
#     soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     print("Socket created")
#     try:
#         soc.bind((TCP_IP, TCP_PORT))
#     except:
#         print("Bind failed. Error : " + str(sys.exc_info()))
#         sys.exit()
#     soc.listen(20)
#     soc.settimeout(10)
#     print("Socket now listening")
#     # infinite loop- do not reset for every requests
#     start_time = time.time()
#     j = 1
#     while (time.time() - start_time) % 60 < 10:
#
#         # print('accept')
#         try:
#             connection, address = soc.accept()
#             print('after connection' + str(j))
#             ip, TCP_PORT = str(address[0]), str(address[1])
#             print("Connected with " + ip + ":" + TCP_PORT)
#         except:
#             break
#         # break
#         try:
#             print('Thread create' + str(j))
#             Thread(target=client_thread,
#             args=(connection, ip, TCP_PORT, BUFFER_SIZE, my_group, start_time)).start()
#
#         except:
#             print("Thread did not start.")
#             traceback.print_exc()
#         j += 1
#     soc.close()
#
#
# def client_thread(connection, ip, port, max_buffer_size, my_group, start_time):
#     print('thread  ' + ip)
#     is_active = True
#     num = 1
#     while is_active:
#         client_input = receive_input(connection, max_buffer_size)
#         print('data from client  ' , client_input)
#         if num == 1:
#             group_name = client_input.split('\n')
#             my_group.add_to_name_dict(ip, group_name[0])
#             current_time = time.time()
#             num += 1
#             while (time.time() - start_time) % 60 < 10:
#                 continue
#             massage = create_welcome_massage(my_group)
#             connection.sendall(massage.encode("utf_8"))
#         elif num == 2 and len(client_input) > 0:
#             start_time = time.time()
#             my_group.add_to_keyboard_dict(ip, len(client_input))
#             while (time.time() - start_time) % 60 < 10:
#                 continue
#             massage = create_win_massage(my_group)
#             # massage = 'len: ' + str(len(client_input))
#             connection.sendall(massage.encode("utf_8"))
#             connection.close()
#             is_active = False
#
#
# def receive_input(connection, max_buffer_size):
#     client_input = connection.recv(max_buffer_size)
#     client_input_size = sys.getsizeof(client_input)
#     if client_input_size > max_buffer_size:
#         print("The input size is greater than expected {}".format(client_input_size))
#     decoded_input = client_input.decode("utf8")
#     # result = process_input(decoded_input)
#     return str(decoded_input)
#
# #
# # def process_input(input_str):
# #     # print("Processing the input received from client")
# #     return str(input_str).upper()
#
#
# if __name__ == '__main__':
#     i_server = True
#     i_client = False
#     if i_server:
#         # ip = get_if_addr('eth1')
#         # print(ip)
#         # tcp thread handler
#         tcp_thread = threading.Thread(target=start_server)
#         # udp thread handler
#         udp_thread = threading.Thread(target=udp_thread_handler)
#         tcp_thread.start()
#         udp_thread.start()
#         udp_thread.join()
#         tcp_thread.join()
#         print('workes!')
#     if i_client:
#         print('i client')
#         host_config = server.receving_udp_mess()
#         #send to the server the team name
#         client.sending_tcp_mess(host_config)


import client
import server
import concurrent.futures
import time
import threading
from threading import *
import socket
import traceback
import sys


class group():
    group_name_dict = {}
    group_keyboard_dict = {}

    def add_to_name_dict(self, ip, name):
        self.group_name_dict[ip] = name


    def add_to_keyboard_dict(self,ip,keyboard):
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
    group_1_name = []
    group_2 = []
    group_2_name = []
    for key, value in my_group_sorted.items():
        if i % 2 == 0:
            group_1.append(value)
        else:
            group_2.append(value)
        i += 1
    i=0
    for key, value in my_group_sorted_names.items():
        if i % 2 == 0:
            group_1_name.append(value)
        else:
            group_2_name.append(value)
        i += 1

    massage = 'Game over!\n' \
              'Group 1 typed in ' + str(group_1[0]) +' characters. Group 2 typed in ' + str(group_2[0]) + ' characters.\n'
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
        client.sending_udp_mess("10.100.102.4")
        client.sending_udp_mess("10.100.102.11")
        # with concurrent.futures.ThreadPoolExecutor(max_workers=num_of_threads) as executor:
        #     executor.submit(udp_thread_handler)
        # executor.shutdown()
        # print('sleep')
        time.sleep(1)

    # print('receving the team name')
    # receving the team name
    # server.receving_tcp_mess()


def start_server():
    my_group = group()
    TCP_IP = "10.100.102.15"
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
        print('data from client  ' , client_input)
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

#
# def process_input(input_str):
#     # print("Processing the input received from client")
#     return str(input_str).upper()


if __name__ == '__main__':
    # tcp thread handler
    tcp_thread = threading.Thread(target=start_server)
    # with concurrent.futures.ThreadPoolExecutor(max_workers=num_of_threads) as executor:
    #     executor.submit(start_server)

    # udp thread handler
    udp_thread = threading.Thread(target=udp_thread_handler)
    # num_of_threads = 1
    # start_time = time.time()
    # while (time.time() - start_time) % 60 < 10:
    #     with concurrent.futures.ThreadPoolExecutor(max_workers=num_of_threads) as executor:
    #         executor.submit(udp_thread_handler)
    #         # executor.shutdown()
    #     print('sleep')
    #     time.sleep(1)
    print(tcp_thread.getName())
    tcp_thread.start()
    print(udp_thread.getName())
    udp_thread.start()
    udp_thread.join()
    tcp_thread.join()
    print('workes!')
