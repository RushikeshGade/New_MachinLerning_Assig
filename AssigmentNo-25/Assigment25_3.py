# Q3: Apply Label Encoding to a 'City' column
# data = {'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}
#--------------------------------------------------------------------.

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def main():
    data = {'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}
    df = pd.DataFrame(data)

    lebel = LabelEncoder()

    df['City'] = lebel.fit_transform(df['City'])

    print("DtaFrame with Encoded City : ")
    print(df)

if __name__ == "__main__":
    main()    