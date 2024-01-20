import socket 

def is_server_down(host, port):
    try:
        s = socket.create_connection((host, port), timeout=2)
        return False
    except socket.error as e:
        return True