#task 1 concatinate dictionaries
def add_dicts(dicts):
    #dicts is a list of dictionaries
    my_dict = {}
    for i in dicts:
        for key, value in i.items():
            my_dict[key] = value

    return my_dict

dict1 = {'sc0011': 'Ali Bin Ahmad', 'sc0012': 'Wong Fei Hung', 'sc0013': 'James Purple', 'sc0014': 'Salimah Wahid'}
dict2 = {'it1011': 'Abdus Salam', 'it1012': 'Alex Chung', 'it1013': 'Anastasia Zeus', 'it1014': 'Vihaan Arjun'}
dict3 = {'ai2011': 'Charles Lewin', 'ai2012': 'Apollo Leto', 'ai2013': 'Ciarra Vega', 'ai2014': 'Lara Gould'}
            
my_list = [dict1, dict2,dict3]
#print(add_dicts(my_list))

def add_dict_values (d1, d2):
    #iterate through first dict
    key_list = []
    d3 = {}
    for key in d1:
        if key not in key_list:
            key_list.append(key)

    for key in d2:
        if key not in key_list:
            key_list.append(key)

    #add values from each list
    for key in key_list:
        if key in d1 and key in d2:
            total = d1[key] + d2[key]
            d3[key] = total
        elif key in d1:
            d3[key] = d1[key]
        else:
            d3[key] = d2[key]

    return d3

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
#print(add_dict_values(d1,d2))

def odd_even_dict():
    odd = []
    even = []
    for i in range(1,52):
        if i %2 == 0:
            even.append(i)
        else:
            odd.append(i)

    my_dict = {'odd':odd, 'even':even}

    return my_dict

#print(odd_even_dict())

my_dict = {'a': 500, 'b': 200, 'c': 1500, 'd': 20, 'x': 1550, 'v': 260}

def get_boundaries(my_dict):
    lowest = list(my_dict.values())[0]
    highest = list(my_dict.values())[0]
    for key, value in my_dict.items():
        if value < lowest:
            lowest = value
        elif value > highest:
            highest = value

    return lowest, highest

print(get_boundaries(my_dict))


