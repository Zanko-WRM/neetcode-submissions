from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    n = len(arr)
    arr2 =[]
    for i in range(n):
        arr2.append(arr[-1])
        arr.pop(-1)
    return arr2
        




# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
