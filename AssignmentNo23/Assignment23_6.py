# Q6: Sort the DataFrame by Total marks in descending order


import pandas as pd
import numpy as np

def main():
    data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    df['Total'] = df['Math'] + df['Science'] + df['English']

    print("Data before sorting")
    print(df)

    df_new = df.sort_values(by='Total', ascending = False)

    print("Data after sorting")
    print(df_new)

if __name__=="__main__":
    main()    