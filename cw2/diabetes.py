"""
Please write your name
@author:Noah Davis

"""

# Reminder: You are only allowed to import the csv module (done it for you).
# OTHER MODULES ARE NOT ALLOWED (NO OTHER IMPORT!!!).

import csv


class Diabetes:
    def __init__(self, filepath) -> None:
        # open the file
        try:
            f = open(filepath,"r")
        except:
            raise Exception("FileNotFoundError")
        
        # make the variables header and data
        # read the data
        my_data = f.read().splitlines()
        # make the header variable
        self.header = my_data[0].split(",")
        # make the data variable
        # this will be a 2d array
        self.data = []
        for i in range(1,len(my_data)):
            self.data.append(my_data[i].split(","))

    def get_dimension(self) -> list:
        return [len(self.data),len(self.header)]

    def web_summary(self, filepath: str) -> None:
        # sort out my data and make lists
        attributes = self.header.copy()
        #make a copy of list so actual list isn't changed when i pop
        #remove age and gender attributes
        attributes.pop(0)
        attributes.pop(0)
        pos_list = []
        neg_list = []
        for row in self.data:
            if row[self.get_dimension()[1]-1] == "Positive":
                pos_list.append(row)
            else:
                neg_list.append(row)

        # now for each of these lists check how many yesses and nos
        pos_y_list = []
        pos_n_list = []
        neg_y_list = []
        neg_n_list = []
        # make these lists the correct length
        for i in range(0,self.get_dimension()[1]):
            pos_y_list.append(0)
            pos_n_list.append(0)
            neg_y_list.append(0)
            neg_n_list.append(0)


        # iterate through pos_list
        for row in pos_list:
            for i in range(0,self.get_dimension()[1]):
                if row[i] == 'Yes':
                    pos_y_list[i] += 1
                else:
                    pos_n_list[i] += 1

        # iterate through neg_list
        for row in neg_list:
            for i in range(0,self.get_dimension()[1]):
                if row[i] == 'Yes':
                    neg_y_list[i] += 1
                else:
                    neg_n_list[i] += 1

        print(attributes)
        print(pos_n_list)
        print(pos_y_list)
        print(neg_y_list)
        print(neg_n_list)

        # write the html file
        f = open(filepath,"w")
        f.write('''<html>
 <head> 
  <meta name="viewport" content="width=device-width, initial-scale=1"> 
  <style id="compiled-css" type="text/css">
th, td {
   font-weight:normal;
   padding:6px;
   width:121px;
   vertical-align:top;
}




tr + tr, tbody {
   text-align:left
}

table, th, td {
   border:solid 2px;
   border-collapse:collapse;
   table-layout:fixed;
}
</style> 
 </head> 
 <body> 
  <table> 
   <thead> 

    <tr> 
     <th colspan="1" rowspan="3">Attributes </th> 
     <th colspan="4">Class</th>  
    </tr> 

    <tr>
        <th colspan="2">Positive</th>
        <th colspan="2">Negative</th>
    </tr>


    <tr> 
     <th>Yes</th> 
     <th>No</th> 
     <th>Yes</th> 
     <th>No</th>  
    
    </tr> 
   </thead>
    <tbody>  
   ''')
        
        # now i need to iterate through my lists and add all the items
        # minus one so that i don't include the class attribute
        for i in range(0,self.get_dimension()[0] -1):
            f.write("<tr>\n")
            f.write("<th>")
            f.write(attributes[i])
            f.write("</th>\n")
            f.write("<td>")
            f.write(str(pos_y_list[i]))
            f.write("</td>\n")
            f.write("<td>")
            f.write(str(pos_n_list[i]))
            f.write("</td>\n")
            f.write("<td>")
            f.write(str(neg_y_list[i]))
            f.write("</td>\n")
            f.write("<td>")
            f.write(str(neg_n_list[i]))
            f.write("</td>\n")

        # finish off the code
        f.write('''</tbody> 
  </table>  
 </body>
</html>''')
        f.close()


        

        
    
    #criteria will be a string split by commas to seperate the criteria which the user wants to select
    #gender will be a string saying either "Male" or "Female"
    #age will be a string which will contain an number
    # positive will be a string saying either "Positive" or "Negative"
    def count_instances(self,gender = None, age = None, positive = None, criteria = None) -> int:
        # work out the index of each of the items
        criteria_list = []
        if gender != None:
            criteria_list.append([1,gender])

        if age != None:
            criteria_list.append([0,age])

        if positive != None:
            criteria_list.append([(self.get_dimension()[1] - 1),positive])

        if criteria != None:
            # iterate through the list and check if the items are in the header
            # if they are add the item to criteria_list
            temp_list = criteria.split(",")
            for item in temp_list:
                if item in self.header:
                    #find the position of that item in header
                    criteria_list.append([self.header.index(item),"Yes"])

        # now count the items
        # iterate through data
        count = 0
        for row in self.data:
            # iterate through criteria list 
            row_valid = True
            for criterion in criteria_list:
                #check the values in row
                if row[criterion[0]] != criterion[1]:
                    row_valid  = False

            if row_valid:
                count += 1


        print(criteria_list)
        print(count)


if __name__ == "__main__":
    # You can comment the following when you are testing your code
    # You can add more tests as you want

    # test diabetes_data.csv
    #d1 = Diabetes("diabetes_data.csv")
    #print(d1.get_dimension())
    #d1.web_summary('stat01.html')
    # d1.count_instances() # change according to your criteria
    print()

    # test diabetes2_data.csv
    d2 = Diabetes("diabetes2_data.csv")
    print(d2.get_dimension())
    d2.web_summary('stat02.html')
    d2.count_instances("Male",age="58",positive="Positive",criteria="Polydipsia")  # change according to your criteria
