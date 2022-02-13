def largestNum(list) -> None:
    return max(list)

def smallestNum(list) -> None:
    return min(list)


list = eval(input("Input a List : "))

print("Maximum Number from the list : ",largestNum(list))
print("Minimum Number from the list : ",smallestNum(list))