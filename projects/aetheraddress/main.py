import sys

def is_valid_ipv4_octet(octet):
    try:
        octet_int = int(octet)
        return 0 <= octet_int <= 255
    except ValueError:
        return False

def is_valid_ipv4_address(ip_address):
    octets = ip_address.split('.')
    if len(octets) != 4:
        return False
    for octet in octets:
        if not is_valid_ipv4_octet(octet):
            return False
    return True

def main():
    try:
        ip_address = input("Enter an IPv4 address: ")
    except KeyboardInterrupt:
        print("\nExiting.")
        sys.exit(0)

    if is_valid_ipv4_address(ip_address):
        print(f"{ip_address} is a valid IPv4 address.")
    else:
        print(f"{ip_address} is NOT a valid IPv4 address.")

if __name__ == "__main__":
    main()
