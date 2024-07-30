import socket

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the IP address and port number
ip_address = "127.0.0.1"
port_no = 1435      # 0 - 65353 , 0 - 1023 -> Reserved
complete_address = (ip_address, port_no)

# Bind the socket to the address
s.bind(complete_address)

print("Hey, I am Listening...")

try:
    while True:
        # Receive message from client
        message, addr = s.recvfrom(1024)  # Buffer size is 1024 bytes
        print(f"Message from {addr}: {message.decode('utf-8')}")
        
        # Send a response back to the client
        response = input("Enter your response: ")
        s.sendto(response.encode('ascii'), addr)
        print("Response sent.")
except KeyboardInterrupt:
    print("\nServer is shutting down.")
finally:
    s.close()
