# Final Skeleton
#
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
      # Flood the packet
      msg = of.ofp_flow_mod()
      msg.match = of.ofp_match.from_packet(packet)
      msg.idle_timeout = 30
      msg.hard_timeout = 30
      msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
      msg.data = packet_in
      self.connection.send(msg)
    else: # IP packet
      src_ip = ip_header.srcip
      dst_ip = ip_header.dstip
      icmp_packet = packet.find('icmp')

      # If the packet is from untrusted host, drop all ICMP packets and any IP traffic to the server.
      if src_ip == "106.44.82.103" and (icmp_packet is not None or dst_ip == "10.3.9.90"):
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet)
        msg.idle_timeout = 30
        msg.hard_timeout = 30
        msg.data = packet_in
        self.connection.send(msg)
      # If the packet is from trusted host, drop ICMP packets to hosts in Department B and the server, and any IP traffic to the server.
      elif src_ip == "108.24.31.112" and ((icmp_packet is not None and dst_ip in ["10.2.5.50", "10.2.6.60", "10.2.7.70", "10.2.8.80", "10.3.9.90"]) or dst_ip == "10.3.9.90"):
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet)
        msg.idle_timeout = 30
        msg.hard_timeout = 30
        msg.data = packet_in
        self.connection.send(msg)
      # If the packet is from hosts in Department A, drop ICMP packets to hosts in Department B.
      elif src_ip in ["10.1.1.10", "10.1.2.20", "10.1.3.30", "10.1.4.40"] and icmp_packet is not None and dst_ip in ["10.2.5.50", "10.2.6.60", "10.2.7.70", "10.2.8.80"]:
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet)
        msg.idle_timeout = 30
        msg.hard_timeout = 30
        msg.data = packet_in
        self.connection.send(msg)
      # If the packet is from hosts in Department B, drop ICMP packets to hosts in Department A.
      elif src_ip in ["10.2.5.50", "10.2.6.60", "10.2.7.70", "10.2.8.80"] and icmp_packet is not None and dst_ip in ["10.1.1.10", "10.1.2.20", "10.1.3.30", "10.1.4.40"]:
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet)
        msg.idle_timeout = 30
        msg.hard_timeout = 30
        msg.data = packet_in
        self.connection.send(msg)
      else: # Other cases, forward the packets
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet)
        msg.idle_timeout = 30
        msg.hard_timeout = 30
        msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
        msg.data = packet_in
        self.connection.send(msg)

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
