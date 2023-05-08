# Lab 1_ Installing and Using Mininet-1

published: No

### Pre-lab Questions

1. [5] What command will show you which groups you are a member of?

```cpp
groups
```

1.  [5] What does the environmental variable “$?” hold? (Hint: the command ‘echo $?’ will should you this on your screen)

`$?` holds the return value of the last executed command.

1. [5] What key combination will suspend a currently running process and place it as a background process?

`Ctrl + Z` to suspend a running process followed by `bg` to place in background process.

1.  [5] With what command (and arguments) can you find out your kernel version and the “nodename”?

```cpp
uname -vn
```

1. [5] What is the difference between the paths “.”, “..”, and “~”? What does the path “/” refer to when not

`.` refers to the current working directory.

`..` refers to the parent directory of the current working directory.

`~` refers to home directory of the current user.

`/` refers to the root directory.

1. [5] What is a pid? Which command would you use to find the “pid” for a running process?

A PID or process identifier is a unique, non-negative integer, assigned by the operating system to identify a running process.

`ps` displays information about the currently running processes.

1. [20] Write a single command that will return every user’s default shell. [You may chain commands using piping and redirects] (Hint: See ‘Chapter 19: filters’ of [linux-training.be](http://linux-training.be/) as well as the man page for the /etc/passwd file: [https://linux.die.net/man/5/passwd](https://linux.die.net/man/5/passwd))

```cpp
cut -d: -f7 /etc/passwd
```

Citation(s):

Daniel J. Barrett. (2023). KAPITEL 5: Das Arsenal erweitern. In *Produktiv auf der Linux-*

*Kommandozeile: Sicher und souverän mit linux arbeiten*. O'Reilly. 

1. [10] What is the difference between “sudo” and “su root”?

`sudo` or “substitute user and do” allows a user to execute a command as another user specified in `/etc/sudoers` configuration with root privileges.

`su root` or “switch user root” switches to the root account.

1. [10] How would you tell your computer to run a program or script on a schedule or set interval on Linux? E.g. Run this program once every 30 minutes.

Use the `cron` daemon to schedule tasks or cron jobs at specified intervals. To run a program once every 30 minutes:

First, edit the current user’s cron table.

```cpp
crontab -e
```

Next, add this new line:

```cpp
*/30 * * * * /path/to/your/script-or-command
```

- `/30`: This means every 30 minutes.
- `*`: Any value for the hour field (0-23).
- `*`: Any value for the day of the month field (1-31).
- `*`: Any value for the month field (1-12).
- `*`: Any value for the day of the week field (0-7, where both 0 and 7 represent Sunday).
- `/path/to/script-or-command`: The full path to the script or command you want to execute.

Lastly, save the file and exit the editor.

10. [30] Write a shell script that only prints the even numbered lines of each file in the current directory. The output should be filename: line for each even numbered line. You do not need to print line numbers.

```bash
#!/bin/bash

for file in *; do
  if [[ -f "$file" ]] && [[ "$file" != "$(basename $0)" ]]; then
    awk 'NR % 2 == 0 { print FILENAME ": " $0 }' "$file"
  fi
done
```

![Untitled](Lab%201_%20Installing%20and%20Using%20Mininet-1%20742a3b0d8eac40a79905934f36cd5cc1/Untitled.png)

Citation(s):

Robbins, A. (2015). Chapter 1. Getting Started with awk. In *Effective Awk Programming: Universal Text Processing and Pattern Matching* (p. 12), O'Reilly. 

### The Lab:

1. In Mininet change the default configuration to have 4 hosts connected to a switch.

![Untitled](Lab%201_%20Installing%20and%20Using%20Mininet-1%20742a3b0d8eac40a79905934f36cd5cc1/Untitled%201.png)

1. [30 pts] Save a screenshot of dump and pingall output. Explain what is being shown in the screenshot

![Untitled](Lab%201_%20Installing%20and%20Using%20Mininet-1%20742a3b0d8eac40a79905934f36cd5cc1/Untitled%202.png)

The `dump` command in Mininet prints the current network configuration, including hosts, switches, and the controller. Following problem 1, it shows the four hosts (h1, h2, h3, and h4) with their respective IP addresses (10.0.0.1 to 10.0.0.4) and process IDs (pid). It also shows the Open vSwitch (OVSSwitch s1) with its local loopback address (lo:127.0.0.1) and its interfaces (s1-eth1 to s1-eth4) with 'None' as their IP addresses since they're switch interfaces. Lastly, it shows the default Mininet controller (Controller c0) with its IP address (127.0.0.1) and port (6633) along with its process ID (pid).

![Untitled](Lab%201_%20Installing%20and%20Using%20Mininet-1%20742a3b0d8eac40a79905934f36cd5cc1/Untitled%203.png)

The **`pingall`** command in Mininet tests the connectivity between all pairs of hosts in the network. It sends ICMP ECHO_REQUEST packets (pings) from each host to every other host and checks if they receive a response (ICMP ECHO_REPLY). Following problem 1, the output shows that all hosts (h1, h2, h3, and h4) can successfully ping each other. There is no packet loss (0% dropped), and all 12 pings (4 hosts * 3 pings/host) were successfully received.

1. [10 pts] Run the iperf command as well, and screenshot the output, how fast is the connect?

After running iperf The connection speed between h1 and h4 is measured at 65.6 Gbits/sec and 65.6 Gbits/sec.

![Untitled](Lab%201_%20Installing%20and%20Using%20Mininet-1%20742a3b0d8eac40a79905934f36cd5cc1/Untitled%204.png)

1. Run wireshark, and using the display filter, typing “of” in filter line and remember to click Apply after you start. Note: When you run wireshark you should do so as “sudo wireshark” in a new terminal. When you choose an interface to capture on, you should select “any”.

a. [20 pts] Run ping from a host to any other host using hX ping -c 5 hY. How many of_packet_in messages show up? Take a screenshot of your results.

After running `h1 ping -c 5 h4`, 6 of_packet_in messages showed up.

![Untitled](Lab%201_%20Installing%20and%20Using%20Mininet-1%20742a3b0d8eac40a79905934f36cd5cc1/Untitled%205.png)

b. [20 pts] What is the source and destination IP addresses for these entries? Find another packet that matches the “of” filter with the OpenFlow typefield set to OF_PACKET_OUT. What is the source and destination IP address for this entry? Take screenshots showing your results.

For the first part of this question, the source of destination of these entries of of_packet_in are listed below:

- Frame 23: Source IP 10.0.0.1 (h1) and Destination IP 10.0.0.4 (h4)
- Frame 31: Source IP 10.0.0.4 (h4) and Destination IP 10.0.0.1 (h1)
- Frame 36: Source IP 10.0.01 (h1) and Destination IP 10.0.0.4 (h4)
- Frame 55: Source MAC 8e:3c:17:e6:7d:ff (IP 127.0.0.1) and Destination MAC c2:0c:09:2d:61:83 (IP 127.0.0.1)
- Frame 60: Source MAC c2:0c:09:2d:61:83 (IP 127.0.0.1) and Destination MAC 8e:3c:17:e6:7d:ff (IP 127.0.0.1)

For the second part of this question, the source of the OF_PACKET_OUT entry is 127.0.0.1 and its destination is 127.0.0.1.

![Untitled](Lab%201_%20Installing%20and%20Using%20Mininet-1%20742a3b0d8eac40a79905934f36cd5cc1/Untitled%206.png)

c. [20 pts] Replace the display filter for “of” to “icmp && not of”. Run pingall again, how many entries are generated in wireshark? What types of icmp entries show up? Take a screenshot of your results.

57 more displayed entries were generated from existing 23 displayed entries before, totaling 80 displayed entries. There are four devices with IP addresses 10.0.0.1, 10.0.0.2, 10.0.0.3, and 10.0.0.4 communicating using the ICMP (Internet Control Message Protocol) with echo request (ping) and echo reply messages. The devices are receiving echo replies from the devices they sent echo requests to, which means that communication between these devices is working properly.

![Untitled](Lab%201_%20Installing%20and%20Using%20Mininet-1%20742a3b0d8eac40a79905934f36cd5cc1/Untitled%207.png)
