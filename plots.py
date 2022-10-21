import pandas as pd
import matplotlib.pyplot as plt

def SingelLine(df):
    namex = input("What do you want on X-axis: ")
    x = df[namex]
    namey = input("What do you want on Y-axis: ")
    y = df[namey]
    plt.plot(x,y,color='Red')
    plt.xlabel(input("Enter X-label: "))
    plt.ylabel(input("Enter Y-label: "))
    plt.title(input("Enter the title of the graph: "))
    plt.show()

def MultiLine(df):
    namey = input("What do you want on X-axis: ")
    x = df[namey]
    yn = int(input("Enter the No. of columns you want to plot: "))
    keys = []
    for i in range(0,yn):
        temp = input(f"Enter the Exact Name of Column {i+1} you want to plot: ")
        keys.append(temp)
    print(f"These the Columns that will be ploted {keys}")
    d = []
    df1 = pd.DataFrame(d)
    for i in keys:
        df1[i] = df[i]
    df1.plot(kind='line')
    plt.xlabel(input("Enter X-label: "))
    plt.ylabel(input("Enter Y-label: "))
    plt.title(input("Enter the title of the graph: "))
    plt.show()





# d = {"Name":['Vasu','Jatin','Rachit','Daksh'],
#      'IP':[100,90,45,50],
#      'Maths':[84,85,80,34],
#      'Chemistry':[90,99,89,69]
#     }
# df = pd.DataFrame(d)
# MultiLine(df)

