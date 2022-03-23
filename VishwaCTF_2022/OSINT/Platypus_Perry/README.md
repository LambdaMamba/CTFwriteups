# Platypus Perry (Category: OSINT)
The challenge is the following,

![Figure 1](img/challenge.png) 


Here, we are given the file [Hire-me.mp3](./files/Hire-me.mp3). 
The challenge description says `Agent John got some information that a group of people hid a bag of LSD on a dog. He needs to find the dog before it reaches the dealer.`, which is a pretty ambiguous challenge description but tells us that we should be looking for a `dog`.



When I listened to [Hire-me.mp3](./files/Hire-me.mp3), I couldn't make out anything meaningful, so I opened it up on Audacity.

![Figure 2](img/audio1.png) 

It sounded like it was in reverse, so I reversed the audio and amplified it.

![Figure 3](img/audio2.png) 

This processed audio file can be found in [Hire-me-rev.mp3](./files/Hire-me-rev.mp3). 

I listened to the audio and wrote down the letters, which gave me,

`nierbrustiushcihwgnihtemosulletthgimlabmobdivadyugruo`

Since the audio was in reverse, I assumed this text might also be in reverse, so I went ahead and reversed the text,

`ourguydavidbombalmighttellusomethingwhichsuitsurbrein`

And I added spaces to the text,

`our guy david bombal might tell u something which suits ur brein`

Now we know the next step would involve `David Bombal`, who is a well-known guy in the infosec community and has a lot of websites and accounts associated with him.

![Figure 4](img/bombal.png) 


The hint in the challenge says `Hint : David is Linked IN with some "Russian Hacks"`, which hints to looking up [his LinkedIn](https://www.linkedin.com/in/davidbombal/), and find something related to `Russian Hacks`.

His LinkedIn looks like the following,

![Figure 5](img/linkedin.png) 

If we look closely, there is indeed a post related to `Russian Hacks`.

![Figure 6](img/russia.png) 

And in the comments, I saw the following comment.

![Figure 7](img/comment.png) 


I went ahead and checked [Atharva Pande's LinkedIn](https://www.linkedin.com/in/atharva-pande-277b58206/),


![Figure 8](img/link.png) 

This person was from `Vishwakarma Institute of Information Technology`, which is a [gold sponsor for VishwaCTF](https://ctftime.org/event/1548) so I assumed the comment this person made was one of the clues to this challenge.

I isolated the cipher-like section of [Atharva Pande's](https://www.linkedin.com/in/atharva-pande-277b58206/) comment, and put it into [brainfk.txt](./files/brainfk.txt)

```
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>++++.++++++++++++..----.+++.<------------.-----------..>++++...<-.>----------.--------.-.+++++.--------.+++++.+++.+++++++++.-------------.<.>--.++++++++++++.--.<+.>-------.+++.+++.-------.<.>++++++++++++.<++++++++.>------.----------.<----.>+++.++++.---.++++++++++++++.-.++++++++.--------------------.++++++++++++++.-----------------.+.<----.>--.+++++++++.--------.+++++.----.<-.>++++++++++++++.-----------------.+++++++++++++++++.<+.>------------.+++.+++.-------.
```



I wasn't exactly sure what type of cipher it was using, so I copied and pasted it into Google to get some hints.

![Figure 9](img/brainf.png) 

So apparently, it was using [Brain F*ck](https://en.wikipedia.org/wiki/Brainfuck), so I went ahead to a [Brain F*ck Decoder](https://www.dcode.fr/brainfuck-language).


![Figure 10](img/braindecode.png) 

Decoding this gave me the following URL,

`https://www.mediafire.com/file/q7ka3dhesrzftcd/bkchd.rar/file`

Accessing this [Media Fire Link](https://www.mediafire.com/file/q7ka3dhesrzftcd/bkchd.rar/file) gave me the following,

![Figure 10](img/rar.png) 

I went ahead and downloaded [bkchd.rar](./files/bkchd.rar), but unfortunately, it was password protected.

![Figure 11](img/password.png) 

I tried to crack this .rar file using John the Ripper. A couple of hours passed, but no password candidate was found. 

At this time, a new hint was added,

![Figure 12](img/hint.png) 

Now I know that the password length is 5 characters, which drastically reduces the brute-forcing time.

So I downloaded rockyou.txt from [here](https://github.com/praetorian-inc/Hob0Rules/blob/master/wordlists/rockyou.txt.gz), unzipped it, and isolated all the 5 character passwords into [rock5.txt](./files/rock5.txt) with,

`$ grep -E '^.{5}$' rockyou.txt > rock5.txt`


So now I just needed to use [rock5.txt](./files/rock5.txt) as the wordlist for John the Ripper. 

I went ahead and made the hash using

`$ sudo rar2john bkchd.rar > rarhash`


And crack with John using [rock5.txt](./files/rock5.txt) as the wordlist,

`$ john --wordlist=rock5.txt rarhash `

After a few minutes, John has found the password, which is 

`idgaf`

![Figure 13](img/john.png) 


I went ahead and opened [bkchd.rar](./files/bkchd.rar) with the password `idgaf`, and inside was the following picture. 


![Figure 14](bkchd.png) 


I checked for steganographic messages using [Steganography Online
](https://stylesuxx.github.io/steganography/), 

![Figure 15](img/steg.png) 

As shown above, some text was contained in this image, which I put into [decodedsteg.txt](./files/decodedsteg.txt). 

```
this  ( guy's pet love dem fries, thats your final pin@ @  @@@   @@ D @ @ @  @@@@ @ @@ @@@     @@  @ @  @ @ @@    @@  @@ @@@@@@@ @ @ @  @  @ @  @ H @  @@ @@ @@@@   @@ @@@ @ @@@@
```

I didn't know what this was supposed to mean and assumed it was saying that this guy's pet, more specifically, the dog is what we're supposed to look for.

So I did a reverse image on Google using [bkchd.png](./files/bkchd.png).

![Figure 16](img/rev.png) 

However, nothing much came up except for other men with tattoos. So I went [Yandex](https://yandex.com/images/) to do a reverse image search.

![Figure 17](img/yandex.png) 


By looking for his distinctive beard and tattoo through the reverse image search results, I noticed that most of them had the name `Polish Viking` on them, so I assumed that was his nickname.
![Figure 18](img/yandex2.png) 

So I looked up `Polish Viking`,


![Figure 19](img/polish.png) 


and found [his Instagram](https://www.instagram.com/pavel_ladziak/) and name, which was `pavel_ladziak`.

![Figure 20](img/pavel.png) 



I went to Google and changed the language settings to Polish to get the most out of the results, and looked up `pavel ladziak dog`, which showed me that his dog was a toy dog with white and beige coloration. 

![Figure 21](img/paveldog.png) 


I dug through his Instagram, and found a [few pictures with his dog](https://www.instagram.com/p/COQt4rkB5oa/),

![Figure 22](img/paveldog2.png) 

However, I could not find the name of his dog. I was thinking to look through his followings list to find his dog, but I assumed that his wife might be more likely to tag their dog in the pictures.


![Figure 23](img/wife.png) 

So I went ahead to [his wife's](https://www.instagram.com/natalia.ziecina/) account.


![Figure 24](img/natalia.png) 


So I dug through her pictures with their dog in it, and came across [this picture](https://www.instagram.com/p/CPbQ_mjrKGI/).


![Figure 25](img/dogwalk.png) 


I saw that she tagged her dog in that picture, which has the Instagram username [iamthemisio](https://www.instagram.com/iamthemisio/)



I went to the dog's account and saw the following,


![Figure 26](img/misio.png) 

The dog's name is `Misio Zdzisio`, and as the challenge was to find a dog and the flag format was `vishwaCTF{Firstname_Lastname}`, the flag for this challenge would be,

 `vishwaCTF{Misio_Zdzisio}`


I cried tears of joy when I inputted this flag and finally got `correct`, because I failed multiple times with flags like `vishwaCTF{David_Bombal}`, `vishwaCTF{Atharva_Pande}` and  `vishwaCTF{Pavel_Ladziak}`. 

![Figure 27](img/correct.png) 

This challenge was an emotional rollercoaster. Every time I thought I got the flag, it turns out it wasn't the flag, but rather only a step in obtaining the flag. Thus, finally getting `correct` was extremely satisfying, especially when you're the first to solve the challenge. I experienced an important life lesson while doing this challenge, which is to keep trying even if you fail because those failures will lead your way to success.

