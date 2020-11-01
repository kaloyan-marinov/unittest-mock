# Setup

```
$ python3 --version
Python 3.8.3
$ python3 -m venv venv
$ source venv/bin/activate

(venv) $ pip install --upgrade pip
(venv) $ pip install -r requirements.txt
```

# Example 1 is a handcrafted example

To run all unit tests:
```
(venv) $ python -m unittest discover -v tests/
```
To run a specific unit test:
```
(venv) $ python -m unittest tests/test_ex_1_m_2.py
(venv) $ python -m unittest tests.test_ex_1_m_2
```

# The remaining examples are based on the following talk: (Lisa Roach - Demystifying the Patch Function - PyCon 2018)

`patch` is the main mocking mechanism that the Python `unittest` library has.

It temporarily replaces a target object/attribute with a different object. By default, that different object is a `MagicMock`.

You should mock/patch when you don't want to actually call an object. Examples of things I might not want to actually call when are used in a test:
- writing to a database (e.g. a production database)
- system calls (e.g. deleting files from your filesystem)

What makes this so confusing?
1. Identifying the target
    - It must be importable from your test file.
    - **Patch where the object is used** (rather than where the object is defined).
2. Multiple ways to call

Down the rabbit hole:
1. https://docs.python.org/3.8/library/functions.html#dir
2. https://docs.python.org/3.8/library/functions.html#locals
3. https://stackoverflow.com/questions/12918189/any-difference-between-dir-and-locals-in-python
4. https://stackoverflow.com/questions/9085450/symbol-table-in-python
