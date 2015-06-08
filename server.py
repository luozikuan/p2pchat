# -*- coding: utf-8 -*-
#!/usr/bin/python3

# p2p server

import socket, json, sys, time

server_addr = ('localhost', 9999)
client_ip = {}

def client_login(skt, json_data):
    name = json_data['name']
    addr = json_data['addr']
    client_ip[name] = addr
    reply = {}
    reply['online'] = get_online_user()
    skt.sendto(json.dumps(reply).encode(), addr)
    print('[%s] login, addr is %s' % (name, addr))

def get_online_user():
    arr = []
    for name in client_ip:
        arr.append(name)
    return arr

def client_logout(skt, json_data):
    name = json_data['name']
    addr = json_data['addr']
    del client_ip[name]
    skt.sendto(b'logout success', addr)
    print('[%s] logout, addr is %s' % (name, addr))

def query(skt, json_data):
    name = json_data['name']
    addr = json_data['addr']
    tmp = {
        'type' : 'through',
        'addr' : client_ip[name]
    }
    skt.sendto(json.dumps(tmp), addr)
    tmp['addr'] = addr
    skt.sendto(json.dumps(tmp), client_ip[name])

handler = {
    'login' : client_login,
    'logout': client_logout,
    'query' : query,
}

if __name__ == '__main__':
    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    skt.bind(server_addr)

    try:
        while True:
            data, addr = skt.recvfrom(1000)
            data = data.decode()
            json_data = json.loads(data)
            json_data['addr'] = addr
            handler[json_data['type']](skt, json_data)
    except Exception as e:
        print(e)
    except KeyboardInterrupt as e:
        print('bye')
    finally:
        skt.close()