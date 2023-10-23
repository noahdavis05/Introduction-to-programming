def minus(arg1, arg2):
    return arg2 - arg1

def rectangle_area(width, height):
    return width * height

def check_upper_lower(x):
    x = str(x)
    lower_count = 0
    upper_count = 0
    my_list = list(x)
    
    for item in my_list:
        if item.isupper():
            upper_count += 1
        elif item.islower():
            lower_count += 1
        elif item.isnumeric():
            lower_count += 1

    return [upper_count, lower_count]


print(check_upper_lower(1234))

