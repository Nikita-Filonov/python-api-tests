from enum import Enum


class APIRoutes(str, Enum):
    CARDS = "/fakebank/cards"
    CLIENTS = "/fakebank/clients"
    OPERATIONS = "/fakebank/accounts"
    STATEMENTS = "/fakebank/statements"
    NOTIFICATIONS = "/fakebank/notifications"

    def __str__(self):
        return self.value
