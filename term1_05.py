def perfectNumber(num : int):

    Sum = 0

    for i in range(1, num):
        if num%i==0:
            Sum = Sum+i
    
    if Sum == num:
        return f"\nPerfect Number : True"
    else:
        return f"\nPerfect Number : False"

def armStrongNum(num : int):

    lenNum = len(str(num))
    Sum = 0 

    temp = num
    while temp > 0:
        digit = temp % 10
        Sum += digit ** lenNum
        temp //= 10

    if num == Sum:
        return f"\nArmstrong Number : True"
    else:
        return f"\nArmstrong Number : False"

def palindromeNum(num : int):

    Strnum = str(num)
    reversedNum = Strnum[::-1]

    if Strnum == reversedNum:
        return f"\nPalindrome Number : True\n"
    else:
        return f"\nPalindrome Number : False\n"

#Driver's Code
number = int(input("Enter any Number : "))

print(perfectNumber(number))
print(armStrongNum(number))
print(palindromeNum(number))