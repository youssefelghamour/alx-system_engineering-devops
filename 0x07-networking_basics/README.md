# 0x07. Networking basics #0

This project delves into the fundamentals of networking, covering the OSI model, types of networks, MAC and IP addresses, and TCP/UDP. The tasks require creating Bash scripts that demonstrate an understanding of these networking concepts.

## Project Files

| Filename                             | Description                                                |
| ------------------------------------ | ---------------------------------------------------------- |
| `0-OSI_model`                        | Describes the OSI model and its organization.               |
| `1-types_of_network`                  | Covers LAN, WAN, and Internet networks.                    |
| `2-MAC_and_IP_address`               | Explains MAC and IP addresses.                              |
| `3-UDP_and_TCP`                      | Details the characteristics of UDP and TCP protocols.      |
| `4-TCP_and_UDP_ports`                | Displays listening ports and their associated processes.   |
| `5-is_the_host_on_the_network`       | Pings an IP address to check network connectivity.         |

## Task 0: OSI Model

### Questions:

- What is the OSI model?
  - 1. Set of specifications that network hardware manufacturers must respect
  - 2. The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology
  - 3. The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology

- How is the OSI model organized?
  - 1. Alphabetically
  - 2. From the lowest to the highest level
  - 3. Randomly

## Task 1: Types of Network

### Questions:

- What type of network is a computer in a local connected to?
  - 1. Internet
  - 2. WAN
  - 3. LAN

- What type of network could connect an office in one building to another office a few streets away?
  - 1. Internet
  - 2. WAN
  - 3. LAN

- What network do you use when browsing www.google.com from your smartphone (not connected to WiFi)?
  - 1. Internet
  - 2. WAN
  - 3. LAN

## Task 2: MAC and IP Address

### Questions:

- What is a MAC address?
  - 1. The name of a network interface
  - 2. The unique identifier of a network interface
  - 3. A network interface

- What is an IP address?
  - 1. To devices connected to a network what a postal address is to houses
  - 2. The unique identifier of a network interface
  - 3. A number that network devices use to connect to networks

## Task 3: UDP and TCP

### Questions:

- Which statement is correct for the TCP box?
  - 1. It is a protocol that is transferring data in a slow way but surely
  - 2. It is a protocol that is transferring data in a fast way and might lose data along the process

- Which statement is correct for the UDP box?
  - 1. It is a protocol that is transferring data in a slow way but surely
  - 2. It is a protocol that is transferring data in a fast way and might lose data along the process

- Which statement is correct for the TCP worker?
  - 1. Have you received boxes x, y, z?
  - 2. May I increase the rate at which I am sending you boxes?

## Task 4: TCP and UDP Ports

### Task Description:

Write a Bash script that displays listening ports and their associated processes.

## Task 5: Is the Host on the Network

### Task Description:

Write a Bash script that pings an IP address passed as an argument.

Requirements:
- Accepts a string as an argument
- Displays Usage: 5-is_the_host_on_the_network {IP_ADDRESS} if no argument passed
- Pings the IP 5 times

Example:

```bash
./5-is_the_host_on_the_network 8.8.8.8
