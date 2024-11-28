from fuel import convert, gauge
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("1.5/2.5")

def test_correct_inputs():
    assert convert("3/4") == 75 and gauge(75) == "75%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"
