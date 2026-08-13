# arp_poisoning_detector.py
import subprocess
import re

def get_arp_table():
    # Run the arp -a command
    result = subprocess.run(['arp', '-a'], capture_output=True, text=True)
    return result.stdout

def parse_arp_table(arp_output):
    # Regular expression to match IP and MAC addresses
    arp_regex = re.compile(r'(\d+\.\d+\.\d+\.\d+)\s+([0-9A-Fa-f:-]+)\s+(\w+)')
    arp_entries = arp_regex.findall(arp_output)
    return arp_entries

def check_for_arp_poisoning(arp_entries):
    ip_mac_map = {}
    arp_poisoning_detected = False
    for ip, mac, entry_type in arp_entries:
        network_id = entry_type
        interface_ip = ip
        mac_regex = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
        if not entry_type.startswith('Ox'):
            # This line in arp_entries is not an interface
            network_id = None
            interface_ip = None
        if not mac_regex.match(mac):
            continue
        # else:
        #     print(mac, ip)
        if ip in ip_mac_map:
            if ip_mac_map[ip] != mac:
                print(f"Warning: Potential ARP poisoning detected for IP {ip}!")
                print(f"MAC addresses: {ip_mac_map[ip]} and {mac}")
                print(f"Interface IP: {interface_ip} Network ID: {network_id}")
                arp_poisoning_detected = True
        else:
            ip_mac_map[ip] = mac
    if not arp_poisoning_detected:
        print("Info: ARP poisoning not detected.")
    return arp_poisoning_detected
    
if __name__ == "__main__":
    arp_output = get_arp_table()
    arp_entries = parse_arp_table(arp_output)
    check_for_arp_poisoning(arp_entries)
