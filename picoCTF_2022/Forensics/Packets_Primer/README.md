# picoCTF 2022 Packets Primer (Forensics 100 points)
The challenge is the following,

![Figure 1](img/challenge.png) 

We are also given the file [network-dump.flag.pcap](./files/network-dump.flag.pcap). Opening this up on Wireshark showed the following,


![Figure 1](img/packets.png) 

I decided to `Follow TCP stream`, which revealed the flag

![Figure 1](img/flag.png) 

Therefore, the flag is,

`picoCTF{p4ck37_5h4rk_d0565941}`

