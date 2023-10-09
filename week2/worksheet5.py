#task 1
def sum_tuple_of_tuples(my_tuple):
    sum = 0
    for i in my_tuple:
        for x in i:
            sum += x

    return sum
my_nums = ((5, 10, 15, 20),  (2, 4, 6, 8), (57, 68, 79, 81), (1, 3, 5, 7))
print(sum_tuple_of_tuples(my_nums))