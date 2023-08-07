import socket

def scan_ports(target_host, port_list):
    print(f"Scanning ports on {target_host}...")
    
    for port in port_list:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((target_host, port))

            if result == 0:
                print(f"Port {port}: Open")
            else:
                print(f"Port {port}: Closed")
                
            sock.close()

        except socket.error:
            print(f"Could not connect to {target_host}:{port}")
    
    print(f"Port scanning finished!")

target_host = "127.0.0.1"
port_list = [80, 22, 5432]

scan_ports(target_host, port_list)