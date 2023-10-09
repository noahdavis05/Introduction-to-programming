#task 1
def within_range(num):
    if num >= 0 and num <= 94:
        return "Correct"
    else:
        return "Incorrect"
    
#n = int(input("Enter number:  "))
#print(within_range(n))

#task 2
def can_purchase_alcohol():
    age = int(input("Enter your age:  "))
    age_on_id = int(input("Enter the age on your ID:  "))
    estimated_age = int(input("Enter the estimated age of the buyer:  "))
    payed_on_card = int(input("Enter 1 if the user payed by card and 2 if not:  "))
    age_limit = 18
    if age == age_on_id:
        if age >= age_limit:
            if estimated_age >= 21:
                return True
            elif payed_on_card == 1:
                return True
            
    return False
            

print(can_purchase_alcohol())