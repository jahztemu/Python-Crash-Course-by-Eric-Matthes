with open("chapter_10\\module_text\\learning_python.txt") as file_object:
    contents = file_object.read()
print(contents)

print("\n")
with open("chapter_10\\module_text\\learning_python.txt") as file_object:
    contents = file_object.readlines()
for line in contents:
    print(line)


text = ""
for value in contents:
    text += value

print(text)


for value in contents:
    texts = value.replace("Python", "C")
    print(texts.strip())
