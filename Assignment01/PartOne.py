def example(my_list, n):
    for item in my_list:
        if item < n:
            print(item, end=" ")

a = [1, 2, 3, 3, 6, 8, 15, 20, 32, 59, 87]

x = int(input("Enter a number: "))


print(example(a, x))