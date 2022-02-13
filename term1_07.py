def Fibonacci_series(Number):

    if(Number == 0):
        return 0

    elif(Number == 1):
        return 1

    else:
        return (Fibonacci_series(Number - 2) + Fibonacci_series(Number - 1))

#Driver's Code
num = int(input("Enter the Number of terms you want to display: "))
print("Fibonacci Series:", end = ' ')

for i in range(0, num):
  print(Fibonacci_series(i), end = ' ')
