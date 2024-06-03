import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
        addresses = re.findall(pattern, self.email_addresses)

        addresses.sort()

        return addresses