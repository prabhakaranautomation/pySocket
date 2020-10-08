import socket
import pickle

a = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(),2233))

while True:
    complete_info:b''
    rec_msg = True
    while True:
        mymsg = s.recv(16)
        if rec_msg:
            print(f"The length of the message = {mymsg[:a]}")
            x = int(mymsg[:a])
            rec_msg = False
            complete_info += mymsg
        if len(complete_info)-a == x:
            print("Received the complete info")
            print(complete_info[a:])
            m = pickle.loads(complete_info[a:])
            print(m)
            rec_msg = True
            complete_info = b''
    print(complete_info)