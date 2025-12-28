from pymongo import MongoClient


class MongoDB():
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["FındıkTakip"]
        self.users = self.db["users"]
        self.customers = self.db["customers"]
        

            

    def close_connection(self):
        self.client.close()    

