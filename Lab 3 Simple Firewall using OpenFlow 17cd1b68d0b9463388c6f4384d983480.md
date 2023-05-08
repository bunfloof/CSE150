# Lab 3: Simple Firewall using OpenFlow

published: No

1. The output of `pingall` shows that all of the pings failed, which is the expected behavior, since ICMP traffic should be blocked by the firewall. All pings show "X" as a result, meaning 100% of packets were dropped. Below is a screenshot of my output:

![Untitled.png](Lab%203%20Simple%20Firewall%20using%20OpenFlow%2017cd1b68d0b9463388c6f4384d983480/Untitled.png)

2. After I generated some TCP traffic using `iperf`, I immediately ran `dpctl dump-flows` to show the active flow entries installed in the switch before they expire due to the idle_timeout or hard_timeout specified in my of_flow_mod (idle_timeout = 10, hard_timeout = 30). Below is a screenshot of my output:

![Untitled 1.png](Lab%203%20Simple%20Firewall%20using%20OpenFlow%2017cd1b68d0b9463388c6f4384d983480/Untitled_1.png)

3. The `iperf` test between h1 and h4 was successful, with high bandwidth rates, which indicates that my firewall is allowing TCP traffic. Below is a screenshot of my output:

![Untitled](Lab%203%20Simple%20Firewall%20using%20OpenFlow%2017cd1b68d0b9463388c6f4384d983480/Untitled%201.png)