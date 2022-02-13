def checkStrPalindrome(string):

    revsersedStr = string[::-1]

    if string == revsersedStr:
        print(f"{string} is a Palindrome String")
    else:
        print(f"{string} is not a Palindrome String")

def changeStrCase(string):

    for char in string:
        if char.isupper():
            print(char.lower(), end="")
        else:
            print(char.upper(), end="")
        

#Driver's Code
string = input("Enter a string : ")

checkStrPalindrome(string)

print("Changed Case String: ", end="")
changeStrCase(string)
