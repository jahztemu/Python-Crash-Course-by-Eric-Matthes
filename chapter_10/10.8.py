def read_text(files):
    for file in files:
        try:
            with open(file) as file_object:
                contents = file_object.readlines()
        except FileNotFoundError:
            print(f"File {file} not found")
        else:
            print(contents)


texts = [
    "chapter_10\\module_text\\cat.txt",
    "chapter_10\\module_text\\dog.txt",
    "chapter_10\\module_text\\mouse.txt",
]
read_text(texts)
