from scapy.all import *
import argparse
import os
import sys
import base64

# User Generated Variables
parser = argparse.ArgumentParser(description="Arguments to send data via DNS")
parser.add_argument('-d', '--data', type=str, help="Data to send via DNS", required=True)
parser.add_argument('-c', '--count', type=int, help="Total Count of DNS Transmissions", required=True)
parser.add_argument('-s', '--source', type=str, help="Source Domain Name for Request", required=True)
parser.add_argument('-a', '--dest', type=str, help="Destination IP Address to receive Transmissions", required=True)

# Parse the Command Line Args
args = parser.parse_args()

# Require root privileges
def require_sudo_privileges():
    if os.geteuid() != 0:
        print("This script requires sudo privileges")
        sys.exit(1)

# Encode the payload data using base64
def encode_payload(payload):
    encoded_payload = base64.b64encode(payload.encode()).decode()
    return encoded_payload

# Main Function
if __name__ == "__main__":
    require_sudo_privileges()
    
    # Encode the user-provided payload
    payload = encode_payload(args.data)
    
    # Set the target DNS server and domain name
    count = args.count
    dns_server = args.dest
    domain = args.source

    # Craft DNS Request with User Provided Data
    dns_request = IP(dst=dns_server)/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=domain, qtype="A", qclass="IN"))
    
    # Add the payload as the answer section in the DNS packet
    dns_request[DNS].an = DNSRR(rrname=domain, type="TXT", rclass="IN", ttl=10, rdata=payload)
    dns_request[DNS].ancount = 1
    
    # Send the DNS request packet for the specified count
    for i in range(count):
        send(dns_request)
        # Print the request number
        print(f"Request {i+1} sent.")
