#task one

def list_even_nums(limit):
    even_list = []
    odd_list = []
    for i in range(1,limit + 1):
        if i % 2 == 0:
            even_list.append(i)

        else:
            odd_list.append(i)

    return even_list, odd_list

#print(list_even_nums(51))

#task two
def split_letters_and_numbers(my_string):
    my_list = list(my_string)
    num_list = []
    letter_list = []
    for i in my_list:
        if ord(i) > 47 and ord(i) < 58:
            num_list.append(i)
        else:
            letter_list.append(i)

    return num_list, letter_list

s = str(input("Enter a sentenne please:  "))
#print(split_letters_and_numbers(s))

def sort_characters(my_string):
    my_list = list(my_string)
    sorted_list = []
    found_letters = []
    my_list.sort()
    for i in my_list:
        if i not in found_letters:
            found_letters.append(i)
            temp_list = [i]
            sorted_list.append(temp_list)
        else:
            #find sublist where letters are stored
            for x in sorted_list:
                if x[0] == i:
                    x.append(i)

    return sorted_list


print(sort_characters(s))
