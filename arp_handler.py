from pox.core import core
import pox.openflow.libopenflow_01 as of
import pox.lib.packet as pkt

log = core.getLogger()


arp_table = {}

def _handle_PacketIn(event):
    packet = event.parsed

    # 🔹 1. Intercept ARP packets
    if packet.type == packet.ARP_TYPE:
        arp_pkt = packet.payload
        log.info("ARP packet intercepted")

        
        arp_table[arp_pkt.protosrc] = arp_pkt.hwsrc
        log.info("Learned Host: %s -> %s", arp_pkt.protosrc, arp_pkt.hwsrc)


        
        if arp_pkt.protodst in arp_table:

            log.info("Generating ARP reply for %s", arp_pkt.protodst)

            reply = pkt.arp()
            reply.opcode = pkt.arp.REPLY
            reply.hwsrc = arp_table[arp_pkt.protodst]
            reply.hwdst = arp_pkt.hwsrc
            reply.protosrc = arp_pkt.protodst
            reply.protodst = arp_pkt.protosrc

            eth = pkt.ethernet()
            eth.type = pkt.ethernet.ARP_TYPE
            eth.src = reply.hwsrc
            eth.dst = reply.hwdst
            eth.payload = reply

            msg = of.ofp_packet_out()
            msg.data = eth.pack()
            msg.actions.append(of.ofp_action_output(port=event.port))
            event.connection.send(msg)

            log.info("ARP reply sent")

        else:
            
            msg = of.ofp_packet_out()
            msg.data = event.ofp
            msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
            event.connection.send(msg)

    else:
        
        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        event.connection.send(msg)


def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("ARP SDN Controller Started")
