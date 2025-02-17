from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

#MongoDB Connection URI 
MONGO_URI= "mongodb://localhost:27017"

#Create client and specify the databse 
client = AsyncIOMotorClient(MONGO_URI)
db = client['finance_app']

async def test_mongodb():
    # Insert a test document
    test_collection = db['test_collection']
    result = await test_collection.insert_one({"name": "test", "value": 123})
    print(f"Inserted document ID: {result.inserted_id}")

    # Retrieve the test document
    document = await test_collection.find_one({"name": "test"})
    print(f"Retrieved document: {document}")

# Run the test
if __name__ == "__main__":
    asyncio.run(test_mongodb())