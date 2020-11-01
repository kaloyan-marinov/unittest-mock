def foo():
    x = db_write()
    return x


def db_write():
    print('writing to the database')
    return 1

