import socket
from threading import Thread
import rsa
import hashlib

client_pub, client_priv = rsa.newkeys(1024)
server_pub = ''
run = True

def handshake(s):
    global run
    global server_pub
    global client_pub
    msg = rsa.PublicKey.save_pkcs1(client_pub, "PEM")
    s.sendall(msg)
    try:
        rec = s.recv(1024)
        server_pub = rsa.PublicKey.load_pkcs1(rec, "PEM")
        print("Handshake successful")
    except socket.error as msg:
        print("Handshake unsuccessful")
        run = False


def receiveMsg(s):
    global run
    while run:
        try:
            data = s.recv(4096)
            if not data:
                continue
            hashval = data[:32]
            msg = data[32:]
            msg = s_decrypt(msg)

            sha_256 = hashlib.sha256()
            sha_256.update(msg.encode())
            if hashval == sha_256.digest():
                print('\nMessage Received: {}'.format(msg))
                print('\nType Message: ')
            else:
                print('\nUnauthenticated message found')
                print('\nType Message: ')
        except socket.error as msg:
            run = False
        except KeyboardInterrupt:
            run = False
    s.close()     


def sendMsg(s):
    global run
    while run:
        try:
            msg = input("Type Message: ")

            sha_256 = hashlib.sha256()
            sha_256.update(msg.encode())
            hash_val = sha_256.digest()

            data = hash_val + s_encrypt(msg)

            s.sendall(data)
        except socket.error as err:
            run = False
        except KeyboardInterrupt:
            run = False
    s.close()


def s_encrypt(msg):
    msg_1 = msg.encode()
    return rsa.encrypt(msg_1, server_pub)

def s_decrypt(data):
    return rsa.decrypt(data, client_priv).decode()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.10.108', 8000))
    handshake(s)
    if(run):
        # print('\nClient priv: ' + str(client_priv) )
        # print('\nClient pub: ' + str(client_pub) )
        # print('\nServer pub: ' + str(server_pub) )
        rcv = Thread(target=receiveMsg, args=(s, ))
        rcv.start()
        msg = Thread(target=sendMsg, args=(s,))
        msg.start()
    else:
        print("\nProgram Exit")

