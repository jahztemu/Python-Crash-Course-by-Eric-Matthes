while True:
    user = input("Enter your name (or 'quit' to exit): ")
    print(f"Thank you {user} for your visit!")
    if user == "quit":
        break
    else:
        with open("chapter_10\\module_text\\guest.txt", "a") as file_object:
            file_object.write(user + "\n")
