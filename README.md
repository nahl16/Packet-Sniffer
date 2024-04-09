```markdown
```
# Packet Sniffer Tool

This tool is a basic packet sniffer implemented in Python using the `scapy` library. It captures and displays relevant information from network packets, including source and destination IP addresses, protocols, and raw payload data.

## Features

- Captures packets on a specified network interface.
- Displays source and destination IP addresses.
- Shows the protocol used (e.g., TCP, UDP).
- Outputs raw payload data if available.

## Requirements

- Python 3.x
- `scapy` library (`pip install scapy`)

## Usage

1. **Install Dependencies**:
   - Make sure you have Python 3.x installed.
   - Install the required `scapy` library using pip:
     ```bash
     pip install scapy
     ```

2. **Run the Packet Sniffer**:
   - Clone or download the `packet_sniffer.py` script.
   - Open a terminal or command prompt.
   - Navigate to the directory containing `packet_sniffer.py`.
   - Run the script by executing the following command:
     ```bash
     python packet_sniffer.py
     ```

3. **Provide Network Interface**:
   - Enter the name of the network interface (e.g., `Ethernet`, `Wi-Fi`) when prompted:
     ```
     Enter the interface to sniff on (e.g., Ethernet, Wi-Fi): Ethernet
     ```

4. **View Captured Packets**:
   - The script will start capturing packets on the specified interface.
   - Each captured packet will display source IP, destination IP, protocol, and raw payload data (if available) in the console output.

## Disclaimer

This tool is intended for educational purposes only. Do not use it for any unauthorized or illegal activity. Always respect privacy and network usage policies.

```
