# time_server.py
import socket
import time
import datetime

# --- Configuration ---
HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 9999       # Port to listen on (non-privileged ports are > 1023)

def run_server():
    # Create a TCP/IP socket
    # AF_INET is for IPv4, SOCK_STREAM is for TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the address and port
        server_socket.bind((HOST, PORT))
        
        # Listen for incoming connections (allow up to 1 queued connection)
        server_socket.listen(1)
        
        print(f"[*] Server listening on {HOST}:{PORT}")

        # --- Main loop to accept new connections ---
        while True:
            try:
                # Wait for a client to connect (this is a blocking call)
                client_socket, client_address = server_socket.accept()
                
                with client_socket:
                    print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")
                    
                    # --- Loop to send time to the connected client ---
                    while True:
                        try:
                            # Get the current time and format it
                            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            
                            # Encode the string to bytes before sending
                            client_socket.sendall(current_time.encode('utf-8'))
                            
                            # Wait for 1 second
                            time.sleep(1)

                        # Handle the case where the client has disconnected
                        except (BrokenPipeError, ConnectionResetError):
                            print(f"[-] Client {client_address[0]}:{client_address[1]} disconnected.")
                            break
                            
            except KeyboardInterrupt:
                print("\n[*] Server is shutting down.")
                break
            except Exception as e:
                print(f"[!] An error occurred: {e}")
                break

if __name__ == '__main__':
    run_server()
