path = "chapter_10\\module_text\\text.txt"

with open(path) as file_object:
    contents = file_object.read()

print(contents.count("the"))
print(contents.count("The"))
