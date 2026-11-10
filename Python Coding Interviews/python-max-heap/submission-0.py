import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    results = []
    sort_num = []

    for num in nums:
        heapq.heappush(sort_num, -num)
    
    while sort_num:
        results.append(-heapq.heappop(sort_num))

    return results


#TypeError: 'builtin_function_or_method' object is not subscriptable
#Not subscriptable means you cannot use square brackets [] to access elements of that object.


# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
