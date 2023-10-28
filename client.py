
class Client:
    def init(self, firstname, lastname, id):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id

    def getName(self):
        return self.firstname

    def getSurname(self):
        return self.lastname

    def getID(self):
        return self.id
