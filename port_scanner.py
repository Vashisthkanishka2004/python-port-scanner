import socket

# Common ports dictionary
common_ports = {
    80: "HTTP",
    443: "HTTPS",
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    135: "RPC",
    139: "NetBIOS",
    445: "SMB",
    902: "VMware",
    912: "VMware Auth"
}

target = input("Enter target IP: ").strip()
print(f"\nScanning {target}...\n")

for port in range(1, 200):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        result = s.connect_ex((target, port))

        if result == 0:
            service = common_ports.get(port, "Unknown")
            print(f"[+] Port {port} is OPEN ({service})")

    except socket.error:
        print("Connection error")

    finally:
        s.close()

print("\nScan Complete!")
