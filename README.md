SDN ARP Handler - Project 6

Problem Statement In traditional networking, switches broadcast ARP requests to all ports, which can lead to unnecessary traffic. This project implements an SDN-based ARP Proxy using the POX controller. The controller intercepts ARP requests, learns host locations (IP-to-MAC mappings), and generates ARP replies directly, reducing broadcast traffic and validating secure communication within a Mininet topology.

Setup and Execution Steps This project was developed on a Dell laptop server running Ubuntu on Windows.

Prerequisites Mininet: Network emulator.

POX Controller: Python-based SDN controller (Source-based installation used for Python 3.12 compatibility).

Execution Start the Controller: Navigate to the pox directory and run the custom handler:

Bash python3 pox.py arp_handler Start the Topology: In a separate terminal, create a single switch topology with 3 hosts:

Bash sudo mn --topo single,3 --controller remote,ip=127.0.0.1 --mac 3. SDN Logic & Implementation The controller logic handles PacketIn events using a match-action approach:

Match: Incoming packets are parsed to identify ARP types.

Action (Learning): The controller extracts the source IP and MAC to populate an internal arp_table.

Action (Proxying): If the destination IP is known, the controller constructs a pkt.arp.REPLY and wraps it in an Ethernet frame using ofp_packet_out to send back to the requester.

Test Scenarios & Functional Validation As per the project requirements, the following scenarios demonstrate the working behavior:
Scenario 1: Normal Operation (Success) Condition: POX controller is running arp_handler.py.

Observation: The controller logs "Learned mapping" and "Proxying ARP reply".

Result: pingall succeeds with 0% packet loss.

Proof:
<img width="1058" height="986" alt="Screenshot 2026-04-10 092033" src="https://github.com/user-attachments/assets/5509e878-8515-4718-985f-d355324ac222" />
