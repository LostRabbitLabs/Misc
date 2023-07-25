from scapy.all import *
import argparse
import os
import sys
import base64

# ...

def listen_for_dns_responses():
    # Create a raw socket using AF_INET and SOCK_RAW for DNS protocol
    dns_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)

    # Bind the socket to port 53 to listen for DNS responses
    dns_socket.bind(('0.0.0.0', 53))

    try:
        while True:
            # Receive the incoming DNS response packet and its source address
            packet, addr = dns_socket.recvfrom(65535)

            # Parse the packet using Scapy
            ip_packet = IP(packet)

            # Check if the packet contains UDP layer and DNS layer
            if UDP in ip_packet and DNS in ip_packet[UDP]:
                dns_packet = ip_packet[UDP][DNS]

                # Check if the DNS response has an answer section (ANCOUNT > 0)
                if dns_packet.ancount > 0:
                    txt_data_list = []
                    for dns_record in dns_packet[DNSRR]:
                        # Check if the DNS resource record is of type TXT
                        if dns_record.type == 16:  # Type 16 is TXT
                            # If rdata is a list, join the elements before decoding
                            if isinstance(dns_record.rdata, list):
                                txt_data = b''.join(dns_record.rdata).decode()
                            else:
                                txt_data = dns_record.rdata.decode()
                            txt_data_list.append(txt_data)
                            decoded_data = base64.b64decode(txt_data).decode()

                    # Print the decoded data from each TXT record in the answer section
                    print(f"Received DNS response of {len(packet)} bytes from {addr}:")
                    for idx, txt_data in enumerate(txt_data_list):
                        print(f"Decoded Data from TXT record {idx+1}: {decoded_data}")

    except KeyboardInterrupt:
        print("Listening stopped by the user.")
    finally:
        dns_socket.close()

# Main Function
if __name__ == "__main__":
    listen_for_dns_responses()
