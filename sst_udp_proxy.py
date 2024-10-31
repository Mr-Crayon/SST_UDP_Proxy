import socket

LOCAL_PORT = 27000 ## Defined to catch SST UDP broadcast
DESTINATION_HOST = '192.168.0.25' ## Video board IP
DESTINATION_PORT = 3002 ## Daktronics RTD UDP port on video board

def udp_proxy():
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as listen_socket:
      listen_socket.bind(('0.0.0.0', LOCAL_PORT)) ## listen on all interfaces
      listen_socket.settimeout(None) ## No timeout for continuous listening
      print(f"Proxy listening on port {LOCAL_PORT}...")
      with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as forward_socket:
        while True:
          try:
            data, client_address = listen_socket.recvfrom(4096) ## Pulling data from received packet
            forward_socket.sendto(data, (DESTINATION_HOST, DESTINATION_PORT))
            print(data)
          except socket.error as e:
            print(f"Socket error: {e}")
            continue
  except Exception as e:
    print(f"Unexpected error: {e}")

if __name__ == "__main__":
  udp_proxy()