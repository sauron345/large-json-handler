import ipaddress

uniq_ip_tags = []

ips_networks = [
 "192.0.2.0/24",
 "192.0.2.8/29",
 "10.20.0.0/16",
 "10.20.30.40/32",
]

for ip_network in ips_networks:
    ip_obj = ipaddress.IPv4Address("255.255.255.255")
    subnet_obj = ipaddress.IPv4Network(ip_network, strict=False)
    print(ip_obj in subnet_obj)
