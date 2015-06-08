# -*- Coding: utf-8 -*-
#!/usr/bin/python3

# p2p client

import socket, json, time

#server_addr = ('182.92.215.130', 9999)
server_addr = ('localhost', 9999)

def send_message(skt, data):
    skt.send(data.encode())
    recv, t = skt.recvfrom(1000)
    return recv.decode()

# def sendto_message(addr, data):
#     skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     skt.sendto(data, addr)
#     skt.close()

def recv_message(skt):
    recv = skt.recv(1000)
    return recv.decode()

def login(skt, name):
    tmp = {}
    tmp['type'] = 'login'
    tmp['name'] = name
    data = json.dumps(tmp)
    recv = send_message(skt, data)
    return recv

def logout(skt, name):
    tmp = {}
    tmp['type'] = 'logout'
    tmp['name'] = name
    data = json.dumps(tmp)
    recv = send_message(skt, data)
    return recv

def menu_select():
    menu = ('logout', 'send', 'receive', 'query')
    print('\n------menu------')
    for i in range(len(menu)):
        print('%d. %s' % (i, menu[i]))
    print('----------------')
    num = int(input('your choise: '))
    return menu[num]

def query_addr(peer):
    tmp = {}
    tmp['type'] = 'query'
    tmp['name'] = peer
    data = json.dumps(tmp)
    recv = send_message(skt, data)
    return eval(recv)

def p2p_send(skt, peer, data):
    addr = query_addr(peer)
    send_message(skt, data)

if __name__ == '__main__':
    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    skt.connect(server_addr)
    username = input("login name: ")
    try:
        #print(login(skt, username))
        reply = login(skt, username)
        reply = json.loads(reply)
        print('------online------')
        for name in reply['online']:
            print(name)
        print('------------------')
        while True:
            func = menu_select()
            if func == 'logout':
                logout(skt, username)
                break
            elif func == 'query':
                name = input('peer name: ')
                addr = query_addr(name)
                print(addr)
            elif func == 'send':
                peer = input('to who: ')
                data = input('say what: ')
                p2p_send(skt, peer, data)
            elif func == 'receive':
                print(recv_message(skt))
            else:
                print("not implement yet")

    except Exception as e:
        print(e)
    except KeyboardInterrupt as e:
        print('bye')
    finally:
        skt.close()
