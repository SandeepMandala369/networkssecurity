
from pymongo.mongo_client import MongoClient

#password = Sandyman30
uri = "mongodb+srv://mcsandeepreetham:<@password>@cluster0.xy2yb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)