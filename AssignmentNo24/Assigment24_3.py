# Q3: Group students by gender and calculate average marks.

import pandas as pd 

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Gender': ['Male', 'Male', 'Female'],  
        'Math' :  [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    avg_marks = df.groupby('Gender')[['Math', 'Science', 'English']].mean()

    print("Average marks grouped by Gender:\n")
    print(avg_marks)

if __name__ == "__main__":
    main()
