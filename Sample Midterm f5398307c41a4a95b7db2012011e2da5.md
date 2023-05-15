# Sample Midterm

published: No

### Files

Sample midterm: [https://nbviewer.org/github/bunfloof/CSE150-UCSC/blob/main/Downloads/Midterm_sample_W17.pdf](https://nbviewer.org/github/bunfloof/CSE150-UCSC/blob/main/Downloads/Midterm_sample_W17.pdf)

Chapter 1-3 slides: [https://nbviewer.org/github/bunfloof/CSE150-UCSC/blob/main/CSE150 Chap1-3 OCR Orientation-fixed.pdf](https://nbviewer.org/github/bunfloof/CSE150-UCSC/blob/main/CSE150%20Chap1-3%20OCR%20Orientation-fixed.pdf) 

### Tutor Response

Hello,

I hope you are doing well! I just wanted to follow up with you about the review session I held yesterday. Please take note of the following:

1. For **Problem 2 on the Practice Midterm,** please disregard what I mentioned about that question asking for the total delay; it strictly asks about the **propagation delay** (just like the textbook practice problem). The phrasing is not the clearest; however, the term **"propagate over a link"** **in this context** refers to the **propagation delay**, which is **(2,500 km * 1000m)/ (2.5 * 10^8) m/s  = 0.01 seconds = 10 msec.**

2. For **Problem 4 on the Practice Midterm**, the approach to solving this question can be found at the **bottom of Chapter 2 Slides, slide 27**. The answer is **2*Tr + Tf.** The logic for this question comes from how RTT and the file transfer time are defined. In this class, **RTT** is defined as the **time** for a **small packet** to travel **from the client to the server and back**. A **small packet** is one that **does not** carry a **large payload**, such as TCP SYN, TCP SYN-ACK, TCP ACK, or HTTP GET request (HTTP POST request would not be a small packet because it can carry a large payload). Furthermore, in this class, the **file transfer time** is analogous to **the transmission delay**; in other words, it is **how long** it takes for the current router or host **to push out** the **whole file onto the link**. That is why the time to transmit the file is so short in the graphic below (from slide 27 of chapter 2 slides).
![Untitled](Sample%20Midterm%20f5398307c41a4a95b7db2012011e2da5/Untitled.png)
[https://mail.google.com/mail/u/0?ui=2&ik=156cbe3961&attid=0.0.1&permmsgid=msg-f:1765456691370154994&th=18802981cb745bf2&view=fimg&fur=ip&sz=s0-l75-ft&attbid=ANGjdJ8lgaeTmcL-Fq43AhGl1O2Y4I5Ygx3782atkHrmOSTMbiQPnos3BUfdE64bDaGsl1RxQPZ_Suy3MN5hFqSlQSuO6VK6p2ZGV8C1mcgz5YbDtE1w_0KKc8LSQFU&disp=emb&realattid=ii_lhgte4wl0](https://mail.google.com/mail/u/0?ui=2&ik=156cbe3961&attid=0.0.1&permmsgid=msg-f:1765456691370154994&th=18802981cb745bf2&view=fimg&fur=ip&sz=s0-l75-ft&attbid=ANGjdJ8lgaeTmcL-Fq43AhGl1O2Y4I5Ygx3782atkHrmOSTMbiQPnos3BUfdE64bDaGsl1RxQPZ_Suy3MN5hFqSlQSuO6VK6p2ZGV8C1mcgz5YbDtE1w_0KKc8LSQFU&disp=emb&realattid=ii_lhgte4wl0)

3. I've attached to this email **another practice midterm** with a different set of questions (ignore the yellow sticky note things on question 6). I **highly encourage** all of you to practice these questions, too, **especially question 9**. Question 9 tests your knowledge of **DNS, different types of HTTP connections, and caching**. There will likely be a question on **your midterm** that touches on all these concepts.

Please get in touch with me if you have any questions or come to my other review sessions. Also, if you have any feedback about how I can more effectively use the time during these review sessions to help you learn better, please let me know!

Thanks, and good luck with your midterms!

Best Regards,
Yesh Chandiramani
He/Him/His
University of California, Santa Cruz - Class of 2024
Computer Science Major

### **Problem 1**

(a) Name the five layers of the Internet protocol stack.

- application
    - FTP, SMTP, HTTP
- transport
    - TCP, UDP
- network
    - IP, routing protocols
- link
    - ethernet, 802.11
- physical

(b)  List two types of access networks.

- enterprise access networks (ethernet)
- wireless

(c) Associate each of the following concept with either packet switching (PS) or circuit switching (CS):

Store and forward ---  **Packet switching (PS)**

Dedicated resource allocation --- **Circuit switching (CS)**

Queuing --- **Packet switching (PS)**

(d)  Consider a video streaming server with an upload capacity of 200 Mbps and a download capacity of 100 Mbps.  It is serving 50 clients simultaneously by *fairly* multiplexing its upload capacity. Each of the clients streaming from the server has an upload capacity of 2 Mbps and a download capacity of 5 Mbps.  The Internet is not congested.  What is the maximum bit rate at which this client is receiving service?

Maximum server’s egress (upload) capacity = 200 Mbps / 50 clients = **4 Mbps**

### **Problem 2**

(a) How long does it take a packet of length 1,000 bytes to propagate over a link of distance 2,500 km, propagation speed 2.5 · 10^8 m/s, and transmission rate 2 Mbps?

Recall delay equation: 

$$
d_{nodal} = d_{processing} + d_{queue} + d_{transmission} + d_{propogation}
\\d_{nodal} =
\cancel{d_{processing}} + \cancel{d_{queue}} + d_{transmission} + d_{propogation}
$$

Recall unit conversions:

1 kilometer  = 1000 meter

1 megabit = 1000000 bits = 1 * 10^6 bits

8 megabits = 1 megabyte

**Transmission delay:**

Solving using dimensional analysis,

$$
\begin{align*}1000\, bytes \times \frac{8\,bits}{1\,byte}\times \frac{1\,second}{2\cdot10^6\ bits} &=\\1000\, \cancel{bytes} \times \frac{8\,\cancel{bits}}{1\,\cancel{byte}}\times \frac{1\,second}{2\cdot10^6\ \cancel{bits}} &= 0.004\, seconds\end{align*}
$$

**********Propagation delay:**********

Recall speed formula,

$$
\begin{align*}speed&=\frac{distance}{time}\\ speed&=2500 \,km\times\frac{1 000\,m}{1\,km}\times\frac{1\,second}{{2.5\cdot10^8\,m}}\\ speed&=\boxed{0.01 \, seconds}\end{align*}
$$

**~~Total delay:~~**

$$
\begin{aligned}d_{nodal}&=d_{trans}+d_{prop}\\ d_{nodal}&=0.004\,s+0.01\,s=0.014\,s\times\frac{1000\,ms}{1\,s}=14\,ms\end{aligned}
$$

However, the problem is referring to propagation delay, thus the answer is **0.01 seconds** or **1 ms**.

(b) More generally, how long does it take a packet of length L to propagate over a link of distance d, propagation speed s, and transmission rate R bps?

$$
\begin{aligned}D_{nodal}&= d_{propogation}\\ &=\frac{d_{distance}}{s_{speed}}\end{aligned}
$$

### **Problem 3**

(a) In class, we discussed different ways loss can occur as data is transferred over the network. List and provide a brief explanation of the two types of data loss we discussed.

1. Packet lost from routers, buffer being full: When a router's buffer is full, it cannot store any more packets. In this case, any incoming packets will be dropped or lost.

2. Packet loss from bit errors: Bit errors can occur during transmission due to noise or interference in the communication channel. These errors can cause some bits in the packet to be corrupted or lost, resulting in packet loss.

(b) What is the difference between virus and worm? When a malware is included in an Email attachment, is it a virus or worm?

A virus is a self-replicating infection by receiving/executing object, while a worm is a self-replicating infection by passively receiving an object that gets itself executed. When malware is included in an email attachment, it is typically a virus.

**Problem 4**

(a) Let the round trip time be Tr and file transfer time be Tf, what is the time to use non-persistent HTTP to get a file?

**non-persistent HTTP response time = 2RTT + file transmission time**, where RTT is the round trip time and file transmission time is Tf.

(b) Consider an institution with a 1.5 Mbps incoming channel from the Internet.  The average http request rate from all browsers in the institution is 30/second.  Each request is for a single object with an average size of 7,000 bytes.  Will the incoming channel congested by the http traffic?

Yes, the incoming channel will be congested by the HTTP traffic.

First, calculate the average data rate of HTTP requests from all browsers in the institution.

$$
\begin{aligned}\frac{30\,requests}{second}\times\frac{7000\,bytes}{request}&=\\
\frac{30\,\cancel{requests}}{second}\times\frac{7000\,bytes}{\cancel{request}}&=210000\,bytes/second\end{aligned}
$$

Converting bytes to bits, we get:

$$
\begin{aligned}\frac{210000\,bytes}{second}\times\frac{8\,bits}{byte}&=
\\frac{210000\,\cancel{bytes}}{second}\times\frac{8\,bits}{\cancel{byte}}&=1680000\,bits/second\end{aligned}
$$

Since the incoming channel from the Internet is only 1.5 Mbps (1,500,000 bits/second), the HTTP traffic of 1.68 Mbps (1,680,000 bits/second) will congest the channel.

### **Problem 5**

(a) In BitTorrent, a peer sends chunks “tit-for-tat” to four neighbors currently sending chunks to it at the highest rates.  And every 30 seconds it “optimistically unchokes” a randomly selected peer, i.e., sends chunks to it.  Why is it *necessary* for the system to have chunks sent to randomly selected peer.

It is necessary for the BitTorrent system to have chunks sent to randomly selected peers because it allows for new peers to join the network and receive chunks, even if they are not currently one of the top four neighbors sending chunks to the peer. This helps to ensure that the file distribution is more efficient and that all peers have a chance to receive chunks, even if they are not currently one of the top contributors.

(b) Compare DNS recursive query and iterative query.

- DNS recursive query puts the burden of name resolution on the contacted name server, while iterative query returns the name of the server to contact.
- In a recursive query, the contacted server replies with the name of the server to contact, while in an iterative query, the contacted server replies with the best effort name-to-address translation.

### **Problem 6**

(a) List the advantages and disadvantages by comparing client-server to peer-to-peer.

Advantages of client-server architecture:

- Clients can rely on the server to be always available and provide a consistent service.
- The server can handle a large number of clients simultaneously.
- The server can provide a centralized point of control and management.

Disadvantages of client-server architecture:

- The server can become a bottleneck if it is overloaded with requests.
- The server can be a single point of failure, causing the entire system to fail if it goes down.
- The server can be expensive to maintain and scale.

Advantages of peer-to-peer architecture:

- Peers can share resources and provide services to each other, reducing the load on any single peer.
- Peers can be added or removed from the network dynamically, allowing for self-scalability.
- Peers can operate independently, making the system more resilient to failures.

Disadvantages of peer-to-peer architecture:

- Peers can be unreliable, making it difficult to manage the system.
- Peers can be intermittently connected and change IP addresses, making it difficult to locate and communicate with them.
- Peers may have limited resources, such as bandwidth or storage, which can affect the overall performance of the system.

(b)  Compute the Internet checksum of the following 16-bit integers, using the following steps

1 1 0 1 0 1 1 1 0 1 0 1 0 0 1 1

1 1 0 0 1 0 0 1 0 1 0 1 0 1 1 1

1. *add*
    
       1 1 0 1 0 1 1 1 0 1 0 1 0 0 1 1
       1 1 0 0 1 0 0 1 0 1 0 1 0 1 1 1
    1 1 0 1 0 0 0 0 0 1 0 1 0 1 0 1 0
    
2. *one’s complement sum*
    
    Add one bit:
    
    1 1 0 1 0 0 0 0 0 1 0 1 0 1 0 1 1
    
    Invert:
    0 0 1 0 1 1 1 1 1 0 1 0 1 0 1 0 0
    
3. *Internet check sum*
    
          1 0 1 1 1 1 1 0 1 0 1 0 1 0 0
    

### **Problem 7**

(a) Given $T_A$ = 0, $T_P$ = 0 and P = 0, the maximum utilization formula for the sliding window protocol is 

$$
\begin{cases}
   U=1 &\text{for }WT_F > T_F+2\tau \\
   U=WT_F /(T_F+2\tau) &\text{otherwise}
\end{cases}
$$

where $T_F$ denotes the transmission time of a frame, *W* the send window size, and $\tau$ the one-way propagation time. Suppose the link transmission rate is 10 megabits/second, frame size = 10,000 bits, and $\tau$ = ****10 msec. **** We would like to choose *W* such that *U* is at least 0.8.  Determine *W*.  Show your derivation steps.

$$
\begin{aligned}T_F&=\frac{frame\space size}{transmission\space rate}\\T_F&=\frac{10000\,bits}{10000000\,bits/second}=0.001\,sec
\end{aligned}
$$

Substitute given values U = 0.8 and τ = 10 ms into provided formula:

$$
\begin{aligned}U &= WT_F / (T_F + 2\tau )\\0.8 &= W * 0.001 / (0.001 + 2*0.01)\\W &= 0.8 * (0.001 + 2*0.01) / 0.001\\ W&= 16.8 = 17\,ms \end{aligned}
$$

Rounding from 16.8 to 17 because window size W should be an integer. Substitute values W = 17 ms, $T_F$ = 0.001 sec, and $\tau$ = ****10 ms into given case.

$$
\begin{aligned}WT_F &> T_F+2\tau\\
17 * 0.001 &> 0.001 + 2*0.01 \\0.017 &\cancel{>}  0.021\end{aligned}
$$

Since 0.017 <= 0.021, the condition for U = 1 doesn't hold. So, the maximum utilization with W = 17 is indeed less than 1, and the calculated U should be valid.

### **Problem 8**

(a) In design of the reliable data transfer protocol, what mechanism is used to handle the case that the receiver may receive a segment with errors?

The mechanism used to handle the case that the receiver may receive a segment with errors in the reliable data transfer protocol is negative acknowledgements (NAKs). The receiver explicitly tells the sender that the packet had errors, and the sender retransmits the packet on receipt of NAK.

(b) Compare go-back-N and selective repeat. list their advantages and disadvantages.

Advantages of Go-Back-N:

- Simple to implement
- Receiver only sends cumulative ACKs, reducing the number of packets sent
- Can handle lost packets well

Disadvantages of Go-Back-N:

- Can result in unnecessary retransmissions of packets
- Limited by the size of the sender's window
- Can cause head-of-line blocking if a packet is lost

Advantages of Selective Repeat:

- Can handle out-of-order packets well
- Can handle lost packets well
- Can make better use of available bandwidth

Disadvantages of Selective Repeat:

- More complex to implement than Go-Back-N
- Receiver sends individual ACKs, increasing the number of packets sent
- Requires more buffer space at the receiver to store out-of-order packets.

### **Problem 9**

Host A and B are directly connected with a 100 Mbps link. There is one TCP connection between the two hosts, and Host A is sending to Host B an enormous file over this connection. Host A can send its application data into its TCP socket at a rate as high as 120 Mbps but Host B can read out of its TCP receive buffer at a maximum rate of 50 Mbps. Describe the effect of TCP flow control.

The effect of TCP flow control in this scenario is that Host B's TCP receive buffer will fill up quickly, causing it to send a smaller receive window to Host A. This will cause Host A to slow down its sending rate to match the receive rate of Host B, resulting in a reduced throughput of the TCP connection.