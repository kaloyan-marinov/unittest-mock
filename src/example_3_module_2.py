from src.example_3_module_1 import db_write


def foo():
    x = db_write()
    return x


if __name__ == '__main__':
    print()
    # print(dir() == sorted(locals().keys()))
    # print(locals())
    print(f"The following have been loaded into this module's locals: {dir()}")
    print('db_write' in dir())

    print()
    result = foo()
    print(f'the result is {result}')

