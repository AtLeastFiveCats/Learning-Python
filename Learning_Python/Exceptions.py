while True:
    try:
        file = input("Enter a file name. ")
        with open(file) as f:
            print(f.read())
            break
    except FileNotFoundError:
        print("Not Found")