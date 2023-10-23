def task1():
    num1 = int(input("Enter an integer number please: "))
    num2 = int(input("Enter a bigger integer number please: "))
    count = 0
    for i in range(num1,num2):
        count += 1

    return count

def task2():
    my_list = []
    for i in range(0,5):
        temp_list = []
        for x in range(0,5):
            temp_list.append(i*5 + x)

        my_list.append(temp_list)

    return my_list
            
def task3():
    num_list = []
    for i in range(0,10):
        temp = int(input("Enter a number please:  "))
        num_list.append(temp)

    print(sum(num_list))
    print(sum(num_list)/10)

def calc_neighbours(i,x):  #This is used in task 4
    neighbours = [(i,x-1),(i,x+1),(i-1,x),(i+1,x)]
    if x == 0:
        neighbours.remove((i,x-1))
    if x == 5:
        neighbours.remove((i,x+1))
    if i == 0:
        neighbours.remove((i-1,x))
    if i == 2:
        neighbours.remove((i+1,x))

    return neighbours


def task4():
    num_list = [[1, 4, 0, 1, 3, 1], [2, 2, 4, 2, 2, 3], [1, 0, 1, 0, 1, 0]]
    
    num_list2 = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    for i in range(0,3):
        temp = []
        for x in range(0,6):
            #check if number 
            temp_num = num_list[i][x]
            neighbours = calc_neighbours(i,x) #returns a list of all the locations of the neighbours of the position
            for location in neighbours:
                n = num_list[location[0]][location[1]]
                temp_num += n

            num_list2[i][x] = round(temp_num /(len(neighbours)+1))

    return num_list2
                





print(task4())