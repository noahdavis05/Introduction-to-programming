import random

def work_out(num):
    answer = ""
    if (num % 5) == 0 and (num % 3) == 0:
        answer = "fizzbuzz"
    elif num % 5 == 0:
        answer = "buzz"
    elif num % 3 == 0:
        answer = "fizz"
    else:
        answer = str(num)

    return answer

def task1():
    for i in range(1,101):
        if i % 2 == 1:
            #users go
            ans = str(input("Enter answer:  "))
            if ans != work_out(i):
                print("incorrect, you lose")
                break
        else:
            correct = work_out(i)
            if random.randint(1,5) == 1:
                ans = str(i)
                if ans != correct:
                    print(ans)
                    print("Computer is wrong, you win")
                    break
                else:
                    print(correct)
            else:
                print(correct)

def task2():
    num = random.randint(1,100)
    guessed = False
    count = 0
    while guessed == False and count < 5:
        guess = int(input("Guess a number:  "))
        count += 1
        if guess == num:
            guessed = True
            print("Correct")
        elif guess > num:
            print("Lower")
        else:
            print("Higher")

    if guessed == False:
        print("Unlucky, the answer was",str(num))





task2()