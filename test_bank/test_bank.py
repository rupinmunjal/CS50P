from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0

def test_h():
    assert value("hi") == 20
    assert value("Hey") == 20

def test_else():
    assert value("rupin") == 100
