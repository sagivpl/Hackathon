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

def receving_udp_mess():
    UDP_IP = "10.100.102.4"
    UDP_PORT = 5005
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    sock.bind((UDP_IP, UDP_PORT))
    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        print("received message: %s" % data)



def receving_tcp_mess():
    TCP_IP = "10.100.102.11"
    TCP_PORT = 5005
    BUFFER_SIZE = 1024  # Normally 1024, but we want fast response
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    conn, addr = s.accept()
    print('Connection address:', addr)
    while 1:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        print("received data:", data.decode('utf_8'))
        data = data.decode('utf_8')
        # print(data)
        data = data.split('\n')
        data_dict = {data[0]: data[1]}
        print(data_dict)
        conn.send('ok'.encode('utf_8'))  # echo
    # conn.close()