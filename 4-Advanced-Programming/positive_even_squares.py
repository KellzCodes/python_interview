def positive_even_squares(*args):
    lst = []

    for item in args:
        filtered = filter(lambda x: x > 0 and x % 2 == 0, item)
        lst.extend(filtered)

    squares = map(lambda x: x ** 2, lst)
    return list(squares)