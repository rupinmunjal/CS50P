from twttr import shorten

def test_default():
    assert shorten("") == ""

def test_upper():
    assert shorten("rUpIn") == "rpn"

def test_lower():
    assert shorten("RuPiN") == "RPN"

def test_int():
    assert shorten("100") == "100"

def test_float():
    assert shorten("100.16") == "100.16"

def test_punctuation():
    assert shorten("rpn!") == "rpn!"
