# Ch 1-3 Practice Problems

published: No

## 🌕 Chapter 1

### R13

**R13.**  Suppose users share a 2 Mbps link. Also suppose each user transmits continuously at 1 Mbps when transmitting, but each user transmits only 20 percent of the time. (See the discussion of statistical multiplexing in Section 1.3.)

1. When circuit switching is used, how many users can be supported?
    
    **2 users can be supported because each user requires half of the link bandwidth.**
    
2. For the remainder of this problem, suppose packet switching is used. Why will there be essentially no queuing delay before the link if two or fewer users transmit at the same time? Why will there be a queuing delay if three users transmit at the same time?
    
    **Since each user requires 1Mbps when transmitting, if two or fewer users transmit simultaneously, a maximum of 2Mbps will be required. Since the available bandwidth of the shared link is 2Mbps, there will be no queuing delay before the link. Whereas, if three users transmit simultaneously, the bandwidth required will be 3Mbps which is more than the available bandwidth of the shared link. In this case, there will be queuing delay before the link.**
    
3. Find the probability that a given user is transmitting.
    
    $$
    \binom{3}{3}p^3(1-p)^{3-3}=(0.2)^3=0.008
    $$
    
    **Since the queue grows when all the users are transmitting, the fraction of time during which the queue grows (which is equal to the probability that all three users are transmitting simultaneously) is 0.008.**
    
4. Suppose now there are three users. Find the probability that at any given time, all three users are transmitting simultaneously. Find the fraction of time during which the queue grows.

### R18

**R18.**  How long does it take a packet of length 1,000 bytes to propagate over a link of distance 2,500 km, propagation speed 2.5 · 108 m/s, and transmission rate 2 Mbps? More generally, how long does it take a packet of length *L* to propagate over a link of distance *d*, propagation speed *s*, and transmission rate *R* bps? Does this delay depend on packet length? Does this delay depend on transmission rate?

**10msec; d/s; no; no**

### R19

**R19.**  Suppose Host A wants to send a large file to Host B. The path from Host A to Host B has three links, of rates *R*1 = 500 kbps, *R*2 = 2 Mbps, and *R*3 = 1 Mbps.

1. Assuming no other traffic in the network, what is the throughput for the file transfer?
    
    **500 kbps**
    
2. Suppose the file is 4million bytes. Dividing the file size by the throughput, roughly how long will it take to transfer the file to Host B?
    
    **64 seconds**
    
3. Repeat (a) and (b), but now with *R*2 reduced to 100 kbps.
    
    **100 kbps; 320 seconds**
    

### R23

**R23.**  What are the five layers in the Internet protocol stack? What are the principal responsibilities of each of these layers?

**The five layers in the Internet protocol stack are – from top to bottom – the application layer, the transport layer, the network layer, the link layer, and the physical layer. The principal responsibilities are outlined in Section 1.5.1.**

### R26

**R26.**  What is the difference between a virus and a worm?

1. **Virus: Requires some form of human interaction to spread. Classic example: E-mail viruses.**
2. **Worms: No user replication needed. Worm in infected host scans IP addresses and port numbers, looking for vulnerable processes to infect.**

### P3

**P3.**  Consider an application that transmits data at a steady rate (for example, the sender generates an *N*-bit unit of data every *k* time units, where *k* is small and fixed). Also, when such an application starts, it will continue running for a relatively long period of time. Answer the following questions, briefly justifying your answer:

1. Would a packet-switched network or a circuit-switched network be more appropriate for this application? Why?
    
    **A circuit-switched network would be well suited to the application, because the application involves long sessions with predictable smooth bandwidth requirements. Since the transmission rate is known and not bursty, bandwidth can be reserved for each application session without significant waste. In addition, the overhead costs of setting up and tearing down connections are amortized over the lengthy duration of a typical application session.**
    
2. Suppose that a packet-switched network is used and the only traffic in this network comes from such applications as described above. Further- more, assume that the sum of the application data rates is less than the capacities of each and every link. Is some form of congestion control needed? Why?
    
    **In the worst case, all the applications simultaneously transmit over one or more network links. However, since each link has sufficient bandwidth to handle the sum of all of the applications' data rates, no congestion (very little queuing) will occur. Given such generous link capacities, the network does not need congestion control mechanisms.**
    

### P8

**P8.**  Suppose users share a 3 Mbps link. Also suppose each user requires 150 kbps when transmitting, but each user transmits only 10 percent of the time. (See the discussion of packet switching versus circuit switching in Section 1.3 or the slides.)

1. When circuit switching is used, how many users can be supported?
    
    **20 users can be supported**
    
2. For the remainder of this problem, suppose packet switching is used. Find the probability that a given user is transmitting.
    
    **p = 0.1**
    
3. Suppose there are 120 users. Find the probability that at any given time, exactly *n* users are transmitting simultaneously. (*Hint*: Use the binomial distribution.)
    
    $$
    \binom{120}{n}p^n(1-p)^{120-n}
    $$
    

### P29

**P29.** Suppose there is a 10Mbps microwave link between a geostationary satellite and its base station on Earth. Every minute the satellite takes a digital photo and sends it to the base station. Assume a propagation speed of 2.4*108 meters/sec.

1. What is the propagation delay of the link?
    
    **150 msec**
    
2. Let *x* denote the size of the photo. What is the minimum value of *x* for the microwave link to be continuously transmitting?
    
    **600,000,000 bits**
    

### E1

**E1.** Circuit switching versus packet switching

i. In a circuit switching network, when Alice wants to communicate with Bob, a physical "circuit" is established between Alice and Bob before any data can be sent.

1. Why do you think this is necessary?
    
    **This is necessary because in a circuit switching network, resources must be reserved beforehand**
    along the path that will be used to carry data between Bob and Alice.
    
2. What is(are) the advantage(s)?
    
    **Circuit switched networks provide predictable performance/quality of service.**
    
3. What is(are) the disadvantage(s)?
    
    **Circuit switched networks do not always make best use of available resource (i.e. resources may be under-utilized when calls are idle)**
    

ii. In a packet switching network, when Alice wants to communicate with Bob, no circuit is established and Alice simply starts sending data to Bob.

1. What is(are) the advantage(s)?
    
    **This fully utilizes the bandwidth available along the path between Alice and Bob. It is also more resilient to faults (e.g. if a link is severed, packets can take alternate paths)**
    
2. What is(are) the disadvantage(s)?
    
    **Packet switched networks are "best effort" and on demand--no guarantee about reliability or performance. Unpredictable.**
    

## 🌕 Chapter 2

### **Practice Problem 1)**

**Practice Problem 1)** (Computer Networking: A Top-Down Approach 6th Edition: Chapter 2 P1)

True or false?

1. A user requests a Web page that consists of some text and three images. For this page, the client will send one request message and receive four response messages. **F**
2. Two distinct Web pages (for example, www.mit.edu/research.html and www.mit.edu/students.html) can be sent over the same persistent connection. **T**
3. With nonpersistent connections between browser and origin server, it is possible for a single TCP segment to carry two distinct HTTP request messages. **F**

### **Practice Problem 2**

**Practice Problem 2)** (Computer Networking: A Top-Down Approach 6th Edition: Chapter 2 P3)

Consider an HTTP client that wants to retrieve a Web document at a given URL. The IP address of the HTTP server is initially unknown. What transport and application-layer protocols besides HTTP are needed in this scenario?

**Application layer protocols: DNS and HTTP
Transport layer protocols: UDP for DNS; TCP for HTTP**

### **Practice Problem 3**

**Practice Problem 3)** (Computer Networking: A Top-Down Approach 6th Edition: Chapter 2 P7)

Suppose within your Web browser you click on a link to obtain a Web page. The IP address for the associated URL is not cached in your local host, so a DNS lookup is necessary to obtain the IP address. Suppose that n DNS servers are visited before your host receives the IP address from DNS; the successive visits incur an RTT of RTT 1, . . ., RTTn. Further suppose that the Web page associated with the link contains exactly one object, consisting of a small amount of HTML text. Let RTT0 denote the RTT between the local host and the server containing the object. Assuming zero transmission time of the object, how much time elapses from when the client clicks on the link until the client receives the object?

**The total amount of time to get the IP address is**

**RTT1 + RTT2 + … + RTTn**

**Once the IP address is known, RTTo elapses to set up the TCP connection and another RTTo elapses to request and receive the small object. The total response time is**

**2RTTo + RTT1 + RTT2 + … + RTTn**

### **Practice Problem 4**

**Practice Problem 4)** (Computer Networking: A Top-Down Approach 6th Edition: Chapter 2 P8)

Referring to the previous question, suppose the HTML file references eight very small objects on the same server. Neglecting transmission times, how much time elapses with:

1. Non-persistent HTTP with no parallel TCP connections?
    
    **RTT1 + … + RTTn + 2RTTo + 8 * 2RTTo = 18RTTo + RTT1 + … + RTTn**
    
2. Non-persistent HTTP with the browser configured for 5 parallel connections?
    
    **RTT1 + … + RTTn + 2RTTo + 2 * 2RTTo = 6RTTo + RTT1 + … + RTTn**
    
3. Persistent HTTP?
    
    **RTT1 + … + RTTn + 2RTTo + RTTo = 3RTTo + RTT1 + … + RTTn**
    

### **Practice Problem 5**

**Practice Problem 5)** (Computer Networking: A Top-Down Approach 6th Edition: Chapter 2 P19)

**P19.** In this problem, we use the useful dig tool available on Unix and Linux hosts to explore the hierarchy of DNS servers. Recall that in Figure 2.21, a DNS server higher in the DNS hierarchy delegates a DNS query to a DNS server lower in the hierarchy, by sending back to the DNS client the name of that lower-level DNS server. First read the man page for dig, and then answer the following questions.

1. Starting with a root DNS server (from one of the root servers [a-m].rootservers.net), initiate a sequence of queries for the IP address for your department’s Web server by using dig. Show the list of the names of DNS servers in the delegation chain in answering your query.
    
    **dig +norecurse @a.root-servers.net any [soe.ucsc.edu](http://soe.ucsc.edu/)**
    
    ![Untitled](Ch%201-3%20Practice%20Problems%20383e219b16e247c1b2758bb7608c5ade/Untitled.png)
    
    **dig +norecurse @f.edu-servers.net any [soe.ucsc.edu](http://soe.ucsc.edu/)**
    
    ![Untitled](Ch%201-3%20Practice%20Problems%20383e219b16e247c1b2758bb7608c5ade/Untitled%201.png)
    
    **dig +norecurse @ns.zocalo.net any [soe.ucsc.edu](http://soe.ucsc.edu/)**
    
    ![Untitled](Ch%201-3%20Practice%20Problems%20383e219b16e247c1b2758bb7608c5ade/Untitled%202.png)
    
    **dig +norecurse @adns1.ucsc.edu any [soe.ucsc.edu](http://soe.ucsc.edu/)**
    
    ![Untitled](Ch%201-3%20Practice%20Problems%20383e219b16e247c1b2758bb7608c5ade/Untitled%203.png)
    
    **The answer for [google.com](http://google.com/) could be similar as above, using the nameservers:**
    
    [**a.root-servers.net](http://a.root-servers.net/)
    [E.GTLD-SERVERS.NET](http://e.gtld-servers.net/)
    [ns1.google.com](http://ns1.google.com/)**
    

### **Practice Problem 6**

**Practice Problem 6)** (Computer Networking: A Top-Down Approach 6th Edition: Chapter 2 P20)

Suppose you can access the caches in the local DNS servers of your department. Can you propose a way to roughly determine the Web servers (outside your department) that are most popular among the users in your department? Explain.
**We can periodically take a snapshot of the DNS caches in the local DNS servers. The Web server that appears most frequently in the DNS caches is the most popular server. This is because if more users are interested in a Web server, then DNS requests for that server are more frequently sent by users. Thus, that Web server will appear in the DNS caches more frequently.**

### **Practice Problem 7**

**Practice Problem 7)** (Computer Networking: A Top-Down Approach 6th Edition: Chapter 2 P21)

Suppose that your department has a local DNS server for all computers in the department. You are an ordinary user (i.e., not a network/system administrator). Can you determine if an external Web site was likely accessed from a computer in your department a couple of seconds ago? Explain.

**Yes, we can use dig to query that Web site in the local DNS server. For example, “dig [cnn.com](http://cnn.com/)” will return the query time for finding [cnn.com](http://cnn.com/). If [cnn.com](http://cnn.com/) was just accessed a couple of seconds ago, an entry for [cnn.com](http://cnn.com/) is cached in the local DNS cache, so the query time is 0 msec. Otherwise, the query time is large**

### **Practice Problem 8**

**Practice Problem 8)** (Computer Networking: A Top-Down Approach 6th Edition: Chapter 2 P22)

Consider distributing a file of F = 15 Gbits to N peers. The server has an upload rate of u_s = 30 Mbps, and each peer has a download rate of d_i = 2 Mbps and an upload rate of u. For N = 10, 100, and 1,000 and u = 300 Kbps, 700 Kbps, and 2 Mbps, prepare a chart giving the minimum distribution time for each of the combinations of N and u for both client-server distribution and P2P distribution.

**Client Server:**

|  | 10 | 100 | 1000 |
| --- | --- | --- | --- |
| 300 Kbps | 7680 | 51200 | 512000 |
| 700 Kbps | 7680 | 51200 | 512000 |
| 2 Mbps | 7680 | 51200 | 512000 |

**Peer to Peer:**

|  | 10 | 100 | 1000 |
| --- | --- | --- | --- |
| 300 Kbps | 7680 | 25904 | 47559 |
| 700 Kbps | 7680 | 15616 | 21525 |
| 2 Mbps | 7680 | 7680 | 7680 |

### **Practice Problem 9**

**Practice Problem 9)** (Computer Networking: A Top-Down Approach 6th Edition: Chapter 2 P33)

Can you configure your browser to open multiple simultaneous connections to a Web site? What are the advantages and disadvantages of having a large number of simultaneous TCP connections?

**Yes, you can configure many browsers to open multiple simultaneous connections to a Web site. The advantage is that you will you potentially download the file faster. The disadvantage is that you may be hogging the bandwidth, thereby significantly slowing down the downloads of other users who are sharing the same physical links.**

## 🌕 Chapter 3

### **Practice Problem 1**

**Practice Problem 1)** (Computer Networking: A Top-Down Approach 6th Edition: Chapter 3 P1)

Suppose Client A initiates a Telnet session with Server S. At about the same time, Client B also initiates a Telnet session with Server S. Provide possible source and destination port numbers for:

1. The segments sent from A to S. **Source: any Destination: 23**
2. The segments sent from B to S. **Source: any Destination: 23**
3. The segments sent from S to A. **Source: 23 Destination: answer from a**
4. The segments sent from S to B. **Source: 23 Destination: answer from b**
5. If A and B are different hosts, is it possible that the source port number in the segments from A to S is the same as that from B to S? ********Yes********
6. How about if they are the same host? **No**

### **Practice Problem 2**

**Practice Problem 2)** (Computer Networking: A Top-Down Approach 6th Edition: Chapter 3 P3)

UDP and TCP use 1s complement for their checksums. Suppose you have the following three 8-bit bytes: 01010011, 01100110, 01110100. What is the 1s complement of the sum of these 8-bit bytes? (Note that although UDP and TCP use 16-bit words in computing the checksum, for this problem you are being asked to consider 8-bit sums.) Show all work. Why is it that UDP takes the 1s complement of the sum; that is, why not just use the sum? With the 1s complement scheme, how does the receiver detect errors? Is it possible that a 1-bit error will go undetected? How about a 2-bit error?

**Note: Wrap around if overflow.**

**01010011 + 01100110 = 10111001
10111001 + 01110100 = 00101110**

```bash
01010011 + 
01100110 = 
10111001

10111001 + 
01110100 = 
00101110

11010001 # One's complement
```

**One's complement = 1 1 0 1 0 0 0 1.**

**To detect errors, the receiver adds the four words (the three original words and the checksum). If the sum contains a zero, the receiver knows there has been an error. All one-bit errors will be detected, but two-bit errors can be undetected (e.g., if the last digit of the first word is converted to a 0 and the last digit of the second word is converted to a 1).**

### **Practice Problem 3**

**Practice Problem 3)** (Computer Networking: A Top-Down Approach 6th Edition: Chapter 3 P5)

Suppose that the UDP receiver computes the Internet checksum for the received UDP segment and finds that it matches the value carried in the checksum field. Can the receiver be absolutely certain that no bit errors have occurred? Explain.

**No, the receiver cannot be absolutely certain that no bit errors have occurred. This is because of the manner in which the checksum for the packet is calculated. If the corresponding bits (that would be added together) of two 16-bit words in the packet were 0 and 1 then even if these get flipped to 1 and 0 respectively, the sum still remains the same. Hence, the 1s complement the receiver calculates will also be the same. This means the checksum will verify even if there was transmission error.**

### **Practice Problem 4**

**Practice Problem 4)** (Computer Networking: A Top-Down Approach 6th Edition: Chapter 3 P14)

Consider a reliable data transfer protocol that uses only negative acknowledgments. Suppose the sender sends data only infrequently. Would a NAK-only protocol be preferable to a protocol that uses ACKs? Why? Now suppose the sender has a lot of data to send and the end-to-end connection experiences few losses. In this second case, would a NAK-only protocol be preferable to a protocol that uses ACKs? Why?

**In a NAK only protocol, the loss of packet x is only detected by the receiver when packet x+1 is received. That is, the receivers receives x-1 and then x+1, only when x+1 is received does the receiver realize that x was missed. If there is a long delay between the transmission of x and the transmission of x+1, then it will be a long time until x can be recovered, under a NAK only protocol.**

**On the other hand, if data is being sent often, then recovery under a NAK-only scheme could happen quickly. Moreover, if errors are infrequent, then NAKs are only occasionally sent (when needed), and ACK are never sent – a significant reduction in feedback in the NAK-only case over the ACK-only case.**

### **Practice Problem 5**

**Practice Problem 5)** (Computer Networking: A Top-Down Approach 6th Edition: Chapter 3 P19)

Consider a scenario in which Host A wants to simultaneously send packets to Hosts B and C. A is connected to B and C via a broadcast channel—a packet sent by A is carried by the channel to both B and C. Suppose that the broadcast channel connecting A, B, and C can independently lose and corrupt packets (and so, for example, a packet sent from A might be correctly received by B, but not by C). Design a stop-and-wait-like error-control protocol for reliably transferring packets from A to B and C, such that A will not get new data from the upper layer until it knows that both B and C have correctly received the current packet. Give FSM descriptions of A and C. (Hint: The FSM for B should be essentially the same as for C.) Also, give a description of the packet format(s) used.

**This problem is a variation on the simple stop and wait protocol (rdt3.0).  Because the channel may lose messages and because the sender may resend a message that one of the receivers has already received (either because of a premature timeout or because the other receiver has yet to receive the data correctly), sequence numbers are needed.  As in rdt3.0, a 0-bit sequence number will suffice here.**

**The sender and receiver FSM are shown in Figure 3.  In this problem, the sender state indicates whether the sender has received an ACK from B (only), from C (only) or from neither C nor B. The receiver state indicates which sequence number the receiver is waiting for.**

![Untitled](Ch%201-3%20Practice%20Problems%20383e219b16e247c1b2758bb7608c5ade/Untitled%204.png)

**Figure 3. Sender and receiver for Problem 3.19 (Problem 19) (From Computer Networking: A Top-Down Approach 6th Edition Solutions Manual)**

### **Practice Problem 6**

**Practice Problem 6)** (Computer Networking: A Top-Down Approach 6th Edition: Chapter 3 P22)

Consider the GBN protocol with a sender window size of 4 and a sequence number range of 1,024. Suppose that at time t, the next in-order packet that the receiver is expecting has a sequence number of k. Assume that the medium does not reorder messages. Answer the following questions:

1. What are the possible sets of sequence numbers inside the sender’s window at time t? Justify your answer.
    
    **Here we have a window size of N=3. Suppose the receiver has received packet k-1, and has ACKed that and all other preceding packets. If all of these ACK's have been received by sender, then sender's window is [k, k+N-1]. Suppose next that none of the ACKs have been received at the sender. In this second case, the sender's window contains k-1 and the N packets up to and including k-1. The sender's window is thus [k-N,k-1]. By these arguments, the senders window is of size 3 and begins somewhere in the range [k-N,k].**
    
2. What are all possible values of the ACK field in all possible messages currently propagating back to the sender at time t? Justify your answer.
    
    **If the receiver is waiting for packet k, then it has received (and ACKed) packet k-1 and the N-1 packets before that. If none of those N ACKs have been yet received by the sender, then ACK messages with values of [k-N,k-1] may still be propagating back.Because the sender has sent packets [k-N, k-1], it must be the case that the sender has already received an ACK for k-N-1. Once the receiver has sent an ACK for k-N-1 it will never send an ACK that is less that k-N-1. Thus the range of inflight ACK values can range from k-N-1 to k-1.**
    

### **Practice Problem 7**

**Practice Problem 7)** (Computer Networking: A Top-Down Approach 6th Edition: Chapter 3 P25)

We have said that an application may choose UDP for a transport protocol because UDP offers finer application control (than TCP) of what data is sent in a segment and when.

1. Why does an application have more control of what data is sent in a segment?
    
    **Consider sending an application message over a transport protocol. With TCP, the application writes data to the connection send buffer and TCP will grab bytes without necessarily putting a single message in the TCP segment; TCP may put more or less than a single message in a segment. UDP, on the other hand, encapsulates in a segment whatever the application gives it; so that, if the application gives UDP an application message, this message will be the payload of the UDP segment. Thus, with UDP, an application has more control of what data is sent in a segment.**
    
2. Why does an application have more control on when the segment is sent?
    
    **With TCP, due to flow control and congestion control, there may be significant delay from the time when an application writes data to its send buffer until when the data is given to the network layer. UDP does not have delays due to flow control and congestion control.**
    

### **Practice Problem 8**

**Practice Problem 8)** (Computer Networking: A Top-Down Approach 6th Edition: Chapter 3 P28)

Host A and B are directly connected with a 100 Mbps link. There is one TCP connection between the two hosts, and Host A is sending to Host B an enormous file over this connection. Host A can send its application data into its TCP socket at a rate as high as 120 Mbps but Host B can read out of its TCP receive buffer at a maximum rate of 50 Mbps. Describe the effect of TCP flow control.

**Since the link capacity is only 100 Mbps, so host A’s sending rate can be at most 100Mbps. Still, host A sends data into the receive buffer faster than Host B can remove data from the buffer. The receive buffer fills up at a rate of roughly 40Mbps. When the buffer is full, Host B signals to Host A to stop sending data by setting RcvWindow = 0. Host A then stops sending until it receives a TCP segment with RcvWindow > 0. Host A will thus repeatedly stop and start sending as a function of the RcvWindow values it receives from Host B. On average, the long-term rate at which Host A sends data to Host B as part of this connection is no more than 60Mbps.**