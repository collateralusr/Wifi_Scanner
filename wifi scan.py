import socket
import subprocess

def scan_network(ip_range):
    devices = []
    ip_prefix = ip_range.rsplit('.', 1)[0]

    for i in range(1, 255):
        ip = f"{ip_prefix}.{i}"
        response = subprocess.run(["ping", "-c", "1", "-W", "1", ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if response.returncode == 0:
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except socket.herror:
                hostname = "N/A"
            devices.append({"ip": ip, "hostname": hostname})
    
    return devices
if __name__ == "__main__":
    c = input("Enter the IP range you are looking to scan: ")
    ip_range = c  # Adjust the IP range as needed

    devices = scan_network(ip_range)
    print("Connected devices:")
    for device in devices:
        print(f"IP: {device['ip']} - Hostname: {device['hostname']}")