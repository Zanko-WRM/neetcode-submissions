from typing import List # this is used to add type hints for List type

def find_index(nums: List[int], target: int) -> int:
    n = len(nums)
    i = -1
    for m in nums: 
        i +=1
        if m==target:
             return i
            
   
    # for n in nums:
    #     if n==target:
    #         return nums.index(n)       


# don't modify code below this line
print(find_index([1, 2, 3, 4, 5], 3))
print(find_index([1, 2, 3, 4, 5, 3], 3))
print(find_index([1, 2, 3, 4], 1))
print(find_index([1, 3, 4, 2], 2))

