"""Task Nr.1 : Create the CLI application, that would populate MongoDB database with random data. The input should ask for :
- database name
- collection name
- field name with types (string, number, date string objects etc.) with range of values (lets say field name = price , then value is number (float, int) which is random number from a(min) to b(max) )
- number o documents to create."""

from wonderwords import RandomWord
from tqdm import tqdm
from pymongo import MongoClient
from datetime import datetime, timedelta
import random
# pylint: disable-all


def get_db(db_name: str):
    mongodb_host = "localhost"
    mongodb_port = 27017
    client = MongoClient(mongodb_host, mongodb_port)
    return client[db_name]


def generate_random_words(min_lenght: int, max_lenght: int) -> str:
    rw = RandomWord()
    generated_words = rw.random_words(
        word_min_length=min_lenght, word_max_length=max_lenght)
    return " ".join(generated_words)


def generate_random_number(min_value: int, max_value: int) -> int:
    return random.randint(min_value, max_value)


def generate_random_date(min_value: int, max_value: int) -> datetime:
    start_date = datetime.strptime(min_value, "%Y-%m-%d")
    end_date = datetime.strptime(max_value, "%Y-%m-%d")
    time_diff = (end_date - start_date).days
    random_days = random.randint(0, time_diff)
    formatted_date = (
        start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")
    return formatted_date


def generate_random_data(field_type, min_value, max_value):
    if field_type == "string":
        return generate_random_words(int(min_value), int(max_value))
    elif field_type == "number":
        return generate_random_number(int(min_value), int(max_value))
    elif field_type == "date":
        return generate_random_date(min_value, max_value)


def populate_database(db_name, collection_name, field_name, field_type, min_value, max_value, num_documents):
    db = get_db(db_name)
    collection = db[collection_name]

    with tqdm(total=num_documents, desc="Inserting documents") as pbar:
        for x in range(num_documents):
            document = {field_name: generate_random_data(
                field_type, min_value, max_value)}
            collection.insert_one(document)
            pbar.update(1)

    print("Data insertion completed.")


def update_collection(
        db_name, collection_name, field_name, field_type, min_value, max_value):
    db = get_db(db_name)
    collection = db[collection_name]

    for document in collection.find():
        collection.update_one(
            {"_id": document["_id"]},
            {
                "$set": {
                    field_name: generate_random_data(
                        field_type, min_value, max_value
                    )
                }
            },
            upsert=False,
            array_filters=None,
        )
    print("Data updated.")
