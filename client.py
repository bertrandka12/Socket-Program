

#client.py

import socket

def menu():
    print("**********Welcome to ATM (socket program)********")
    print("Enter d for Deposit.")
    print("Enter w for Withdraw")
    print("Enter b for checking Balance")
    print("Enter q to Quit")
host = socket.gethostname()
#host = "76.10.8.23"
port = 7777
s = socket.socket()

s.connect((host, port))

while True:
    menu()
    print("PLEASE ENTER YOUR CHOICE HERE:_ ")
    user_choix = input()
    mesag = str.encode(str(user_choix), 'utf-8')
    s.send(mesag)
    print(s.recv(1024).decode())
    if user_choix == 'd' or user_choix == 'w':

        user_choix = input()
        mesag = str.encode(str(user_choix), 'utf-8')
        s.send(mesag)
        print(s.recv(1024).decode())

    elif user_choix == 'q':
        #to quit or exit the program
        exit()
s.close
