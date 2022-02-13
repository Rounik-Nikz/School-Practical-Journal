def searchElement(List_tuple, element) -> None:

    for i in range(len(List_tuple)):

        if List_tuple[i] == element:
            return i

    return -1

List_tuple = eval(input("Enter a list : "))
element = int(input("Enter the element you want to search for : "))

result = searchElement(List_tuple, element)

if result != -1:
    print(f"The element is present at the index position : {result}")
else:
    print("The element is not present in the list")