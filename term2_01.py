def largestNum(list_tuple) -> None:
    return max(list_tuple)

def smallestNum(list_tuple) -> None:
    return min(list_tuple)


list = [2,3,4,5]
tuple = (6,7,8,9,10)

print("Maximum Number from the list : ",largestNum(list))
print("Maximum Number from the tuple : ",largestNum(tuple),"\n")

print("Smallest Number from the list : ",smallestNum(list))
print("Smallest Number from the tuple : ",smallestNum(tuple))