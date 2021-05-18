def add():
    i = 1
    while i < 66:
        print(str(i)+".", end="\t")
        if i % 5 == 0:
            print()
        i += 1


if __name__ == '__main__':
    add()
