"""Task Nr.1 : Create the CLI application, that would populate MongoDB database with random data. The input should ask for :
- database name
- collection name
- field name with types (string, number, date string objects etc.) with range of values (lets say field name = price , then value is number (float, int) which is random number from a(min) to b(max) )
- number o documents to create."""

# pylint: disable-all

import random
from datetime import datetime, timedelta
from pymongo import MongoClient
from tqdm import tqdm
from wonderwords import RandomWord


class DbPopulator:
    def __init__(self):
        self.client = MongoClient()

    def generate_random_words(self, min_lenght: int, max_lenght: int) -> str:
        rw = RandomWord()
        generated_words = rw.random_words(
            word_min_length=min_lenght, word_max_length=max_lenght)
        return " ".join(generated_words)

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
            return self.generate_random_words(int(min_value), int(max_value))
        elif field_type == "number":
            return self.generate_random_number(int(min_value), int(max_value))
        elif field_type == "date":
            return self.generate_random_date(min_value, max_value)

#     def populate_database(self, db_name, collection_name, field_name, field_type, min_value, max_value, num_documents):
#         db = self.client[db_name]
#         collection = db[collection_name]

#         with tqdm(total=num_documents, desc="Inserting documents") as pbar:
#             for x in range(num_documents):
#                 document = {field_name: self.generate_random_data(
#                     field_type, min_value, max_value)}
#                 collection.insert_one(document)
#                 pbar.update(1)

#         print("Data insertion completed.")


# if __name__ == "__main__":
#     populator = DbPopulator()

#     db_name = input("Enter the database name: ")
#     collection_name = input("Enter the collection name: ")
#     field_name = input("Enter the field name: ")
#     field_type = input("Enter the field type (string, number, date): ")
#     min_value = input("Enter the minimum value: ")
#     max_value = input("Enter the maximum value: ")
#     num_documents = int(input("Enter the number of documents to create: "))

#     populator.populate_database(
#         db_name, collection_name, field_name, field_type, min_value, max_value, num_documents)

    def populate_database(self, db_name, collection_name, fields_info, num_documents):
        db = self.client[db_name]
        collection = db[collection_name]

        with tqdm(total=num_documents, desc="Inserting documents") as pbar:
            for number in range(num_documents):
                document = {}
                for field_info in fields_info:
                    field_name, field_type, min_value, max_value = field_info
                    document[field_name] = self.generate_random_data(
                        field_type, min_value, max_value)
                collection.insert_one(document)
                pbar.update(1)

        print("Data insertion completed.")


if __name__ == "__main__":
    populator = DbPopulator()

    db_name = input("Enter the database name: ")
    collection_name = input("Enter the collection name: ")
    num_fields = int(input("Enter the number of fields: "))

    fields_info = []

    for i in range(num_fields):
        field_name = input(f"Enter the field name {i+1}: ")
        field_type = input(
            f"Enter the field type for {field_name} (string, number, date): ")
        min_value = input(f"Enter the minimum value for {field_name}: ")
        max_value = input(f"Enter the maximum value for {field_name}: ")

        fields_info.append((field_name, field_type, min_value, max_value))

    num_documents = int(input("Enter the number of documents to create: "))

    populator.populate_database(
        db_name, collection_name, fields_info, num_documents)
