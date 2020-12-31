

def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def increment(x):
    return x+1

# usually test is in separate file


def test_add():
    assert add(1, 2) == 3


def test_subtract():
    assert subtract(1, 2) == -1


def test_increment():
    assert increment(3) == 4
