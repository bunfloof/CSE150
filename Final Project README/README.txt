{{process.env.fullname}}

{{process.env.ucscnewemail}}

{{process.env.cruzid}}

{{process.env.studentid}}

# Lab 3: Simple Firewall using OpenFlow

## Description

This lab will introduce the user to Software-Defined Networking (SDN) and the OpenFlow protocol by creating a simple firewall using OpenFlow-enabled switches.

## Files

```
.
├── lab3.pdf                # Contains explanations and screenshots of required commands       
├── lab3controller.py       # Firewall code
└── README
```

## Instructions

To test the code, please follow the instruction below:

1. Place `lab3controller.py` in ~/pox/pox/misc directory.

2. Launch controller.

```
sudo ~/pox/pox.py misc.lab3controller
```