def make_validator(min_value):

    def validate(number):

        if number >= min_value:
            return True
        else:
            return False

    return validate


validator1 = make_validator(10)
validator2 = make_validator(50)

print("minimun value 10:")
print("Validator 1:", validator1(15))
print("Validator 1:", validator1(5))

print("\nminimum value 50:")
print("Validator 2:", validator2(60))
print("Validator 2:", validator2(30))