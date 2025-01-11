import pandas as pd
import numpy as np

def main():
    # Task 1: Create DataFrame
    data = {
        'Name': ['Aditi', 'Rahul', 'Deepak', 'Priya', 'Vijay'],
        'Age': [25, 30, 35, 40, 45],
        'City': ['Delhi', 'Mumbai', 'Bangalore', 'Hyderabad', 'Chennai']
    }
    df = pd.DataFrame(data)
    
    # Task 2: Add 'Age Group' column
    bins = [20, 30, 40, 50]
    labels = ['20s', '30s', '40s']
    df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
    
    # Task 3: Filter individuals in their 30s
    df_30s = df[df['Age Group'] == '30s']
    
    # Task 4: Calculate statistics
    mean_age = df['Age'].mean()
    median_age = df['Age'].median()
    variance_age = df['Age'].var()
    
    # Display results
    print("Original DataFrame:")
    print(df)
    print("\nDataFrame for individuals in their 30s:")
    print(df_30s)
    print("\nStatistics for 'Age':")
    print(f"Mean: {mean_age}")
    print(f"Median: {median_age}")
    print(f"Variance: {variance_age}")

# Call the main function
if __name__ == "__main__":
    main()
