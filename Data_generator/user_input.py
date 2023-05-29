from main import populate_database, update_collection


def create_db():
    db_name = input("Enter the database name: ")
    collection_name = input("Enter the collection name: ")
    field_name = input("Enter the field name: ")
    field_type = input("Enter the field type (string, number, date): ")
    min_value = input("Enter the minimum value: ")
    max_value = input("Enter the maximum value: ")
    num_documents = int(input("Enter the number of documents to create: "))
    populate_database(db_name, collection_name, field_name,
                      field_type, min_value, max_value, num_documents)


def update_db():
    db_name = input("Enter the database name: ")
    collection_name = input("Enter the collection name: ")
    field_name = input("Enter the field name: ")
    field_type = input("Enter the field type (string, number, date): ")
    min_value = input("Enter the minimum value: ")
    max_value = input("Enter the maximum value: ")
    update_collection(db_name, collection_name, field_name,
                      field_type, min_value, max_value)
