while True:
    user = input("Enter your name (or 'quit' to exit): ")
    print(f"Thank you {user} for participating in our poll!")
    if user == "quit":
        break
    else:
        question = input("Why do you like programming? ")
        with open("chapter_10\\module_text\\guest.txt", "a") as file_object:
            file_object.write(f"Name: {user}, Answer: {question}\n")
