import pandas as pd
import time

def Welcome():
    print("-------------------------------")
    print("Hi there, I am Mr. Data Analyst")
    print("-------------------------------")
    print("I can help you sort,organize,aggregate and visualize your Data")
    print("I uses Data Frames to Work on Data")
    print("-------------------------------")

def DataCreate():
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
    return df

def CSV(d):
    csv = (input("Do you want to read/write your Data from CSV?(y/n)"))
    if csv=='y':
        d.to_csv('data.csv')
        df=pd.read_csv('data.csv')
        print(df)
    elif csv=='n':
        df=d
    return df

def EndCredits():
    print("\nThank you for using Data Anaylist Tool\n")
    print("Made by - \nJatin Gupta (XII D)\nVasu Jain (XII B)")
    time.sleep(15)
