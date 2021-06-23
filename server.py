
#server.py

import socket, sys
# Server class
class Server():

    # Default Constructor
    def __init__(self):
        # Declare/Initialize account to the default values
        self.acc_balance = float(100)  # initial_balance is 100
        self.initial_balance = self.acc_balance
        self.deposit_amount = float(0)  # Deposit amount starts with 0
        self.withdrawing_amnt = float(0)  # Withdraw amount initially its 0

    # the deposit method
    def deposit(self, amount, conn):

        self.acc_balance += amount
        # Updating deposit amount
        self.deposit_amount += amount
        # Displaying deposited amount and current balance after adding to the account
        print("Command for deposit received")
        serv_data = "An Amount of $%.2f was deposited to your account " % (amount)
        conn.send(serv_data.encode())

    def withdraw(self, amount, conn):
      
        if self.acc_balance >= amount:
            self.acc_balance -= amount
            self.withdrawing_amnt += amount
            print("Withdraw was $%.2f, current balance is $%.2f" % (amount, self.acc_balance))
            serv_data = "you Withdrawed $%.2f, current balance is $%.2f" % (amount, self.acc_balance)
            #conn.send(serv_data.encode())
        elif amount <= 0:
            print("cannot withdraw a negative amount")
            serv_data = "cannot withdraw a negative amount"
            #conn.send(serv_data.encode())
        elif self.acc_balance < amount:
            print("You cannot withdraw more money than is in the account")
            serv_data = "You cannot withdraw more money than is in the account"
        conn.send(serv_data.encode())

    def display_balance(self, conn):
        #print("Command for check_balance received.")
        print("Your current balance: $%.2f" % (self.acc_balance))
        serv_data = "Your current balance is: $%.2f" % self.acc_balance
        conn.send(serv_data.encode())

if __name__ == '__main__':
    print('Server initialized the bank account')
    print('Server is ready to receive requests')

    host = socket.gethostname()  ### Getting local machine name
    #host = "76.10.8.23"
    port = 7777  ## Reserve a port for your service.
    s = socket.socket()  ###Creating socket object
    s.bind((host, port))  ## Binding host address and port together

    s.listen(5)  ## waiting for client to connection
    c, addr = s.accept()  ## here we accept a new connection with client
    print('Connection from', addr)
    acc = Server() ## Creaeting a account object to access its method and attributes
    while True:
        user_choice = c.recv(1024).decode()
        if user_choice == 'd':
            c.send("Enter amount to deposit".encode())
            amount = float(c.recv(1024).decode())

            ### Deposiiting money in the bank account
            acc.deposit(amount, c)
        elif user_choice == 'w':
            c.send("Enter amount to withdraw".encode())
            amount = float(c.recv(1024).decode())
            ### Withdrawing money from bankAccount
            if amount < 0:
                c.send("Sorry cannot withdraw amounts in negatives ".encode())
            else :
                acc.withdraw(amount, c)
        elif user_choice == 'b':
            #c.send("Command for check_balance sent.".encode())
            #c.send("Your current balance is: $%.2f" % (self.acc_balance).encode)
            ### to display the balance in your bankaccount
            acc.display_balance(c)
        elif user_choice == 'q':
            ### Exitting
            c.send("Thanks! Now Exiting ...".encode())
            sys.exit(1)
        else:
            ###In case of wrong choice, displaying the error message
            print("Incorrect choice!! Please try again")
            c.send("Incorrect choice!! Please try again".encode())

    c.close() 
