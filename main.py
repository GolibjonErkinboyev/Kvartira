from manager import Manager

flat1 = Manager.newFlat("A101", 80)
flat1.setTariffs(1000, 1500, 2000)

print(f"Flat Code: {flat1.getCode()}")
print(f"Flat Dimension: {flat1.getDimension()}")


client1 = Manager.newClient("G'olibjon", "Erkinboyev", 1)

print(f"Client Name: {client1.getName()}")
print(f"Client Surname: {client1.getSurname()}")
print(f"Client ID: {client1.getID()}")

client2 = Manager.getClient(1)
print(f"Client Name: {client2.getName()}")
print(f"Client Surname: {client2.getSurname()}")
print(f"Client ID: {client2.getID()}")

clients = Manager.getClients()
for client in clients:
    print(f"Client Name: {client.getName()}")
    print(f"Client Surname: {client.getSurname()}")
    print(f"Client ID: {client.getID()}")