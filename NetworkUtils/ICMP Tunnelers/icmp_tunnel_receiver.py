import socket
import os
import struct
import subprocess
import base64

def receive_icmp_packets():
    # Create a raw socket using AF_INET and SOCK_RAW for ICMP protocol
    icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)

    # Bind the socket to a specific interface and port (optional)
    # For receiving all ICMP packets, binding is not required.

    # Set socket options to allow receiving of IP headers
    icmp_socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    try:
        while True:
            # Receive the incoming ICMP packet and its source address
            packet, addr = icmp_socket.recvfrom(65535)

            # Parse the received packet to extract the ICMP payload
            ip_header_length = (packet[0] & 0x0F) * 4
            icmp_payload = packet[ip_header_length + 8:]

            # Display the data portion of the ICMP payload
            print(f"Received {len(icmp_payload)} bytes from {addr}:")
            print(icmp_payload)
            # Decode the ICMP payload using base64
            try:
                decoded_data = base64.b64decode(icmp_payload).decode()
            except base64.binascii.Error as e:
                decoded_data = f"Decoding Error: {e}"
            print("Decoded data:", decoded_data)

    except KeyboardInterrupt:
        print("Receiving stopped by the user.")
    finally:
        icmp_socket.close()
        
# Main Function, checks for Root for the Raw Sockets
if __name__ == "__main__":
    if os.geteuid() != 0:
        print("This script requires root privileges to run.")
    else:
        receive_icmp_packets()
