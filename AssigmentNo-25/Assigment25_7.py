# Q7: Normalize 'Age' column using Min-Max Scaling
# data = {'Age': [18, 22, 25, 30, 35]}
#-------------------------------------------------------------.

import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def main():
    data = {'Age': [18, 22, 25, 30, 35]}

    df = pd.DataFrame(data)
    
    scaler = MinMaxScaler()
    df['Age_Normalize'] = scaler.fit_transform(df[['Age']])

    print(df)

if __name__ == "__main__":
    main()    