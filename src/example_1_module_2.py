import sys

def print_runtime_info():
    print()
    print(f'running the following module as an executable script: {sys.argv[0]}')

    print()
    for p in sys.path:
        print(p)


# If you understand the answer on
# https://stackoverflow.com/questions/57078689/module-not-found-error-no-module-named-src ,
# then uncommenting the following code-block clarifies why:
# (a) running `python src/module_2.py` crashes with a
#     `ModuleNotFoundError: No module named 'src'`, whereas
# (b) running `$ PYTHONPATH=./ python src/module_2.py` runs successfully.
# fmt: off
'''
print_runtime_info()
'''
# fmf: on

from numpy.random import randint
from src.example_1_module_1 import CHARACTER


def build_str_of_random_length(character):
    random_count = randint(3, 10)
    return random_count * character


def main():
    print_runtime_info()
    
    i_s_pairs = list()
    for i in range(10):
        s = build_str_of_random_length(CHARACTER)
        i_s_pairs.append((i, s))

    print()
    for i, s in i_s_pairs:
        print(f'iteration {i} generate the following random-length string: {s}')


if __name__ == '__main__':
    main()

    import os
    print(os.environ.get('PYTHONHOME'))
    print(os.environ.get('PYTHONPATH'))

