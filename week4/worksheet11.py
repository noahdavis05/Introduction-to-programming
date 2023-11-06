def rec_mult(x,y):
    if y == 1:
        return x
    else:
        return x + rec_mult(x,y-1)


def countdown(x):
    if x == 0:
        print("0")
    else:
        print(x)
        countdown(x-1)

    
print(countdown(2))