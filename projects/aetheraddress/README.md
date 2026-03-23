# AetherAddress - IP Address Validator

A simple command-line tool for validating IPv4 addresses.

## Usage

Run `python main.py` and enter an IP address when prompted.

## Example

```
$ python main.py
Enter an IPv4 address: 192.168.1.1
192.168.1.1 is a valid IPv4 address.
```

```
$ python main.py
Enter an IPv4 address: 256.256.256.256
256.256.256.256 is NOT a valid IPv4 address.
```

```
$ python main.py
Enter an IPv4 address: not.an.ip.address
not.an.ip.address is NOT a valid IPv4 address.
```
