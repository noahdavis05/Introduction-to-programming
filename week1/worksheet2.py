#task 1
def greet(firstname, lastname):
    f = firstname.capitalize()
    s = lastname.capitalize()
    my_string = "Hello " + f + " " + s
    
    return my_string

#f = str(input("Enter firstname:  "))
#s = str(input("Enter surname:  "))
#print(greet(f,s))

#task 2
def calc_occurence(sentence, character):
    count = 0
    s = list(sentence)
    for i in s:
        if i == character:
            count += 1
        
    return count

#s = str(input("Type a sentence:  "))
#c = str(input("Enter a letter to count:  "))
#print(calc_occurence(s,c))

#task 3
def calc_vowels(sentence):
    count = 0
    vowels = ["a","e","i","o","u"]
    s = list(sentence)
    for i in s:
        if i in vowels:
            count += 1

    return count

s = str(input("Sentence:  "))
print(calc_vowels(s))