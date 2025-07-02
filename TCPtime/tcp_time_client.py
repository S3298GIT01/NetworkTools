# time_client.py
import socket

# --- Configuration ---
# Use 'localhost' or '127.0.0.1' if running on the same machine.
# If the server is on another PC, use its LAN IP address (e.g., '192.168.1.105').
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 9999

def run_client():
    # Create a TCP/IP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            # Connect the socket to the server's address and port
            print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
            client_socket.connect((SERVER_HOST, SERVER_PORT))
            print("[+] Connected to the server.")

            # --- Loop to receive data from the server ---
            while True:
                # Receive data from the server (buffer size 1024 bytes)
                data = client_socket.recv(1024)

                # If recv returns an empty byte string, the server has closed the connection
                if not data:
                    print("[-] Server closed the connection. Exiting.")
                    break

                # Decode the bytes back to a string and print it
                print(f"Server time: {data.decode('utf-8')}")

        except ConnectionRefusedError:
            print(f"[!] Connection refused. Is the server running on {SERVER_HOST}:{SERVER_PORT}?")
        except KeyboardInterrupt:
            print("\n[*] Client is shutting down.")
        except Exception as e:
            print(f"[!] An error occurred: {e}")

if __name__ == '__main__':
    run_client()
