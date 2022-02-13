def checkPrimeComposite(num):

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(f"{num}is a COMPOSITE number")
                break
        else:
            print(f"{num} is a PRIME number")

    elif num == 0 or 1:
        print(f"{num} is a neither prime NOR composite number")
    else:
        print(f"{num} is a COMPOSITE number")

#Driver's Code
number = int(input("Enter any number : "))

checkPrimeComposite(number)
