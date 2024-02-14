for first in range(9):
    for second in range(first + 1, 10):
        if first != 8:
            print("{}{}".format(first, second), end=", ")
        else:
            print("{}{}".format(first, second))
