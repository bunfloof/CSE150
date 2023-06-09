#########################################################
# Joey Ma
# 2023 Spring CSE150 Final Project
# finalcontroller_skel.py
# controller
#########################################################
# Final Skeleton
# Hints/Reminders from Lab 3:
#
# To check the source and destination of an IP packet, you can use
# the header information... For example:
#
# ip_header = packet.find('ipv4')
#
# if ip_header.srcip == "1.1.1.1":
#   print "Packet is from 1.1.1.1"
#
# Important Note: the "is" comparison DOES NOT work for IP address
# comparisons in this way. You must use ==.
# 
# To send an OpenFlow Message telling a switch to send packets out a
# port, do the following, replacing <PORT> with the port number the 
# switch should send the packets out:
#
#    msg = of.ofp_flow_mod()
#    msg.match = of.ofp_match.from_packet(packet)
#    msg.idle_timeout = 30
#    msg.hard_timeout = 30
#
#    msg.actions.append(of.ofp_action_output(port = <PORT>))
#    msg.data = packet_in
#    self.connection.send(msg)
#
# To drop packets, simply omit the action.
#

from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class Final (object):
  """
  A Firewall object is created for each switch that connects.
  A Connection object for that switch is passed to the __init__ function.
  """
  def __init__ (self, connection):
    # Keep track of the connection to the switch so that we can
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)

  def do_final (self, packet, packet_in, port_on_switch, switch_id):
    # This is where you'll put your code. The following modifications have 
    # been made from Lab 3:
    #   - port_on_switch: represents the port that the packet was received on.
    #   - switch_id represents the id of the switch that received the packet.
    #      (for example, s1 would have switch_id == 1, s2 would have switch_id == 2, etc...)
    # You should use these to determine where a packet came from. To figure out where a packet 
    # is going, you can use the IP header information.
    ip_header = packet.find('ipv4')
    
    if ip_header is None: # Non-IP packet
      msg = of.ofp_flow_mod()
      msg.match = of.ofp_match.from_packet(packet)
      msg.idle_timeout = 300
      msg.hard_timeout = 720
      msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
      msg.data = packet_in
      self.connection.send(msg)
    else: # IP packet
      src_ip = packet.find('ipv4').srcip
      dst_ip = packet.find('ipv4').dstip
      dpid = switch_id  # The id of the switch that received the packet
  
      forwarding_rules = {
        # Forwarding rules from h10 to the server
        (1, "10.1.1.10", "10.3.9.90"): 3,  # From s1 to s5
        (5, "10.1.1.10", "10.3.9.90"): 5,  # From s5 to server

        # Reverse forwarding rules from the server to h10
        (5, "10.3.9.90", "10.1.1.10"): 1,  # From s5 to s1
        (1, "10.3.9.90", "10.1.1.10"): 1,  # From s1 to h10

        # Forwarding rules from h20 to the server
        (1, "10.1.2.20", "10.3.9.90"): 3,  # From s1 to s5
        (5, "10.1.2.20", "10.3.9.90"): 5,  # From s5 to server

        # Reverse forwarding rules from the server to h20
        (5, "10.3.9.90", "10.1.2.20"): 1,  # From s5 to s1
        (1, "10.3.9.90", "10.1.2.20"): 2,  # From s1 to h10

        # Forwarding rules from h30 to the server mine
        (2, "10.1.3.30", "10.3.9.90"): 3,  # From s2 to s5
        (5, "10.1.3.30", "10.3.9.90"): 5,  # From s5 to server

        # Reverse forwarding rules from the server to h10
        (5, "10.3.9.90", "10.1.3.30"): 2,  # From s5 to s2
        (2, "10.3.9.90", "10.1.3.30"): 1,  # From s1 to h10

        # Forwarding rules from h30 to the server staging
        (2, "10.1.4.40", "10.3.9.90"): 3,  # From s1 to s5
        (5, "10.1.4.40", "10.3.9.90"): 5,  # From s5 to server

        # Reverse forwarding rules from the server to h10
        (5, "10.3.9.90", "10.1.4.40"): 2,  # From s5 to s1
        (2, "10.3.9.90", "10.1.4.40"): 2,  # From s1 to h10

        # Stage department B
        # Forwarding rules from h10 to the server
        (3, "10.2.5.50", "10.3.9.90"): 3,  # From s3 to s5
        (5, "10.2.5.50", "10.3.9.90"): 5,  # From s5 to server

        # Reverse forwarding rules from the server to h10
        (5, "10.3.9.90", "10.2.5.50"): 3,  # From s5 to s1
        (3, "10.3.9.90", "10.2.5.50"): 1,  # From s1 to h10

        # Forwarding rules from h20 to the server
        (3, "10.2.6.60", "10.3.9.90"): 3,  # From s1 to s5
        (5, "10.2.6.60", "10.3.9.90"): 5,  # From s5 to server

        # Reverse forwarding rules from the server to h20
        (5, "10.3.9.90", "10.2.6.60"): 3,  # From s5 to s1
        (3, "10.3.9.90", "10.2.6.60"): 2,  # From s1 to h10

        # Forwarding rules from h30 to the server mine
        (4, "10.2.7.70", "10.3.9.90"): 3,  # From s2 to s5
        (5, "10.2.7.70", "10.3.9.90"): 5,  # From s5 to server

        # Reverse forwarding rules from the server to h10
        (5, "10.3.9.90", "10.2.7.70"): 4,  # From s5 to s2
        (4, "10.3.9.90", "10.2.7.70"): 1,  # From s1 to h10

        # Forwarding rules from h30 to the server staging
        (4, "10.2.8.80", "10.3.9.90"): 3,  # From s1 to s5
        (5, "10.2.8.80", "10.3.9.90"): 5,  # From s5 to server

        # Reverse forwarding rules from the server to h10
        (5, "10.3.9.90", "10.2.8.80"): 4,  # From s5 to s1
        (4, "10.3.9.90", "10.2.8.80"): 2,  # From s1 to h10

        # From h10 to h30
        (1, "10.1.1.10", "10.1.3.30"): 3,  # From s1 to s5
        (5, "10.1.1.10", "10.1.3.30"): 2,  # From s5 to s2
        (2, "10.1.1.10", "10.1.3.30"): 1,  # From s2 to h30

        # From h30 to h10
        (2, "10.1.3.30", "10.1.1.10"): 3,  # From s2 to s5
        (5, "10.1.3.30", "10.1.1.10"): 1,  # From s5 to s1
        (1, "10.1.3.30", "10.1.1.10"): 1,  # From s1 to h10

        # From h10 to h40
        (1, "10.1.1.10", "10.1.4.40"): 3,  # From s1 to s5
        (5, "10.1.1.10", "10.1.4.40"): 2,  # From s5 to s2
        (2, "10.1.1.10", "10.1.4.40"): 2,  # From s2 to h40

        # From h40 to h10
        (2, "10.1.4.40", "10.1.1.10"): 3,  # From s2 to s5
        (5, "10.1.4.40", "10.1.1.10"): 1,  # From s5 to s1
        (1, "10.1.4.40", "10.1.1.10"): 1,  # From s1 to h10

        # From h20 to h30
        (1, "10.1.2.20", "10.1.3.30"): 3,  # From s1 to s5
        (5, "10.1.2.20", "10.1.3.30"): 2,  # From s5 to s2
        (2, "10.1.2.20", "10.1.3.30"): 1,  # From s2 to h30

        # From h30 to h20
        (2, "10.1.3.30", "10.1.2.20"): 3,  # From s2 to s5
        (5, "10.1.3.30", "10.1.2.20"): 1,  # From s5 to s1
        (1, "10.1.3.30", "10.1.2.20"): 2,  # From s1 to h20
        # From h20 to h40
        (1, "10.1.2.20", "10.1.4.40"): 3,  # From s1 to s5
        (5, "10.1.2.20", "10.1.4.40"): 2,  # From s5 to s2
        (2, "10.1.2.20", "10.1.4.40"): 2,  # From s2 to h40

        # From h40 to h20
        (2, "10.1.4.40", "10.1.2.20"): 3,  # From s2 to s5
        (5, "10.1.4.40", "10.1.2.20"): 1,  # From s5 to s1
        (1, "10.1.4.40", "10.1.2.20"): 2,  # From s1 to h20

        # From h30 to h40
        (2, "10.1.3.30", "10.1.4.40"): 2,  # From s2 to h40
        # From h40 to h30
        (2, "10.1.4.40", "10.1.3.30"): 1,  # From s2 to h30
  
        # From h20 to h40
        (1, "10.1.2.20", "10.1.4.40"): 3,  # From s1 to s5
        (1, "10.1.1.10", "10.1.2.20"): 2,  # From s1 to h20
        
        # From h20 to h10
        (1, "10.1.2.20", "10.1.1.10"): 1,  # From s1 to h10
        # From h30 to h40
        (2, "10.1.3.30", "10.1.4.40"): 2,  # From s2 to h40
        # From h40 to h30
        (2, "10.1.4.40", "10.1.3.30"): 1,  # From s2 to h30

        # Forwarding rules from h10 to h30
        (1, "10.1.1.10", "10.1.3.30"): 3,  # From s1 to s5
        (5, "10.1.1.10", "10.1.3.30"): 2,  # From s5 to s2
        (2, "10.1.1.10", "10.1.3.30"): 1,  # From s2 to h30
    
        # Reverse forwarding rules from h30 to h10
        (2, "10.1.3.30", "10.1.1.10"): 3,  # From s2 to s5
        (5, "10.1.3.30", "10.1.1.10"): 1,  # From s5 to s1
        (1, "10.1.3.30", "10.1.1.10"): 1,  # From s1 to h10
    
        # Forwarding rules from h_trust to Department A hosts (h10, h20, h30, h40)
        (6, "108.24.31.112", "10.1.1.10"): 3,  # From s6 to s5
        (5, "108.24.31.112", "10.1.1.10"): 1,  # From s5 to s1
        (1, "108.24.31.112", "10.1.1.10"): 1,  # From s1 to h10
    
        (6, "108.24.31.112", "10.1.2.20"): 3,  # From s6 to s5
        (5, "108.24.31.112", "10.1.2.20"): 1,  # From s5 to s1
        (1, "108.24.31.112", "10.1.2.20"): 2,  # From s1 to h20
    
        (6, "108.24.31.112", "10.1.3.30"): 3,  # From s6 to s5
        (5, "108.24.31.112", "10.1.3.30"): 2,  # From s5 to s2
        (2, "108.24.31.112", "10.1.3.30"): 1,  # From s2 to h30
    
        (6, "108.24.31.112", "10.1.4.40"): 3,  # From s6 to s5
        (5, "108.24.31.112", "10.1.4.40"): 2,  # From s5 to s2
        (2, "108.24.31.112", "10.1.4.40"): 2,  # From s2 to h40
    
        # Reverse forwarding rules from Department A hosts to h_trust
        (1, "10.1.1.10", "108.24.31.112"): 3,  # From s1 to s5
        (5, "10.1.1.10", "108.24.31.112"): 6,  # From s5 to s6
        (6, "10.1.1.10", "108.24.31.112"): 1,  # From s6 to h_trust
    
        (1, "10.1.2.20", "108.24.31.112"): 3,  # From s1 to s5
        (5, "10.1.2.20", "108.24.31.112"): 6,  # From s5 to s6
        (6, "10.1.2.20", "108.24.31.112"): 1,  # From s6 to h_trust
    
        (2, "10.1.3.30", "108.24.31.112"): 3,  # From s2 to s5
        (5, "10.1.3.30", "108.24.31.112"): 6,  # From s5 to s6
        (6, "10.1.3.30", "108.24.31.112"): 1,  # From s6 to h_trust
    
        (2, "10.1.4.40", "108.24.31.112"): 3,  # From s2 to s5
        (5, "10.1.4.40", "108.24.31.112"): 6,  # From s5 to s6
        (6, "10.1.4.40", "108.24.31.112"): 1,  # From s6 to h_trust

        # Department B hosts (h50, h60, h70, h80)
        # From h50 to h60
        (3, "10.2.5.50", "10.2.6.60"): 3,  # From s3 to s5
        (5, "10.2.5.50", "10.2.6.60"): 3,  # From s5 to s3
        (3, "10.2.5.50", "10.2.6.60"): 2,  # From s3 to h60
    
        # From h60 to h50
        (3, "10.2.6.60", "10.2.5.50"): 3,  # From s3 to s5
        (5, "10.2.6.60", "10.2.5.50"): 3,  # From s5 to s3
        (3, "10.2.6.60", "10.2.5.50"): 1,  # From s3 to h50
    
        # From h50 to h70
        (3, "10.2.5.50", "10.2.7.70"): 3,  # From s3 to s5
        (5, "10.2.5.50", "10.2.7.70"): 4,  # From s5 to s4
        (4, "10.2.5.50", "10.2.7.70"): 1,  # From s4 to h70

        # From h70 to h50
        (4, "10.2.7.70", "10.2.5.50"): 3,  # From s4 to s5
        (5, "10.2.7.70", "10.2.5.50"): 3,  # From s5 to s3
        (3, "10.2.7.70", "10.2.5.50"): 1,  # From s3 to h50

        # From h50 to h80
        (3, "10.2.5.50", "10.2.8.80"): 3,  # From s3 to s5
        (5, "10.2.5.50", "10.2.8.80"): 4,  # From s5 to s4
        (4, "10.2.5.50", "10.2.8.80"): 2,  # From s4 to h80

        # From h80 to h50
        (4, "10.2.8.80", "10.2.5.50"): 3,  # From s4 to s5
        (5, "10.2.8.80", "10.2.5.50"): 3,  # From s5 to s3
        (3, "10.2.8.80", "10.2.5.50"): 1,  # From s3 to h50

        # From h60 to h80
        (3, "10.2.6.60", "10.2.8.80"): 3,  # From s3 to s5
        (5, "10.2.6.60", "10.2.8.80"): 4,  # From s5 to s4
        (4, "10.2.6.60", "10.2.8.80"): 2,  # From s4 to h80
    
        # From h80 to h60
        (4, "10.2.8.80", "10.2.6.60"): 3,  # From s4 to s5
        (5, "10.2.8.80", "10.2.6.60"): 3,  # From s5 to s3
        (3, "10.2.8.80", "10.2.6.60"): 2,  # From s3 to h60

        # Stage 2
        # Forwarding rules from h50 to h60
        (3, "10.2.5.50", "10.2.6.60"): 2,  # From s3 to h60
        # Reverse forwarding rules from h60 to h50
        (3, "10.2.6.60", "10.2.5.50"): 1,  # From s3 to h50
        
        # Forwarding rules from h50 to h70
        (3, "10.2.5.50", "10.2.7.70"): 3,  # From s3 to s5
        (5, "10.2.5.50", "10.2.7.70"): 4,  # From s5 to s4
        (4, "10.2.5.50", "10.2.7.70"): 1,  # From s4 to h70
        # Reverse forwarding rules from h70 to h50
        (4, "10.2.7.70", "10.2.5.50"): 3,  # From s4 to s5
        (5, "10.2.7.70", "10.2.5.50"): 3,  # From s5 to s3
        (3, "10.2.7.70", "10.2.5.50"): 1,  # From s3 to h50

        # Forwarding rules from h50 to h80
        (3, "10.2.5.50", "10.2.8.80"): 3,  # From s3 to s5
        (5, "10.2.5.50", "10.2.8.80"): 4,  # From s5 to s4
        (4, "10.2.5.50", "10.2.8.80"): 2,  # From s4 to h80
        # Reverse forwarding rules from h80 to h50
        (4, "10.2.8.80", "10.2.5.50"): 3,  # From s4 to s5
        (5, "10.2.8.80", "10.2.5.50"): 3,  # From s5 to s3
        (3, "10.2.8.80", "10.2.5.50"): 1,  # From s3 to h50

        # Forwarding rules from h60 to h70
        (3, "10.2.6.60", "10.2.7.70"): 3,  # From s3 to s5
        (5, "10.2.6.60", "10.2.7.70"): 4,  # From s5 to s4
        (4, "10.2.6.60", "10.2.7.70"): 1,  # From s4 to h70
        # Reverse forwarding rules from h70 to h60
        (4, "10.2.7.70", "10.2.6.60"): 3,  # From s4 to s5
        (5, "10.2.7.70", "10.2.6.60"): 3,  # From s5 to s3
        (3, "10.2.7.70", "10.2.6.60"): 2,  # From s3 to h60

        # Forwarding rules from h60 to h80
        (3, "10.2.6.60", "10.2.8.80"): 3,  # From s3 to s5
        (5, "10.2.6.60", "10.2.8.80"): 4,  # From s5 to s4
        (4, "10.2.6.60", "10.2.8.80"): 2,  # From s4 to h80
        # Reverse forwarding rules from h80 to h60
        (4, "10.2.8.80", "10.2.6.60"): 3,  # From s4 to s5
        (5, "10.2.8.80", "10.2.6.60"): 3,  # From s5 to s3
        (3, "10.2.8.80", "10.2.6.60"): 2,  # From s3 to h60

        # Forwarding rules from h70 to h80
        (4, "10.2.7.70", "10.2.8.80"): 2,  # From s4 to h80
        # Reverse forwarding rules from h80 to h70
        (4, "10.2.8.80", "10.2.7.70"): 1,  # From s4 to h70
        
        # sammy tesfai h_trust to h_untrust and vice versa
        (6, "108.24.31.112", "106.44.82.103"): 2,  # From s2 to s5
        (6, "106.44.82.103", "108.24.31.112"): 1,  # From s5 to s6

      }

      tcp_forwarding_rules = {
        (6, "106.44.82.103", "10.1.1.10"): 3,  # From s6 to s5
        (5, "106.44.82.103", "10.1.1.10"): 1,  # From s5 to s1
        (1, "106.44.82.103", "10.1.1.10"): 1,  # From s1 to h10
    

        (1, "10.1.1.10", "106.44.82.103"): 3,  # From s1 to s5
        (5, "10.1.1.10", "106.44.82.103"): 6,  # From s5 to s6
        (6, "10.1.1.10", "106.44.82.103"): 2,  # From s6 to h_untrust
    
        (6, "106.44.82.103", "10.1.2.20"): 3,  # From s6 to s5
        (5, "106.44.82.103", "10.1.2.20"): 1,  # From s5 to s1
        (1, "106.44.82.103", "10.1.2.20"): 2,  # From s1 to h20
    
        (1, "10.1.2.20", "106.44.82.103"): 3,  # From s1 to s5
        (5, "10.1.2.20", "106.44.82.103"): 6,  # From s5 to s6
        (6, "10.1.2.20", "106.44.82.103"): 2,  # From s6 to h_untrust
        # h30 and h_untrust
        (6, "106.44.82.103", "10.1.3.30"): 3,  # From s6 to s5
        (5, "106.44.82.103", "10.1.3.30"): 2,  # From s5 to s2
        (2, "106.44.82.103", "10.1.3.30"): 1,  # From s2 to h30
    
        (2, "10.1.3.30", "106.44.82.103"): 3,  # From s2 to s5
        (5, "10.1.3.30", "106.44.82.103"): 6,  # From s5 to s6
        (6, "10.1.3.30", "106.44.82.103"): 2,  # From s6 to h_untrust
    
        # h40 and h_untrust
        (6, "106.44.82.103", "10.1.4.40"): 3,  # From s6 to s5
        (5, "106.44.82.103", "10.1.4.40"): 2,  # From s5 to s2
        (2, "106.44.82.103", "10.1.4.40"): 2,  # From s2 to h40
    
        (2, "10.1.4.40", "106.44.82.103"): 3,  # From s2 to s5
        (5, "10.1.4.40", "106.44.82.103"): 6,  # From s5 to s6
        (6, "10.1.4.40", "106.44.82.103"): 2,  # From s6 to h_untrust
        
        # h50 and h_untrust
        (6, "106.44.82.103", "10.2.5.50"): 3,  # From s6 to s5
        (5, "106.44.82.103", "10.2.5.50"): 3,  # From s5 to s3
        (3, "106.44.82.103", "10.2.5.50"): 1,  # From s3 to h50
    
        (3, "10.2.5.50", "106.44.82.103"): 3,  # From s3 to s5
        (5, "10.2.5.50", "106.44.82.103"): 6,  # From s5 to s6
        (6, "10.2.5.50", "106.44.82.103"): 2,  # From s6 to h_untrust
    
        # h60 and h_untrust
        (6, "106.44.82.103", "10.2.6.60"): 3,  # From s6 to s5
        (5, "106.44.82.103", "10.2.6.60"): 3,  # From s5 to s3
        (3, "106.44.82.103", "10.2.6.60"): 2,  # From s3 to h60
    
        (3, "10.2.6.60", "106.44.82.103"): 3,  # From s3 to s5
        (5, "10.2.6.60", "106.44.82.103"): 6,  # From s5 to s6
        (6, "10.2.6.60", "106.44.82.103"): 2,  # From s6 to h_untrust
    
        # h70 and h_untrust
        (6, "106.44.82.103", "10.2.7.70"): 3,  # From s6 to s5
        (5, "106.44.82.103", "10.2.7.70"): 4,  # From s5 to s4
        (4, "106.44.82.103", "10.2.7.70"): 1,  # From s4 to h70
    
        (4, "10.2.7.70", "106.44.82.103"): 3,  # From s4 to s5
        (5, "10.2.7.70", "106.44.82.103"): 6,  # From s5 to s6
        (6, "10.2.7.70", "106.44.82.103"): 2,  # From s6 to h_untrust
    
        # h80 and h_untrust
        (6, "106.44.82.103", "10.2.8.80"): 3,  # From s6 to s5
        (5, "106.44.82.103", "10.2.8.80"): 4,  # From s5 to s4
        (4, "106.44.82.103", "10.2.8.80"): 2,  # From s4 to h80
    
        (4, "10.2.8.80", "106.44.82.103"): 3,  # From s4 to s5
        (5, "10.2.8.80", "106.44.82.103"): 6,  # From s5 to s6
        (6, "10.2.8.80", "106.44.82.103"): 2,  # From s6 to h_untrust

        # sammy tesfai h_trust to h_untrust and vice versa
        (6, "108.24.31.112", "106.44.82.103"): 2,  # From s2 to s5
        (6, "106.44.82.103", "108.24.31.112"): 1,  # From s5 to s6
      }

      key = (dpid, str(src_ip), str(dst_ip))
      if key in forwarding_rules:
        #print("dpid={0}, src_ip={1}, dst_ip={2}".format(dpid, src_ip, dst_ip))
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet)
        msg.idle_timeout = 300
        msg.hard_timeout = 720
        msg.actions.append(of.ofp_action_output(port = forwarding_rules[key]))
        msg.data = packet_in
        self.connection.send(msg)
      if key in tcp_forwarding_rules and packet.find('tcp'):
        #print("dpid={0}, src_ip={1}, dst_ip={2}".format(dpid, src_ip, dst_ip))
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet)
        msg.idle_timeout = 300
        msg.hard_timeout = 720
        msg.actions.append(of.ofp_action_output(port = tcp_forwarding_rules[key]))
        msg.data = packet_in
        self.connection.send(msg)
      else:
        # Drop the packet if there's no matching rule
        pass
        

  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """
    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.
    self.do_final(packet, packet_in, event.port, event.dpid)

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Final(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
