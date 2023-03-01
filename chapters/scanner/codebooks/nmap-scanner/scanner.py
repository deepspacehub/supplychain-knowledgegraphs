import nmap

# Set up Nmap scanner
scanner = nmap.PortScanner()

# Define target IP range
target = '192.168.1.1/24'

# Perform Nmap scan
scanner.scan(hosts=target, arguments='-sS -sV')

# Iterate over scanned hosts
for host in scanner.all_hosts():
    # Print host and open ports
    print(f'Host: {host}')
    for port in scanner[host]['tcp']:
        state = scanner[host]['tcp'][port]['state']
        service = scanner[host]['tcp'][port]['name']
        print(f'  Port {port} ({service}): {state}')