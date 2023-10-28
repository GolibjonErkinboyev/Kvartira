from flat import Flat
from client import Client

class Manager:
    flats = None
    clients = None

    @staticmethod
    def newFlat(code, area):
        flat = Flat(code, area)
        Manager.flats.append(flat)
        return flat

    @staticmethod
    def newClient(firstname, lastname, id):
        client = Client(firstname, lastname, id)
        Manager.clients.append(client)
        return client

    @staticmethod
    def getClient(id):
        for client in Manager.clients:
            if client.getID() == id:
                return client
        return None

    @staticmethod
    def getClients():
        return Manager.clients
