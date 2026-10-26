from typing import List

def read_integers() -> List[int]:
    data = input()
    string_list = data.split(",")

    int_list = []
    for s in string_list:
        int_list.append(int(s))
    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
