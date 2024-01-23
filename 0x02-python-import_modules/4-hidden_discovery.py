#!/usr/bin/python3
if __name__ == "__main__":
    # import
    import hidden_4
    # iterable
    for name in dir(hidden_4):
        if name[0] != '_' and name[1] != '_':
            print("{}".format(name))
