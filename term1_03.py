def patternOne():
    print("===== Pattern - 1 =====")

    n = 6
    for i in range(0, n):
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")

    print("\n")

def patternTwo():
    print("===== Pattern - 2 =====")

    n = 7
    for j in range(1,6):

        for i in range(1,n-j):
            print(i * 1, end=" ")
        print("\r")

    print("\n")


def patternThree():
    print("===== Pattern - 3 =====")

    lst = ["A", "B", "C", "D", "E"]
    n = 0

    while n<5:
        n=n+1

        for i in range(n):
            print(lst[i], end=" ")
        print("\r")
        
    print("\n")
    
#Driver's Code
patternOne()
patternTwo()
patternThree()