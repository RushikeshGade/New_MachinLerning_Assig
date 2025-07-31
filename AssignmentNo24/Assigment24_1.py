# Q1: Normalize the 'Math' scores using Min-Max scaling.

import pandas as pd 
from sklearn.preprocessing import MinMaxScaler


def main():

    data = {

    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math' :  [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    # math_min = df['Math'].min()
    # math_max = df['Math'].max()

    # df['Math_Normalize'] = (df['Math']-math_min) /(math_max - math_min)   # Min-Max Scaling  
    # print(df)

    # or 

    scaler = MinMaxScaler()

    # Fit and transform the 'Math' Min-Max Scaling 
    df['Math_Normalized'] = scaler.fit_transform(df[['Math']])

    print(df)
     


if __name__ =="__main__":
    main()


