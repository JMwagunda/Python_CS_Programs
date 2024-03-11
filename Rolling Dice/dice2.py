from random import *
from tkinter import *
from tabulate import tabulate

counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0


for i in range (1,1001):
    number= random()

    if  number >=0 and number <(1/6):
        counter1 += 1

    elif number >= 1/6 and number <2/6:
        counter2 += 1

    elif number >= 2/6 and number <3/6:
        counter3 += 1

    elif number >= 3/6 and number <4/6:
        counter4 += 1

    elif number >= 4/6 and number <5/6:
        counter5 += 1

    elif number >= 5/6 and number < 6/6:
        counter6 += 1

    
print(counter1)
print(counter2)
print(counter3)
print(counter4)
print(counter5)
print(counter6)

percent_1 = round(counter1 * 0.1, 1)
percent_2 = round(counter2 * 0.1, 1)
percent_3 = round(counter3 * 0.1, 1)
percent_4 = round(counter4 * 0.1,1)
percent_5 = round(counter5 * 0.1, 1)
percent_6 = round(counter6 * 0.1, 1)


total_counter = counter1 + counter2 + counter3 + counter4 + counter5 + counter6
print("Total counter = ", total_counter)

total_percentage = percent_1+percent_2+percent_3+percent_4+percent_5+percent_6
print("Total percentage is = " + str(round(total_percentage,1)))

l = [["1", counter1,percent_1], ["2", counter2, percent_2], ["3", counter3, percent_3],["4", counter4, percent_4], ["5", counter5, percent_5], ["6", counter6, percent_6], ["", 1000, round(total_percentage,1)]]
table = tabulate(l, headers=['Face ', 'Frequency', 'Percentage'],tablefmt='orgtbl')

print(table)



class Table:
    def __init__(self,root):
        #code for creating table
        for i in range(total_rows ):
            for j in range(total_columns ):
                self.e = Entry(root, width=20, fg='blue', font=('Arial', 16, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, list[i][j])

list = [
        ["Face", "Frequency","Percentage (%) "],["1", counter1,percent_1],
        ["2", counter2, percent_2], ["3", counter3, percent_3],["4", counter4, percent_4],
        ["5", counter5, percent_5], ["6", counter6, percent_6], ["Total", total_counter, round(total_percentage,1)]
        ]


total_rows = len(list)
total_columns = len(list[0])

root =  Tk()
t = Table(root)
root.mainloop()