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
