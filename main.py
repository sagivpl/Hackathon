import client
import server
import time
import threading


if __name__ == '__main__':

    my_server = True
    my_client = False

    if my_server:
        #server
        # tcp thread handler
        tcp_thread = threading.Thread(target=server.start_server)
        # udp thread handler
        udp_thread = threading.Thread(target=server.udp_thread_handler)
        tcp_thread.start()
        udp_thread.start()
        udp_thread.join()
        tcp_thread.join()

    if my_client:
        #client
        arr_server_data = client.receving_udp_mess()
        time.sleep(3)
        port_server = arr_server_data[1]
        ip_server = arr_server_data[0]
        client.sending_tcp_mess(ip_server, int(port_server))
