from scapy.arch import get_if_addr

BUFFER_SIZE = 100000

TCP_IP_SERVER = get_if_addr('eth1')
TCP_IP_CLIENT = ""

UDP_IP_SERVER = '255.255.255.255'
UDP_IP_CLIENT = "0.0.0.0"

TCP_PORT_SERVER = "0"
TCP_PORT_CLIENT = "0"

UDP_PORT_SERVER = "0"
UDP_PORT_CLIENT = "0"

def get_tcp_ip_server():
    return TCP_IP_SERVER

def get_tcp_ip_client():
    return TCP_IP_CLIENT

def get_udp_ip_server():
    return UDP_IP_SERVER

def get_udp_ip_client():
    return UDP_IP_CLIENT

def get_tcp_port_server():
    return TCP_PORT_SERVER

def get_tcp_port_client():
    return TCP_PORT_CLIENT

def get_udp_port_server():
    return UDP_PORT_SERVER

def get_udp_port_client():
    return UDP_PORT_CLIENT

def get_buffer_size():
    return BUFFER_SIZE