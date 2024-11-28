def main():
    while True:
        try:
            # Get the fraction from the user
            fraction = input("Fraction: ")
            # Convert the fraction to a percentage
            percentage = convert(fraction)
            # Get the gauge output
            result = gauge(percentage)
            print(result)
            break
        except (ValueError, ZeroDivisionError):
            # Handle invalid input and prompt the user again
            pass

def convert(fraction):
    """Convert a fraction string to a percentage."""
    try:
        X, Y = fraction.split('/')
        X, Y = int(X), int(Y)
        if Y == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if X > Y:
            raise ValueError("Numerator cannot be greater than denominator.")
        return round((X / Y) * 100)
    except (ValueError, ZeroDivisionError) as e:
        raise e

def gauge(percentage):
    """Return a gauge reading based on the percentage."""
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
