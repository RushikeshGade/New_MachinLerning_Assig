# Q4: Plot a pie chart of subject marks for 'Sagar'.

import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    sagar_marks = df[df['Name'] == 'Sagar'][['Math', 'Science', 'English']].iloc[0]

    # Plot pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(sagar_marks,labels=sagar_marks.index,autopct='%1.1f%%',startangle=140)
    plt.title("Sagar's Subject Marks ")
    plt.show()

if __name__ == "__main__":
    main()
