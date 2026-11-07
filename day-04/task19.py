class InvalidNumberError(Exception):
    pass


while True:

    try:
        number = int(input("Enter a number between 1 and 10: "))

        if number < 1 or number > 10:
            raise InvalidNumberError("Number must be between 1 and 10!")

        print("Valid Number:", number)
        break

    except ValueError:
        print("Error: Please enter a numeric value!")

    except InvalidNumberError as e:
        print("Error:", e)