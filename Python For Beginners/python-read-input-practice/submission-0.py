def add_two_numbers() -> int:
    numbers = input()
    num_string = numbers.split(",")
    n_list = []
    for n in num_string:
        n_list.append(int(n))

    m = len(n_list)
    sum = 0
    for i in range(m):
        sum += n_list[i]

    return sum





# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
