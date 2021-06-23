# NETWORKS


In this socket program, there are two main parts for it, mainly the server.py and the client.py 
the socket program was for an automated teller machine (ATM) wherre the user has options to access their bank account.
the four options were to deposit, withdraw, check balance and to quit/ exit the program/ bank account

**server.py
In this file server.py, this is where i was running the server which is basically the one to be run first.
the server basically accepts requests from a user or a client in this case, and works on the request and replies back to the client
with a message or reply to the request made by the client.
for this socket program, the server had multiple funcctions/methods like withdraw, deposit, display_balance and a default constructor
each method had a specific tasks for their respective options from the client/user.
The server.py also has a main function where those mentioned methods get called and help send back replies to the client.py

**client.py
In this file client.py, this is where the main menu for this socket program was at.
this server was getting connected or can only run when the server is already running that way it can first connect to the server 
as it makes requests to the server through same port number and host.

if the two programs ie. client.py and server.py can't get to connect, you can then try to use your local computer's ip address and make it the host
as i tried it too at first, then it worked and was able to connect.

HOW TO RUN IT:
->To run the server.py, type in: python3 server.py
->To run the client.py, type in: python3 client.py
