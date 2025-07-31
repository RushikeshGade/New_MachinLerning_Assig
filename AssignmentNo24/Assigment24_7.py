# Q7. Export the final DataFrame to a CSV file.

import pandas as pd 

def main():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math' :  [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(data)

    # Export to CSV
    df.to_csv('student_results.csv', index=False)

    print("Final DataFrame exported to 'student_results.csv'")




if __name__ == "__main__":
    main()