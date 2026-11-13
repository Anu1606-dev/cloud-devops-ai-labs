import ipaddress

vpc = ipaddress.ip_network("10.20.0.0/16")

subnets = {
    "public-a": ipaddress.ip_network("10.20.1.0/24"),
    "public-b": ipaddress.ip_network("10.20.2.0/24"),
    "private-app-a": ipaddress.ip_network("10.20.11.0/24"),
    "private-app-b": ipaddress.ip_network("10.20.12.0/24"),
    "private-db-a": ipaddress.ip_network("10.20.21.0/24"),
    "private-db-b": ipaddress.ip_network("10.20.22.0/24"),
}

print(f"VPC CIDR: {vpc}")
print(f"VPC total IPv4 addresses: {vpc.num_addresses}")
print()

for name, subnet in subnets.items():
    if not subnet.subnet_of(vpc):
        raise ValueError(f"{name} is outside the VPC")

    print(
        f"{name}: {subnet} | "
        f"Total: {subnet.num_addresses} | "
        f"AWS usable: {subnet.num_addresses - 5} | "
        "Inside VPC: YES"
    )

items = list(subnets.items())

for i in range(len(items)):
    for j in range(i + 1, len(items)):
        name_a, net_a = items[i]
        name_b, net_b = items[j]

        if net_a.overlaps(net_b):
            raise ValueError(f"Overlap: {name_a} and {name_b}")

print("\nSUCCESS: All subnet ranges are inside the VPC and non-overlapping.")
