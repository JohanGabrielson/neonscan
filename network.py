import ipaddress

def get_hosts(target):
    try:
        network = ipaddress.ip_network(target, strict=False)
        return list(network.hosts())
    except ValueError:
        return [ipaddress.ip_address(target)]
