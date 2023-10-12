
def palindrome(name):
    name = name.lower().replace(" ", "")
    return name == name[::-1]


if __name__ == '__main__':
    word = input("Enter the word: ")
    print(palindrome(word))
