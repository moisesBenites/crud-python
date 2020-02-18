import csv

from clients.models import ClientModel


class ClientService:
    def __init__(self, table_name):
        self.table_name = table_name


    def create_client(self, client):
        with open(self.table_name, mode='w') as f:
            writer = csv.DictWriter(f, fieldnames=ClientModel.schema())
            writer.writerow(client.to_dict())

