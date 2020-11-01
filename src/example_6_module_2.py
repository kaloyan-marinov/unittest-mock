from src.example_6_module_1 import name, birthday, address


def introduce_as_str():
    nm = name()
    bday = birthday()
    addr = address()
    return (
        f"Hello, my name is {nm}. I was born on {bday}. My address is {addr}."
    )


def introduce_as_json():
    nm = name()
    bday = birthday()
    addr = address()
    return {
        'name': nm,
        'birthday': bday,
        'address': addr,
    }


if __name__ == '__main__':
    s = introduce_as_str()
    print(s)
    d = introduce_as_json()
    print(d)

