def is_palindrome(s):
    # Convert the string to lowercase and remove spaces
    s = s.lower().replace(" ", "")

    # Check if the string is equal to its reverse
    return s == s[::-1]


# Example usage
if __name__ == "__main__":
    word = input("Enter a word or phrase: ")
    if is_palindrome(word):
        print(f"'{word}' is a palindrome.")
    else:
        print(f"'{word}' is not a palindrome.")
