import socket
from threading import Thread
import rsa

server_pub, server_priv = rsa.newkeys(1024)
client_pub = ''
run = True

def handshake(conn):
    global run
    global client_pub
    global server_pub
    msg = rsa.PublicKey.save_pkcs1(server_pub, "PEM")
    conn.sendall(msg)
    try:
        rec = conn.recv(1024)
        client_pub = rsa.PublicKey.load_pkcs1(rec, "PEM")
        print("Handshake successful")
    except socket.error as msg:
        print("Handshake unsuccessful")
        run = False


def receiveMsg(conn):
    global run
    while run:
        try:
            data = conn.recv(1024)
            if not data:
                continue
            msg = s_decrypt(data)
            print('\nMessage Received: {}'.format(msg))
            print('\nType Message: ')
        except socket.error as msg:
            print(msg)
            run = False
        except KeyboardInterrupt:
            run = False
    conn.close()


def sendMsg(conn):
    global run
    while run:
        try:
            msg = input("Type Message: ")
            data = s_encrypt(msg)
            conn.sendall(data)
        except socket.error as msg:
            run = False
        except KeyboardInterrupt:
            run = False
    conn.close()


def listenConnection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 8000))
    s.listen(1)
    conn, addr = s.accept()
    print('Server accepted client connection...')
    return conn, addr, s


def s_encrypt(msg):
    msg_1 = msg.encode()
    return rsa.encrypt(msg_1, client_pub)

def s_decrypt(data):
    return rsa.decrypt(data, server_priv).decode()



if __name__ == '__main__':
    conn, addr, s = listenConnection()
    handshake(conn)
    if(run):
        # print('\nServer priv: ' + str(server_priv) )
        # print('\nServer pub: ' + str(server_pub) )
        # print('\nClient pub: ' + str(client_pub) )
        
        rcv = Thread(target=receiveMsg, args=(conn, ))
        rcv.start()
        msg = Thread(target=sendMsg, args=(conn,))
        msg.start()
    else:
        print("\nProgram Exit")