from scapy.all import *
import os
import sys
import argparse
import ast

# User Generated Variables
parser = argparse.ArgumentParser(description="Arguments to send data via ICMP")
parser.add_argument('-d', '--data', type=str, help="Data to send via ICMP", required=True)
parser.add_argument('-c', '--count', type=int, help="Total Count of ICMP Transmissions", required=True)
parser.add_argument('-s', '--source', type=str, help="Source IP Address for Transmissions", required=True)
parser.add_argument('-a', '--dest', type=str, help="Destination IP Address to receive Transmissions", required=True)

# Parse the Command Line Args
args = parser.parse_args()

# Check for missing arguments and exit if any is missing
missing_arguments = [arg for arg in ['data', 'count', 'source', 'dest'] if getattr(args, arg) is None]

if missing_arguments:
    print(f"Missing argument(s): {', '.join(missing_arguments)}")
    parser.print_help()
    sys.exit(1)

# Require root privileges
def require_sudo_privileges():
    if os.geteuid() != 0:
        print("This script requires sudo privileges")
        sys.exit(1)

# ICMP Request Constructor
def send_icmp_packets(dest, source, count, data):  
    encoded_data = subprocess.check_output(f'echo {data} | base64', shell=True, text=True).strip()
    icmp_packet = IP(dst=dest, src=source) / ICMP(type=8) / encoded_data.encode()
    
    for _ in range(count):
        send(icmp_packet)
        
# Main Function
if __name__ == "__main__":
    require_sudo_privileges()

    # Safely evaluate the IP addresses and data strings
    destination_ip = args.dest
    source_ip = args.source
    data_to_send = args.data

    send_icmp_packets(destination_ip, source_ip, args.count, data_to_send)
