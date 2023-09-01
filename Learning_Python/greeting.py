def greets():
    with open("files\greet.txt", "w") as f:
        f.write("Hello Friend!")
    with open("files\greet.txt") as f:
        intro = f.read()
        print(intro)

greets()