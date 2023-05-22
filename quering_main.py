"""Task Nr.1 : Create the CLI application, that would populate MongoDB database with random data. The input should ask for :
- database name
- collection name
- field name with types (string, number, date string objects etc.) with range of values (lets say field name = price , then value is number (float, int) which is random number from a(min) to b(max) )
- number o documents to create."""

# pylint: disable-all

import random
import string
from datetime import datetime, timedelta
from pymongo import MongoClient
from tqdm import tqdm


class DbPopulator:
    def __init__(self):
        self.client = MongoClient()

    def generate_random_string(self, min_lenght: int, max_lenght: int) -> str:
        length = random.randint(min_lenght, max_lenght)
        letters = string.ascii_letters
        return "".join(random.choice(letters) for letter in range(length))

    def generate_random_number(self, min_value: int, max_value: int) -> int:
        return random.randint(min_value, max_value)

    def generate_random_date(self, min_value: int, max_value: int) -> datetime:
        start_date = datetime.strptime(min_value, "%Y-%m-%d")
        end_date = datetime.strptime(max_value, "%Y-%m-%d")
        time_diff = (end_date - start_date).days
        random_days = random.randint(0, time_diff)
        return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

    def generate_random_data(self, field_type, min_value, max_value):
        if field_type == "string":
            return self.generate_random_string(int(min_value), int(max_value))
        elif field_type == "number":
            return self.generate_random_number(int(min_value), int(max_value))
        elif field_type == "date":
            return self.generate_random_date(min_value, max_value)

    def populate_database(self, db_name, collection_name, field_name, field_type, min_value, max_value, num_documents):
        db = self.client[db_name]
        collection = db[collection_name]

        with tqdm(total=num_documents, desc="Inserting documents") as pbar:
            for number in range(num_documents):
                document = {field_name: self.generate_random_data(
                    field_type, min_value, max_value)}
                collection.insert_one(document)
                pbar.update(1)

        print("Data insertion completed.")


if __name__ == "__main__":
    populator = DbPopulator()

    db_name = input("Enter the database name: ")
    collection_name = input("Enter the collection name: ")
    field_name = input("Enter the field name: ")
    field_type = input("Enter the field type (string, number, date): ")
    min_value = input("Enter the minimum value: ")
    max_value = input("Enter the maximum value: ")
    num_documents = int(input("Enter the number of documents to create: "))

    populator.populate_database(
        db_name, collection_name, field_name, field_type, min_value, max_value, num_documents)
