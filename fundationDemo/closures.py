def print_msg(msg):
    def printer():
        print(msg)

    return printer()


if __name__ == '__main__':
    print_msg("message!")
