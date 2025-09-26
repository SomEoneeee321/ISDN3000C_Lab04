import socket
import time
import json

# --- TODO: Configure these values --- #
SERVER_IP = '192.168.50.95'  # The IP address of your RDK-X5
SERVER_PORT = 9999
REQUEST_MESSAGE = "GET_DATA" # The message your server expects
# --- END OF TODO --- #

def run_client():
    while True:
        print("-" * 30)
        print(f"Attempting to connect to {SERVER_IP}:{SERVER_PORT}...")
        try:
            # --- TODO: YOUR CODE GOES HERE --- #
            # 1. Create a socket object.
            # 2. Use a 'with' statement for automatic cleanup.
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                # 3. Connect to the server.
                client_socket.connect((SERVER_IP, SERVER_PORT))
                print("Connected to the server.")
                
                # 4. Send the REQUEST_MESSAGE, encoded to bytes.
                client_socket.sendall(REQUEST_MESSAGE.encode('utf-8'))
                print(f"Sent request: {REQUEST_MESSAGE}")
                
                # 5. Receive the response from the server (e.g., up to 4096 bytes).
                response_bytes = client_socket.recv(4096)
                
                # 6. Decode the response from bytes to a string.
                response_string = response_bytes.decode('utf-8')
                
                # 7. (Recommended) If you used JSON, parse the string into a dictionary.
                try:
                    data = json.loads(response_string)
                    is_json = True
                except json.JSONDecodeError:
                    data = response_string
                    is_json = False
                
                # 8. Print the received data in a user-friendly format.
                print("Received response:")
                if is_json:
                    print(json.dumps(data, indent=2))  # Pretty print JSON
                else:
                    print(data)
            # --- END OF TODO --- #

        except ConnectionRefusedError:
            print("Connection failed. Is the server running?")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Wait for 60 seconds before the next request
        print("\nWaiting for 60 seconds...")
        time.sleep(60)

if __name__ == "__main__":
    run_client()