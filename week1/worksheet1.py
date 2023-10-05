import math
#task one
def calc_distance(capacity,kpl): #kpl is kilometers per litre
    return capacity * kpl

#cap = int(input("What is the car's tanks capacity?"))
#efficiency = int(input("What is the car's kilometers per litre?"))

#print(calc_distance(cap,efficiency))

#task two
def calc_volume(r, h):
    return math.pi * r * r * h

#radius = int(input("Radius of cylinder:  "))
#height = int(input("Height of cylinder:  "))
#print(calc_volume(radius,height))

#task three
def f_to_c(temp):
    return (temp - 32) * (5/9)

t = int(input("Temperature:  "))
print(f_to_c(t))