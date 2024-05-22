import pymongo
from faker import Faker
import random
from datetime import datetime

# Initialize the Faker library
fake = Faker()

# MongoDB connection settings
MONGO_URI = 'mongodb://localhost:27017/'
DATABASE_NAME = 'iot_tasks'
COLLECTION_NAME = 'iot_app_device'

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Function to generate fake IoT device data
def generate_device_data():
    return {
        'device_id': fake.random_int(min=0, max=500),
        'device_type': random.choice(['air', 'energy', 'water']),
        #'temperature': round(random.uniform(20.0, 30.0), 2),
        #'humidity': round(random.uniform(30.0, 70.0), 2),
        #'status': random.choice(['active', 'inactive', 'faulty']),
        'timestamp': datetime.utcnow(),
        'data': fake.random_int(min=0, max=100),
        
    }

# Generate and insert fake data into MongoDB
def insert_fake_data(n):
    for _ in range(n):
        data = generate_device_data()
        collection.insert_one(data)
        print(f"Inserted data: {data}")

# Number of fake records to generate
NUM_RECORDS = 10

# Insert the fake data
insert_fake_data(NUM_RECORDS)

# Close the MongoDB connection
client.close()
