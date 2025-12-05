user = input("Enter your name: ")

with open("chapter_10\\module_text\\guest.txt", "w") as file_object:
    file_object.write(user)
