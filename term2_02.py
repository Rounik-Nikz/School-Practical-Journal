def swap_elements(lst : list) -> None:
    n = len(lst)

    for elelment in range(1,n,2):
        lst[elelment], lst[elelment-1] = lst[elelment-1], lst[elelment]
    return lst


inputList = eval(input("Enter a list : "))
print("List after swapping elements : ",swap_elements(inputList))