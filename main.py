import pandas as pd
import aggr
import plots
import base

base.Welcome()
d = base.DataCreate()

df = base.CSV(d)

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
        6. Back to Previous Menu / Exit
        ''')
        visn = int(input("> "))

        if visn==1:
            plots.SingelLine(df)
        elif visn==2:
            plots.MultiLine(df)
        elif visn==3:
            pass
        elif visn==4:
            plots.Bar(df)
        elif visn==5:
            pass
        elif visn==6:
            pass

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
        8. Back to Previous Menu / Exit
        ''')
        aggrn = int(input("> "))
        if aggrn==1:
            print(aggr.amax(df))
        elif aggrn==2:
            print(aggr.amin(df))
        elif aggrn==3:
            print(aggr.asum(df))
        elif aggrn==4:
            print(aggr.acount(df))
        elif aggrn==5:
            print(aggr.amean(df))
        elif aggrn==6:
            print(aggr.amedian(df))
        elif aggrn==7:
            print(aggr.amode(df))
        elif aggrn==8:
            pass
        else:
            print('Please choice the correct number')
    opn = input("Do you want to continue(y/n): ")