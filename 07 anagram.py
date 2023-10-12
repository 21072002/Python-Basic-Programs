'''An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
For example, "listen" is an anagram of "silent".'''

def is_anagram(str1, str2):
    # Convert the strings to lowercase and remove spaces
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")

    # Check if the sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)


# Example usage
if __name__ == "__main__":
    word1 = input("Enter the first word or phrase: ")
    word2 = input("Enter the second word or phrase: ")

    if is_anagram(word1, word2):
        print(f"'{word1}' and '{word2}' are anagrams.")
    else:
        print(f"'{word1}' and '{word2}' are not anagrams.")
