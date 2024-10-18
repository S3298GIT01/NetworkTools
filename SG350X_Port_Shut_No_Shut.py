import paramiko
import time

def ssh_connect_and_execute(ip, username, password, commands):
    # Create an SSH client
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the server
        client.connect(ip, username=username, password=password)

        # Open a session
        shell = client.invoke_shell()
        time.sleep(1)

        # Execute the commands
        for command in commands:
            shell.send(command + '\n')
            time.sleep(1)  # Wait for the command to be processed

        # Wait for the command to complete
        time.sleep(2)
        
    finally:
        # Close the connection
        client.close()

if __name__ == "__main__":
    ip_address = "192.168.10.22"
    username = "root"
    password = "your_password_here"

    # Commands to shut down the interfaces
    shutdown_commands = [
        "configure terminal",
        "interface GE1/0/13",
        "shutdown",
        "interface GE1/0/19",
        "shutdown"
    ]

    # Commands to bring the interfaces back up
    startup_commands = [
        "configure terminal",
        "interface GE1/0/13",
        "no shutdown",
        "interface GE1/0/19",
        "no shutdown"
    ]

    # Shut down the interfaces
    ssh_connect_and_execute(ip_address, username, password, shutdown_commands)

    # Wait for 1 hour (3600 seconds)
    print("Waiting for 1 hour...")
    time.sleep(3600)

    # Bring the interfaces back up
    ssh_connect_and_execute(ip_address, username, password, startup_commands)

    print("Interfaces have been brought back up.")
