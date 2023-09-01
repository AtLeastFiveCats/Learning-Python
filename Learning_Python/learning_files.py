with open("files/new_file.txt", "w") as f:
    f.write("Hello World! \nThis is a new line!")
with open("files/new_file.txt", "a") as f:
    f.write("\nPython is new and exciting!")
with open("files/new_file.txt") as f:
    content = f.read()
print(content)