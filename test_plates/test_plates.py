from plates import is_valid

def test_check():
    # Test length constraints
    assert is_valid("AB") == True   # Minimum valid length
    assert is_valid("ABCDEF") == True  # Maximum valid length
    assert is_valid("A") == False  # Too short
    assert is_valid("ABCDEFG") == False  # Too long

    # Test alphabetic start
    assert is_valid("AB123") == True  # Valid starting with letters
    assert is_valid("12ABCD") == False  # Invalid: starts with numbers
    assert is_valid("12") == False  # Invalid: starts with numbers

    # Test alphanumeric constraint
    assert is_valid("AB123") == True  # Valid alphanumeric
    assert is_valid("AB!123") == False  # Invalid: special character
    assert is_valid("..!!") == False  # Invalid: only special characters

    # Test numbers starting properly
    assert is_valid("AB123") == True  # Valid numbers
    assert is_valid("AB012") == False  # Invalid: starts with zero

    # Test no letters after numbers
    assert is_valid("AB123C") == False  # Invalid: letters after numbers
    assert is_valid("AB12C3") == False  # Invalid: interspersed letters/numbers

    # Test empty string
    assert is_valid("") == False  # Invalid: empty input
