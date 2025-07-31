# Q8: Plot a histogram of math marks.

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

    # Plot histogram of Math marks
    plt.hist(df['Math'], bins=5, color="skyblue", edgecolor="black")
    plt.xlabel("Math Marks")
    plt.ylabel("Frequency")
    plt.title("Histogram of Math Marks")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

if __name__ == "__main__":
    main()
