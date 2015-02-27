# -*- coding: utf-8 -*-
#!/usr/bin/python3

import socket, json

def P2Pclient(my_account, peer_account):
    """
    Arguments:
    - `my_account`:
    - `peer_account`:

    Init(my_account, peer_account)
    端对端初始化
    Send(content)
    Recv(content)
    Close()
    """

def Chat(server_addr):
    """
    Arguments:
    - `server_addr`: like ('localhost', 9999)

    聊天类，包含以下方法：
    Connect(server_addr)
        初始化
    Send(account, content)
        发送内容
    Recv(account, content)
        接收内容

    Online(account)
        上线
    Offline(account)
        下线
    """

server_addr = ('localhost', 9999)

if __name__ == '__main__':
    account  = input('account: ')
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    skt.connect(server_addr)

    skt.send(account.encode('utf8'))
    buf = skt.recv(1024)
    print("receive: ", buf.decode('utf8'))

    skt.close()