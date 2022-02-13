def sumSeriesOne(x, n):

    sumSeries = 1+x

    for i in range(2, n+1):
        sumSeries += x**i

    return f"Addition of Series One : {sumSeries}"
    
def sumSeriesTwo(x, n):

    sumSeries = 1-x

    for i in range(2, n+1):
        sumSeries += x**i

    return f"Addition of Series Two : {sumSeries}"


def sumSeriesThree(x, n):
    
    sumSeries = x-2**2

    for i in range(3, n+1):
        sumSeries += i**i
    
    return f"Addition of Series Three : {sumSeries}"


def sumSeriesFour(x, n):

    sumSeries = x

    for i in range(2, n+1):
        fact = 1

        for j in range(1, i+1):
            fact*=j

        sumSeries+=fact
    
    return f"Addition of Series Four : {sumSeries}"

#Driver's Code
valueX = int(input("Enter any desired value for x : "))
valueN = int(input("Enter any desired value for n : "))

print(sumSeriesOne(valueX, valueN))
print(sumSeriesTwo(valueX, valueN))
print(sumSeriesThree(valueX, valueN))
print(sumSeriesFour(valueX, valueN))