{{process.env.fullname}}

{{process.env.ucscnewemail}}

{{process.env.cruzid}}

{{process.env.studentid}}

# Final Project: Implementing a Simple Router

## Description

This lab will introduce the user to Software-Defined Networking (SDN) and the OpenFlow protocol by creating a simple firewall using OpenFlow-enabled switches.

## Files

```
.
├── final_skel.py                # Contains topology code
├── finalcontroller_skel.py      # Contains firewall code
├── project.pdf                  # Contains explanations and screenshots of required commands
└── README.txt
```

## Instructions

To test the code, please follow the instructions below:

1. Place `finalcontroller_skel.py` in ~/pox/pox/misc directory.

2. Launch controller.

```
sudo ~/pox/pox.py misc.finalcontroller_skel.py
```

3. Place `final_skel.py` in ~ directory.

4. Launch topology.

```
sudo python final_skel.py
```