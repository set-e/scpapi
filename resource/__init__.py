from scpapi import Client


class Resource:
    def __init__(self, client: Client):
        self.client = client