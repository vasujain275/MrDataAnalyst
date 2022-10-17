from unicodedata import numeric
import pandas as pd
def amax(df):
    print("Which type of maximum value you want?(1/2/3)")
    print('''
    1. Maximum value of all columns in Dataframe
    2. Maximum value of all rows in Dataframe
    3. Maximum value of specifed column in Dataframe
    ''')
    coln = int(input("> "))
    numn = input("Do you want only numeric values?(y/n): ")
    if numn=='y':
        numo = True
    elif numn=='n':
        numo = False

    if coln==1:
        print(df.max(axis=0,numeric_only=numn))
    elif coln==2:
        print(df.max(axis=1,numeric_only=numn))
    elif coln==3:
        col = input("Enter the Exact Name of Column you want to use: ")
        print(df[col].max(numeric_only=numn))
    else:
        print("Choose between 1/2/3")

def amin(df):
    print("Which type of minimum values you wanr?(1/2/3)")
    print('''
    1. Minimum values of all columns in Dataframe
    2. Minimum values of all rows in Dataframe
    3. Minimum values of specified column in Dataframe
    ''')
    coln = int(input("> "))
    numn = input("Do you want only numeric values?(y/n): ")
    if numn=='y':
        numo = True
    elif numn=='n':
        numo = False

    if coln==1:
        print(df.min(axis=0,numeric_only=numn))
    elif coln==2:
        print(df.min(axis=1,numeric_only=numn))
    elif coln==3:
        coln = input("Enter the Exact Name of Column you want to use: ")
        print(df[coln].min(numeric_only=numn))

def asum(df):
    pass

def acount(df):
    pass

def amode(df):
    pass

def amean(df):
    pass

def amedian(df):
    pass

# d = {"Name":['Vasu','Jatin'],
#      'Marks':[100,90]
#     }
# df = pd.DataFrame(d)
# print(amax(df))