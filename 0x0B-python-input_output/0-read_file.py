def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8") as myfile:
        print(myfile.read(), end="")
