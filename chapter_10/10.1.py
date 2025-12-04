with open("chapter_10\\module_text\\pi_digits.txt") as file_object:
    contents = file_object.read()
print(contents)
print(contents.rstrip())

for line in contents:
    print(line)
