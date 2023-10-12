'''An Armstrong number (also known as a narcissistic number or pluperfect digital invariant) is a number
that is equal to the sum of its own digits each raised to the power of the number of digits.
For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.'''

def is_armstrong_number(num):
    # Calculate the number of digits in the number
    num_str = str(num)
    num_digits = len(num_str)

    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

    # Check if the sum is equal to the original number
    return armstrong_sum == num


# Example usage
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_armstrong_number(num):
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")
