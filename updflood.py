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
    for i in range(100000):
        send_udp_packet(destination_ip, destination_port, message)


thread1 = multiprocessing.Process(target=task, args=())
thread2 = multiprocessing.Process(target=task, args=())
thread3 = multiprocessing.Process(target=task, args=())
thread4 = multiprocessing.Process(target=task, args=())
thread5 = multiprocessing.Process(target=task, args=())
thread6 = multiprocessing.Process(target=task, args=())
thread7 = multiprocessing.Process(target=task, args=())
thread8 = multiprocessing.Process(target=task, args=())
thread9 = multiprocessing.Process(target=task, args=())
thread10 = multiprocessing.Process(target=task, args=())
thread11 = multiprocessing.Process(target=task, args=())
thread12 = multiprocessing.Process(target=task, args=())
thread13 = multiprocessing.Process(target=task, args=())
thread14 = multiprocessing.Process(target=task, args=())
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()
thread11.start()
thread12.start()
thread13.start()
thread14.start()







