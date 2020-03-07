import csv
import os

from clients.models import ClientModel


class ClientService:
    def __init__(self, table_name):
        self.table_name = table_name


    def create_client(self, client):
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=ClientModel.schema())
            writer.writerow(client.to_dict())

    def list_clients(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=ClientModel.schema())
            return list(reader)

    
    def update_client(self, clientUpdate):
        client_list = self.list_clients()

        updateList = []
        for client in client_list:
            if client['uid'] == clientUpdate.uid:
                updateList.append(clientUpdate.to_dict())
            else:
                updateList.append(client)

        self._save_to_disk(updateList)


    def _save_to_disk(self, clients):
        tmp_table_clients = self.table_name + '.tmp'
        with open(tmp_table_clients, mode='w') as f:
            writer = csv.DictWriter(f, fieldnames=ClientModel.schema())
            writer.writerows(clients)

        os.remove(self.table_name)
        os.rename(tmp_table_clients, self.table_name)
        