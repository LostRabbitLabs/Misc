# Welcome to the ARP Poisoner utility from x3dnesse

This utility can be used to poison an entire subnet's ARP cache. Of course, you will want to make sure that they are not using static ARP entries or something like that.

#### Tying it in with other attacks

You could act as a man-in-the-middle for all the devices you poison if you want.

Aka enabling IP forwarding

```
echo 1 > /proc/sys/net/ipv4/ip_forward
```

Then tcpdump or something you like

#### Usage

```
sudo bash arp_poisoner.sh
```

The script will ask you the rest of the questions. 

#### Dependancies

1. nmap
2. dsniff (for arpspoof)
