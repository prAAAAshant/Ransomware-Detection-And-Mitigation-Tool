import subprocess

# Function to isolate the system using iptables
def isolate_system(ip_address):
    try:
        subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip_address, "-j", "DROP"])
        subprocess.run(["sudo", "iptables", "-A", "OUTPUT", "-d", ip_address, "-j", "DROP"])
        print(f"System with IP {ip_address} has been isolated.")
    except Exception as e:
        print(f"Error isolating system: {e}")