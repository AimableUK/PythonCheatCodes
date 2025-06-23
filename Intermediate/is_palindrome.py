def is_palindrome(word):
    i = 0  # Start index
    j = len(word) - 1  # End index
    while i < j:  # Continue as long as the start index is less than the end index
        if word[i] != word[j]:  # Compare characters at the start and end
            return False  # If they are not equal, it's not a palindrome
        i = i + 1  # Move the start index forward
        j = j - 1  # Move the end index backward
    return True  # If no mismatches were found, the word is a palindrome


if is_palindrome("racecar"):
    print("palindrome")
else:
    print("not palindrome")