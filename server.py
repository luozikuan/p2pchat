# -*- coding: utf-8 -*-
#!/usr/bin/python3

import socket, json, sys

def P2Pserver():
    """
    """

server_addr = ('localhost', 9999)

if __name__ == '__main__':
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    skt.bind(server_addr)
    skt.listen(5)
    print("listen...")

    while True:
        try:
            conn, addr = skt.accept()
        except KeyboardInterrupt:
            skt.close()
            print("\nexit...")
            sys.exit(0)
        print("get a new connection ", addr)

        conn.settimeout(5)
        buf = conn.recv(1024).decode('utf8')
        print("receive: ", buf)

        if '0' == buf:
            conn.send(u'exit'.encode('utf8'))
        else:
            conn.send((u'welcome %s' % buf).encode('utf8'))

        conn.close()