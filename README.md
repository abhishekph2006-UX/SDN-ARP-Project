# ARP Handling in SDN using POX Controller

##  Objective

To implement ARP request and reply handling using an SDN controller by intercepting ARP packets, generating responses, enabling host discovery, and validating communication.

---

##  Tools Used

* Mininet
* POX Controller
* OpenFlow

---

## 🧠 Project Description

In traditional networks, ARP requests are broadcast.
In this project, the SDN controller handles ARP centrally.

The controller:

* Intercepts ARP packets (Packet-In)
* Learns IP → MAC mapping (Host Discovery)
* Generates ARP replies (Proxy ARP)
* Controls communication between hosts

---

## ⚙️ Features Implemented

### 1. Intercept ARP Packets

Controller captures ARP requests using Packet-In.

### 2. Generate ARP Responses

Controller sends ARP reply instead of broadcast.

### 3. Host Discovery

Controller maintains ARP table (IP → MAC).

### 4. Validate Communication

Ping is used to verify communication.

---

## 🚀 How to Run

### 🔹 Terminal 1 (Controller)
<img width="615" height="458" alt="image" src="https://github.com/user-attachments/assets/3d006d47-362b-438d-9e03-1ec1ce13adfa" />



### 🔹 Terminal 2 (Mininet)
<img width="854" height="492" alt="image" src="https://github.com/user-attachments/assets/a01aa8a8-e8e2-493a-b899-50e2d16b7980" />
<img width="591" height="497" alt="image" src="https://github.com/user-attachments/assets/6ead7a19-c2dc-4f16-ad4c-659410de8709" />





---


## 🧠 Conclusion

This project demonstrates how an SDN controller centrally manages ARP communication, reducing broadcast traffic and improving network control.

---

## 🎓 Viva Points

* ARP converts IP to MAC address
* Packet-In sends unknown packets to controller
* Controller performs ARP handling
* SDN provides centralized control

---

## 📌 Author

Abhishek PH
