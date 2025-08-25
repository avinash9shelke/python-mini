import ipaddress
def validate_ip(ip):
    try:
        ip_obj = ipaddress.ip_address(ip)
        if isinstance(ip_obj, ipaddress.IPv4Address):
            return f"{ip} is a valid IPv4 address."
        elif isinstance(ip_obj, ipaddress.IPv6Address):
            return f"{ip} is a valid IPv6 address."
    except ValueError:
        return f"{ip} is not a valid IP address."

print(f"Given ip address ${validate_ip("192.168.0.1")}");
print(f"Given ip address ${validate_ip("256.256.256.256")}");
print(f"Given ip address ${validate_ip("2001:0db8:85a3:0000:0000:8a2e:0370:7334")}");
print(f"Given ip address ${validate_ip("2001:db8::1")}");
print(f"Given ip address ${validate_ip("not.an.ip.address")}");