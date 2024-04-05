import pytest
from pymongo import MongoClient

from ...Connection.mongodb_connector import MongoDBManager
from ...schemas.config import settings


class TestMongoDBManager:
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.db_name = "test_db"
        self.collection_name = "test_collection"
        self.uri = settings.mongodb_uri
        self.db_manager = MongoDBManager(self.db_name, self.collection_name, self.uri)
        self.client = MongoClient(self.uri)
        yield
        self.client.drop_database(self.db_name)

    def test_insert_item(self):
        item = {"name": "Test-value", "value": 123}
        item_id = self.db_manager.insert_item(item)
        assert item_id is not None
        assert self.client[self.db_name][self.collection_name].find_one({"_id": item_id})

    def test_get_item(self):
        item = {"name": "Test-value", "value": 123}
        item_id = self.db_manager.insert_item(item)
        retrieved_item = self.db_manager.get_item({"_id": item_id})
        assert retrieved_item == item

    def test_update_item(self):
        item = {"name": "Test-value", "value": 123}
        item_id = self.db_manager.insert_item(item)
        new_values = {"name": "New Name", "new_field": 1}
        self.db_manager.update_item({"_id": item_id}, new_values)
        updated_item = self.db_manager.get_item({"_id": item_id})
        assert updated_item["name"] == "New Name"
        assert updated_item["new_field"] == 1

    # def test_delete_item(self):
    #     item = {"name": "Test", "value": 123}
    #     item_id = self.db_manager.insert_item(item)
    #     self.db_manager.delete_item({"_id": item_id})
    #     deleted_item = self.db_manager.get_item({"_id": item_id})
    #     assert deleted_item is None