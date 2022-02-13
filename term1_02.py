def largestNumber(num1, num2, num3):

    print(f"{max(num1,num2,num3)} is largest")
    print(f"{min(num1,num2,num3)} is smallest")

#Driver's Code
numOne = int(input("Enter First Number : "))
numTwo = int(input("Enter Second Number : "))
numThree = int(input("Enter Third Number : "))

largestNumber(numOne,numTwo,numThree)