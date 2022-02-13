def countVowelsConsonants(string):
     
    vowels = 0
    consonants = 0

    for alphabets in string:

        if (alphabets == "a" or alphabets == "A" 
        or alphabets == "e" or alphabets == "E"
        or alphabets == "i" or alphabets == "I"
        or alphabets == "o" or alphabets == "O"
        or alphabets == "u" or alphabets == "U"):

            vowels += 1

        else:
            consonants += 1

    print (f"\nVowels : {vowels}\n")
    print (f"Consonants : {consonants}\n")

def countLowerUpper(string):

    upperCase = 0
    loweCase = 0

    for alphabets in string:
        if alphabets.isupper() == True:
            upperCase += 1
        else:
            loweCase += 1

    print (f"UpperCase Characters : {upperCase}\n")
    print (f"LowerCase Characters : {loweCase}\n")


#Driver's Code
string = input("Enter Any String : ")

countVowelsConsonants(string)
countLowerUpper(string)