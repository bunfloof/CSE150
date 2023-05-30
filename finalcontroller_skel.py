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
    # determine the source and destination IP addresses
    ip_packet = packet.find('ipv4')
    if not ip_packet:
        # Not an IP packet, flood
        self.send_packet(packet_in.buffer_id, packet_in.data, of.OFPP_FLOOD, switch_id)
        return

    icmp_packet = packet.find('icmp')
    tcp_packet = packet.find('tcp')
    udp_packet = packet.find('udp')

    # Assign host IPs to port numbers for each switch
    ip_to_port = {
        '10.1.1.10': 1 if switch_id == 1 else 1 if switch_id == 5 else None,
        '10.1.2.20': 2 if switch_id == 1 else 1 if switch_id == 5 else None,
        '10.1.3.30': 1 if switch_id == 2 else 2 if switch_id == 5 else None,
        '10.1.4.40': 2 if switch_id == 2 else 2 if switch_id == 5 else None,
        '10.2.5.50': 1 if switch_id == 3 else 3 if switch_id == 5 else None,
        '10.2.6.60': 2 if switch_id == 3 else 3 if switch_id == 5 else None,
        '10.2.7.70': 1 if switch_id == 4 else 4 if switch_id == 5 else None,
        '10.2.8.80': 2 if switch_id == 4 else 4 if switch_id == 5 else None,
        '10.3.9.90': 5 if switch_id == 5 else None,
        '108.24.31.112': 1 if switch_id == 6 else 6 if switch_id == 5 else None,
        '106.44.82.103': 2 if switch_id == 6 else 6 if switch_id == 5 else None,
    }

    msg = of.ofp_flow_mod()
    msg.match = of.ofp_match.from_packet(packet)

    # When the IP address of the destination host is known
    if str(ip_packet.dstip) in ip_to_port and ip_to_port[str(ip_packet.dstip)] is not None:
        # Rules for Untrusted Host (106.44.82.103)
        if str(ip_packet.srcip) == '106.44.82.103':
            # Untrusted Host cannot send ICMP traffic to Host 10 to 80, or the Server.
            if icmp_packet or str(ip_packet.dstip) == '10.3.9.90':
                return
        # Rules for Trusted Host (108.24.31.112)
        if str(ip_packet.srcip) == '108.24.31.112':
            # Trusted Host cannot send ICMP traffic to Host 50 to 80 in Department B, or the Server.
            if icmp_packet and (str(ip_packet.dstip).startswith('10.2') or str(ip_packet.dstip) == '10.3.9.90'):
                return
        # Hosts in Department A (Host 10 to 40) cannot send any ICMP traffic to the hosts in Department B (Host 50 to 80), and vice versa.
        if icmp_packet and ((str(ip_packet.srcip).startswith('10.1') and str(ip_packet.dstip).startswith('10.2')) or (str(ip_packet.srcip).startswith('10.2') and str(ip_packet.dstip).startswith('10.1'))):
            return
    # When the IP address of the destination host is known
    if str(ip_packet.dstip) in ip_to_port and ip_to_port[str(ip_packet.dstip)] is not None:
        # Rules for Untrusted Host (106.44.82.103)
        if str(ip_packet.srcip) == '106.44.82.103':
            # Untrusted Host cannot send ICMP traffic to Host 10 to 80, or the Server.
            if icmp_packet or str(ip_packet.dstip) == '10.3.9.90':
                return
        # Rules for Trusted Host (108.24.31.112)
        if str(ip_packet.srcip) == '108.24.31.112':
            # Trusted Host cannot send ICMP traffic to Host 50 to 80 in Department B, or the Server.
            if icmp_packet and (str(ip_packet.dstip).startswith('10.2') or str(ip_packet.dstip) == '10.3.9.90'):
                return
        # Hosts in Department A (Host 10 to 40) cannot send any ICMP traffic to the hosts in Department B (Host 50 to 80), and vice versa.
        if icmp_packet and ((str(ip_packet.srcip).startswith('10.1') and str(ip_packet.dstip).startswith('10.2')) or (str(ip_packet.srcip).startswith('10.2') and str(ip_packet.dstip).startswith('10.1'))):
            return

        msg.actions.append(of.ofp_action_output(port = ip_to_port[str(ip_packet.dstip)]))
    else:
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
