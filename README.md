```markdown
```
# Packet Sniffer Tool

This tool is a basic packet sniffer implemented in Python using the `scapy` library. It captures and displays relevant information from network packets, including source and destination IP addresses, protocols, and raw payload data.

### Features

- Captures packets on a specified network interface.
- Displays source and destination IP addresses.
- Shows the protocol used (e.g., TCP, UDP).
- Outputs raw payload data if available.

### Requirements

- Python 3.x
- `scapy` library (`pip install scapy`)

### Usage

1. Install the required `scapy` library using pip:

   ```
   pip install scapy
   ```

2. Run the packet sniffer script:

   ```
   python packet_sniffer.py
   ```

3. Enter the network interface to sniff on when prompted (e.g., `eth0` for Ethernet).

4. View captured packets and their details in the console output.

### Disclaimer

This tool is intended for educational purposes only. Do not use it for any unauthorized or illegal activity. Always respect privacy and network usage policies.

### Author

Created by Nahl Imran
```
```

### Input for the Code

When running the provided Python script, you will be prompted to enter the network interface you want to sniff on. This could be an interface like `eth0` for Ethernet, `wlan0` for Wi-Fi, or any other available network interface on your system.

For example:
```
Enter the interface to sniff on (e.g., eth0): eth0
```

Replace `eth0` with the appropriate network interface name based on your system configuration. Make sure to run the script with appropriate permissions (e.g., using `sudo` on Unix-based systems) to allow packet capturing on the specified interface.
