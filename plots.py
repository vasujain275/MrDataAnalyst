import pandas as pd
import matplotlib.pyplot as plt

def SingelLine(d):
    plt.plot(d)

d = {"Name":['Vasu','Jatin'],
     'Marks':[100,90]
    }
df = pd.DataFrame(d)
print(SingelLine(df))


