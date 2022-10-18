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



# d = {"Name":['Vasu','Jatin','Rachit','Daksh'],
#      'Marks':[100,90,45,50]
#     }
# df = pd.DataFrame(d)
# print(SingelLine(df))

