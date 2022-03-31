# picoCTF 2022 Operation Oni (Forensics 300 points)
The challenge is the following,

![Figure 1](img/challenge.png) 

We are also given the file [disk.img.gz](./disk.img.gz). I downloaded the file, extracted it. The challenge says to use a `key_file` to ssh to the remote machine, so I assumed that I need to look for a file that contained the key file. I tried to find the partition information using,

`$ mmls disk.img`

And string searched `OPENSSH PRIVATE KEY` using,

`$ strings -t d disk.img | grep -iE "OPENSSH PRIVATE KEY"`

![Figure 1](img/mmls.png) 


There were files that contained `OPENSSH PRIVATE KEY`, so now I have to find the actual contents of the private key file. I used the offset `114562048` and did the operations similar to [Sleuthkit Apprentice](https://github.com/LambdaMamba/CTFwriteups/tree/main/picoCTF_2022/Forensics/Sleuthkit_Apprentice) to find the file contents using the commands, 

`$ expr 114562048 - 105906176`
`$ expr 8655872 / 1024`
`$ ifind -f ext4 -o 206848 -d 8453 disk.img`
`$ icat -f ext4 -o 206848 disk.img 15`


![Figure 1](img/openssh.png) 

This showed the private key, 

```
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACCCLR0HD7N0U/aOCIfE8hu37rqZXPVlAw2nZTCsXzW5iwAAAJhPAhe3TwIX
twAAAAtzc2gtZWQyNTUxOQAAACCCLR0HD7N0U/aOCIfE8hu37rqZXPVlAw2nZTCsXzW5iw
AAAEC64hkpckRMk5Jy2dRmcBTSoQvavri0nLhU6aqeGBT1OIItHQcPs3RT9o4Ih8TyG7fu
uplc9WUDDadlMKxfNbmLAAAADnJvb3RAbG9jYWxob3N0AQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----
```

I also confirmed using Autopsy, and saw that this private key file was in `/root/.ssh/id_ed25519` in the Linux partition that starts at `0000206848`.

![Figure 1](img/autopsy.png) 

So I went into the webshell, and put the private key into `key_file`, and tried to ssh to the remote server using,

`ssh -i key_file -p 64039`


![Figure 1](img/perm.png) 

However, it had the permissions 0664 which was too open so the private key was unusable. Therefore, I changed the permissions to 400 using,


`$ chmod 400 key_file`

And I did ssh again to the remote server, which contained a file called `flag.txt` which contained the flag,


![Figure 1](img/flag.png) 


Therefore, the flag is,

`picoCTF{k3y_5l3u7h_dc01cec5}`
