import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# target_ip = "192.168.121.134"
target_ip = "127.0.0.1"
target_port = 1435      # 0 - 65353 , 0 - 1023 -> Reserved
target_address = (target_ip, target_port)

while True:
    message = input("Please enter your message: ")
    message_encrypted = message.encode('ascii')

    s.sendto(message_encrypted, target_address)
    print("Your message is sent....")
    
    # Receive response from server
    response, server_addr = s.recvfrom(1024)
    print(f"Response from server: {response.decode('utf-8')}")
    
    permission = input("Do you want to quit this program? Press Y/N: ")
    
    if permission.lower() == "y":
        break

s.close()
