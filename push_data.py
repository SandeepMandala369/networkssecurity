import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(str(e), sys)
        

    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            print(f"DataFrame Loaded:\n{data.head()}")  # ✅ Debugging print
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            print(f"Converted JSON Records (First 5): {records[:5]}")  # ✅ Print first 5 records
            return records
        except Exception as e:
            raise NetworkSecurityException(str(e), sys)
        
    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)  #  Fix: Added SSL certificate
            db = self.mongo_client[self.database]  #  Fix: Used `db` variable
            collection = db[self.collection]
            collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(str(e), sys)

if __name__ == "__main__":
    FILE_PATH = r"Network_Data\phisingData.csv"  #  Fix: Use raw string
    DATABASE = "SANDYAI"
    collection = "networkdata"  # Fix: Lowercase variable

    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    
    print(records)  # Fix: Print records before inserting
    
    if records: 
        no_of_records = networkobj.insert_data_mongodb(records, DATABASE, collection)
        print(f"No. of records inserted: {no_of_records}")
    else:
        print("No records found in CSV.")
