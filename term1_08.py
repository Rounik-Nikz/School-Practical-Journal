def numGcd(numOne,numTwo):
    if numOne == 0:
        return numTwo
    return numGcd(numTwo % numOne, numOne)
 

def numLcm(numOne,numTwo):
    return (numOne / numGcd(numOne,numTwo))* numTwo
 

# Driver's Code
numOne = int(input("Enter First Number : "))
numTwo = int(input("Enter Second Number : "))

print(f'\nLowest Common Multiple of {numOne} and {numTwo} : {numLcm(numOne, numTwo)}\n')
print(f'Greatest Common Divisor of {numOne} and {numTwo} : {numGcd(numOne, numTwo)}\n')