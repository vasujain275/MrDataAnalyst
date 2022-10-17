from traceback import print_tb
from unicodedata import numeric
import pandas as pd
def amax(df):
    print("On which you want to use maximum function?(1/2/3)")
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
    print("On which you want to use minimum function?(1/2/3)")
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
    else:
        print("Choose Between 1/2/3")

def asum(df):
    print("On which you want to use sum function?(1/2/3)")
    print('''
    1. Sum of all columns in Dataframe
    2. Sum of all rows in Dataframe
    3. Sum of specified column in Dataframe
    ''')
    coln = int(input("> "))
    numn = input("Do you want only numeric values?(y/n): ")
    if numn=='y':
        numo = True
    elif numn=='n':
        numo = False
    
    if coln==1:
        print(df.sum(axis=0,numeric_only=numn))
    elif coln==2:
        print(df.sum(axis=1,numeric_only=numn))
    elif coln==3:
        coln = input("Enter the Exact Name of Column you want to use: ")
        print(df[coln].sum(numeric_only=numn))
    else:
        print("Choose Between 1/2/3")

def acount(df):
    print("On which you want to use count function?(1/2/3)")
    print('''
    1. Count of all columns in Dataframe
    2. Count of all rows in Dataframe
    3. Count of specified column in Dataframe
    ''')
    coln = int(input("> "))
    numn = input("Do you want only numeric values?(y/n): ")
    if numn=='y':
        numo = True
    elif numn=='n':
        numo = False
    
    if coln==1:
        print(df.count(axis=0,numeric_only=numn))
    elif coln==2:
        print(df.count(axis=1,numeric_only=numn))
    elif coln==3:
        coln = input("Enter the Exact Name of Column you want to use: ")
        print(df[coln].count(numeric_only=numn))
    else:
        print("Choose Between 1/2/3")

def amode(df):
    pass

def amean(df):
    pass

def amedian(df):
    pass

d = {"Name":['Vasu','Jatin'],
     'Marks':[100,90]
    }
df = pd.DataFrame(d)
print(amin(df))