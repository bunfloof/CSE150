# Lab 3 Skeleton
#
# Based on of_tutorial by James McCauley

from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class Firewall (object):
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

  def do_firewall (self, packet, packet_in):
    # The code in here will be executed for every packet.
    
    if packet.find('arp'): # check if packet is ARP
        fm = of.ofp_flow_mod() # create new flow mod message
        fm.match = of.ofp_match.from_packet(packet) # previously match ARP packets (dl_type=0x0806), but now match all unique
        fm.idle_timeout = 30 # set idle timeout to 30 seconds
        fm.hard_timeout = 180 # set hard timeout to 180 seconds
        fm.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD)) # flood ARP packet to all ports
        self.connection.send(fm) # send flow mod message to switch
        return
    
    if packet.find('tcp'): # check if packet is TCP
        fm = of.ofp_flow_mod() # create new flow mod message to allow TCP packets
        fm.match = of.ofp_match.from_packet(packet) # previously match TCP packets (dl_type=0x0800, nw_proto=6), but now match all unique
        fm.idle_timeout = 30 # set idle timeout to 30 seconds
        fm.hard_timeout = 180 # set hard timeout to 180 seconds
        fm.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD)) # flood TCP packet to all ports
        self.connection.send(fm) # send the flow mod message to the switch
        return
      
    # if packet not ARP or TCP, then drop it
    fm = of.ofp_flow_mod() # create new flow mod message
    fm.match = of.ofp_match.from_packet(packet) # previously match IP packets (dl_type=0x0800), but now match all unique
    fm.idle_timeout = 30 # set idle timeout to 30 seconds
    fm.hard_timeout = 180 # set hard timeout to 180 seconds
    fm.priority = 1 # set priority to 1 (lower than default) to ensure this rule is matched last
    fm.actions.append(of.ofp_action_output(port=of.OFPP_NONE)) # do nothing to packet
    self.connection.send(fm) # send flow mod message to switch

  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """

    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    packet_in = event.ofp # The actual ofp_packet_in message.
    self.do_firewall(packet, packet_in)

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Firewall(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
