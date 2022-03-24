# Rocket Raccoon (Category: OSINT)
The challenge is the following,

![Figure 1](img/challenge.png) 

We are given the username `racckoonn`, so I started by looking up this name on [InstantUsername](https://instantusername.com/),


![Figure 1](img/user.png) 


I went ahead and started with [racckoonn's Instagram](https://www.instagram.com/racckoonn/)


![Figure 1](img/rack.png) 


I looked through their pictures, and found [this image](https://www.instagram.com/p/CbEzNo1PQ-g/).


![Figure 1](img/pic.png) 


So I went to the `https://www.youtube.com/channel/UCDurVPcUypifNkJVrHxJ3vQ`,


![Figure 1](img/youtube.png) 

However, there are no videos. So I assumed that I will have to use the username `JohnsonM3llisa` for further investigation. I went to [InstantUsername](https://instantusername.com/) again, and looked that username up.


![Figure 1](img/user2.png) 


I went ahead and started with [JohnsonM3llisa's Twitter](https://twitter.com/JohnsonM3llisa).



![Figure 1](img/twitter.png) 


[This tweet](https://twitter.com/JohnsonM3llisa/status/1503690182432030720) caught my eye, and I immediately assumed that I was supposed to use the [Wayback Machine](https://archive.org/web/) to look at the deleted Tweets.


So I went ahead and [searched their Twitter account on the Wayback Machine](https://web.archive.org/web/*/https://twitter.com/JohnsonM3llisa), and saw that there were snapshots on March 15, 2022.


![Figure 1](img/wayback.png) 


I opened up [the snapshot on March 15, 2022](https://web.archive.org/web/20220315110835/https://twitter.com/JohnsonM3llisa), and saw the following,


![Figure 1](img/flag.png) 



Therefore, the flag is,

`Vishwactf{R4cc00ns_4r3_Sm4rt}`

