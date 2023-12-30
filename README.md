# Command Line Chat Script

This is a simple command line chat script built with Python. It allows users to send and receive text messages in real time over the command line(e.g Command Prompt).

Features
Real-time text messaging between multiple clients.
Command line interface for easy use and integration.
Uses Python’s built-in socket and threading libraries for network communication and concurrent handling of clients.
How to Use
Start the Server: Run the script with the server argument to start the server.
```python chat.py server```

Connect a Client: In a new terminal window, run the script with the client argument to start a new client and connect it to the server.
```python chat.py client```

Send and Receive Messages: Once connected, you can send messages from the client to the server and they will be broadcasted to all other connected clients.
Using ngrok for Remote Connections
If you want to use this script to chat with someone on a different PC, you can use ngrok. ngrok is a service that allows you to expose your local server to the internet, making it accessible from any device with an internet connection.

Here’s how you can set it up:

Download ngrok: Visit the ngrok download page and download the version for your operating system.

Start ngrok: In a new terminal window, navigate to the directory where you downloaded ngrok and start it on the same port as your chat server (1234 in this case).

```./ngrok tcp 1234```

Connect to the Server: ngrok will provide a URL that you can use to connect to your server. Use this URL in place of ```socket.gethostname()``` when connecting the client.
Python.

```s.connect(("0.tcp.ngrok.io", 1234))```  # replace "0.tcp.ngrok.io" with your ngrok URL
Now you can chat with anyone, anywhere in the world!
