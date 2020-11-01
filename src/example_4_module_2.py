import src.example_4_module_1


def foo():
    x = src.example_4_module_1.db_write()
    return x


if __name__ == '__main__':
    print()
    print(f"The following have been loaded into this module's locals: {dir()}")
    print(dir(src))
    print(dir(src.example_4_module_1))
    print('db_write' in dir(src.example_4_module_1))

    print()
    result = foo()
    print(f'the result is {result}')

