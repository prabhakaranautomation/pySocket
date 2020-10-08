import socket
import pickle

a = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),2233))
s.listen(5)

while True:
    clt,adr= s.accept()
    print(f" Connection to {adr} to established")
    m = {1:"client", 2:"Server"}
    mymsg = pickle.dumps(m)
    mymsg = bytes(f'{len(mymsg):<{a}}',"utf-8") + mymsg
    clt.send(mymsg)
