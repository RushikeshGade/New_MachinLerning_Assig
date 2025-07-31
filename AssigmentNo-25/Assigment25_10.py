# Q10: Split a DataFrame with multiple features into train-test for supervised learning
# data = {
# 'Age': [25, 30, 45, 35, 221, Salary [50000, 60000, 80000, 65000, 45000],
# 'Purchased': [1, 0, 1, 0, 1]
# }
#--------------------------------------------------------------------------------------------.

import pandas as pd
from sklearn.model_selection import train_test_split


def main():
    data = {
    'Age': [25, 30, 45, 35, 22],
    'Salary': [50000, 60000, 80000, 65000, 45000],
    'Purchased': [1, 0, 1, 0, 1]
}


    df = pd.DataFrame(data)
    print(df)
    
    X = df[['Age', 'Salary']]   
    y = df['Purchased']

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state = 42)

    print("X_train:", X_train)
    print("\nX_test:", X_test)
    print("\ny_train:", y_train)
    print("\ny_test:", y_test)

if __name__ == "__main__":
    main()    