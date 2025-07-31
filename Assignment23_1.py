# Q1: Create a DataFrame for student marks and print basic information like shape, columns, and data types.
# data = {
# 'Name': ['Amit', 'Sagar', 'Pooja'],
# 'Math' :  [85, 90, 78],
# 'Science': [92, 88, 80],
# 'English': [75, 85, 82]
# }
#---------------------------------------------------------------------------------------------------------------. 

def main():
    import pandas as pd
    import numpy as np

    data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    print("Shape : ",df.shape)
    print("Columns : ",df.columns)
    print("Datatypes : ",df.dtypes)

if __name__ =="__main__":
    main()