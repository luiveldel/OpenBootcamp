def print_100_inv():
    list_sorted = sorted([x for x in range(1, 101)], reverse=True)
    print(list_sorted)


if '__main__' == __name__:
    print_100_inv()
