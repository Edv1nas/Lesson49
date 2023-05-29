from user_input import update_db, create_db

print("Welcome to DB generator")
while True:
    choice = input(
        "Please choose an option from the list:\n1. Create DB\n2. Update DB\n3. Exit\n")
    if choice == "1":
        create_db()
    elif choice == "2":
        update_db()
    elif choice == "3":
        print("Have a great day!")
        break
    else:
        print("Invalid input")
