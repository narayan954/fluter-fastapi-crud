from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router as book_router

config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to MongoDB")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
    print("Disconnected from MongoDB")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/users")
def read_users():
    users_collection = app.database.get_collection("users")
    users = users_collection.find()
    return users

@app.post("/users")
def create_user():
    user = {"name": "John Doe", "age": 30}
    users_collection = app.database.get_collection("users")
    result = users_collection.insert_one(user)
    return {"id": str(result.inserted_id)}

@app.get("/users/{user_id}")
def read_user(user_id: str):
    users_collection = app.database.get_collection("users")
    user = users_collection.find_one({"_id": "65993e05db7bd1df2de42943"})
    return user

@app.put("/users/{user_id}")
def update_user(user_id: str):
    users_collection = app.database.get_collection("users")
    result = users_collection.update_one({"_id": ObjectId(user_id )}, {"$set": {"age": 25}})
    return {"modified_count": result.modified_count}

@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    users_collection = app.database.get_collection("users")
    result = users_collection.delete_one({"_id": ObjectId(user_id)})
    return {"deleted_count": result.deleted_count}

app.include_router(book_router, tags=["books"], prefix="/book")