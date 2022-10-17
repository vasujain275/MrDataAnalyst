import pandas as pd
import aggr
print("-------------------------------")
print("Welcome to Data Anaylist Tool")
print("-------------------------------")
print("This tool can help you sort,organize,aggregate and visualize your Data")
print("We uses Data Frames to Work on Data")
print("-------------------------------")
coln = int(input("Please Enter the Number of Columns you want:"))
d = {}
keys = []
for i in range(0,coln):
    temp = input(f"Enter Column {i+1} Name: ")
    keys.append(temp)
print(f"So your Columns are {keys}")
rown = int(input("Please Enter the Number of Rows you want:"))
for i in keys:
    print(f"Enter Values for {i} :")
    tempval = []
    valn = input("Are Values Numeric?(y/n): ")
    for j in range(0,rown):
        if valn=='y':
            temp = int(input(f"Enter Value {j+1}: "))
            tempval.append(temp)
        else:
            temp = input(f"Enter Value {j+1}: ")
            tempval.append(temp)
    d[i] = tempval
iyn = input("Do you want to use Custom Index?(y/n)")
if iyn=='y':
    indexn = []
    for i in range(0,rown):
        temp1 = int(input("Enter Index Values:"))
        indexn.append(temp1)
    df = pd.DataFrame(d,index=indexn)
else:
    df = pd.DataFrame(d)
print("-------------------------------")
print(f'Here is your Data Frame\n{df}')
print("-------------------------------")
opn ="y"
while opn=='y':
    print("What you want to do with your Data?")
    print('''
    1. Visualize
    2. Aggregate
    ''')
    datan = int(input("> "))

    if datan==1:
        print("Which type of Data Visualization you want?")
        print('''
        1. Single Line Plot
        2. Multiple Line Plot
        3. Multiple View Line Plot
        4. Bar Plot
        5. Histogram
        ''')
        visn = int(input("> "))
    elif datan==2:
        print("Which type of Data Aggregation you want?")
        print('''
        1. Maximum Value
        2. Minimum Value
        3. Sum of Values
        4. Count of Values
        5. Mean of Values
        6. Median of Values
        7. Mode of Values
        ''')
        aggrn = int(input("> "))
        if aggrn==1:
            print(aggr.amax(df))
        

    opn = input("Do you want to continue(y/n): ")

print("\nThank you for using Data Anaylist Tool\n")
print("Made by - \nJatin Gupta (XII D)\nVasu Jain (XII B)")