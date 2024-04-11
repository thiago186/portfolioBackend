from bson.objectid import ObjectId

from pydantic import BaseModel
from pymongo import MongoClient

from schemas.config import settings
from schemas.exceptions import ObjectIdException

class MongoDBManager:
    def __init__(self, db_name, collection_name, uri):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_item(self, item):
        return self.collection.insert_one(item).inserted_id

    def get_item(self, query_dict):
        if '_id' in query_dict:
            query_dict["_id"] = convert_to_object_id(query_dict["_id"])

        try:
            item = self.collection.find_one(query_dict)
        except: 
            return {}
        
        item["_id"] = str(item["_id"])
        return item
    
    def get_all_items(self):
        all_items = []
        for item in self.collection.find(): 
            item["_id"] = str(item["_id"])
            all_items.append(item)
        return all_items

    def update_item(self, query_dict, update_values):
        if '_id' in query_dict:
            query_dict["_id"] = convert_to_object_id(query_dict["_id"])

        result = self.collection.update_one(query_dict, {"$set": update_values})
        return result
    
    def delete_item(self, query_dict):
        if '_id' in query_dict:
            query_dict["_id"] = convert_to_object_id(query_dict["_id"])
            
        return self.collection.delete_one(query_dict)

def convert_to_object_id(id):
    print(f"received id: {id}")
    try:
        return ObjectId(str(id))
    except Exception as e:
        print(e)
        raise ObjectIdException()

db_manager = MongoDBManager("thiagoapp", "projects", uri=settings.mongodb_uri)    

# Exemplo de uso
if __name__ == "__main__":
    
    id = '66105bc6651ac246615b1892'
    query_dict = {"_id": id}
    item = db_manager.get_item(query_dict)

    items = db_manager.get_all_items()
    print(items)
    # Inserir
    item_id = db_manager.insert_item({"name": "Test", "value": 123})
    print(f"Inserted item ID: {item_id}")

    # Buscar
    query_dict = {"name": "Test"}
    item = db_manager.get_item(query_dict)
    print(f"Item: {item}")

    # Atualizar
    new_values = {
        "new_field":  1,
        "name": "New Name"
        }
    db_manager.update_item(query_dict, new_values)
    updated_item = db_manager.get_item(item_id)
    print(f"Updated item: {updated_item}")

    # Remover
    db_manager.delete_item(item_id)
    deleted_item = db_manager.get_item(item_id)
    print(f"Deleted item: {deleted_item}")
