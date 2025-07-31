# Q5. Create a DataFrame with 'Age' and 'Purchased' columns and split into train/test sets.
# data {'Age': [22, 25, 47, 52, 46, 56], 'Purchased':
# [0, 1, 1, 0, 1, 0]}
#--------------------------------------------------------------------.

import pandas as pd
from sklearn.model_selection import train_test_split


def main():
    data = {'Age': [22, 25, 47, 52, 46, 56], 'Purchased':[0, 1, 1, 0, 1, 0]}

    df = pd.DataFrame(data)
    print(df)
    
    X = df[['Age']]   
    y = df['Purchased']

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state = 42)

    print("X_train:", X_train)
    print("\nX_test:", X_test)
    print("\ny_train:", y_train)
    print("\ny_test:", y_test)

if __name__ == "__main__":
    main()    