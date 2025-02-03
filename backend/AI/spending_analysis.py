import pandas as pd
import matplotlib.pyplot as plt

def analyze_student_spending():
    # Read the CSV file
    df = pd.read_csv('backend/AI/student_spending (1).csv')

    # Calculate average spending for each category
    spending_categories = {
        'Housing': df['housing'].mean(),
        'Food': df['food'].mean(),
        'Transportation': df['transportation'].mean(),
        'Books & Supplies': df['books_supplies'].mean(),
        'Entertainment': df['entertainment'].mean(),
        'Personal Care': df['personal_care'].mean(),
        'Technology': df['technology'].mean(),
        'Health & Wellness': df['health_wellness'].mean(),
        'Miscellaneous': df['miscellaneous'].mean()
    }

    # Create pie chart
    plt.figure(figsize=(12, 8))
    plt.pie(spending_categories.values(), 
            labels=spending_categories.keys(), 
            autopct='%1.1f%%',
            startangle=90)
    plt.title('Student Spending Distribution by Category')
    plt.axis('equal')

    # Save the plot
    plt.savefig('spending_distribution.png')
    plt.close()

    # Calculate and format summary statistics
    summary_stats = {
        'category': [],
        'average': [],
        'median': [],
        'std_dev': []
    }

    for category in spending_categories.keys():
        col_name = category.lower().replace(' & ', '_').replace(' ', '_')
        summary_stats['category'].append(category)
        summary_stats['average'].append(df[col_name].mean())
        summary_stats['median'].append(df[col_name].median())
        summary_stats['std_dev'].append(df[col_name].std())

    # Create summary DataFrame
    summary_df = pd.DataFrame(summary_stats)
    summary_df = summary_df.round(2)

    return summary_df

def main():
    try:
        summary = analyze_student_spending()
        print("\nStudent Spending Analysis Summary:")
        print("==================================")
        print(summary.to_string(index=False))
        
        total_avg = summary['average'].sum()
        print(f"\nTotal Average Monthly Spending: ${total_avg:.2f}")
        
    except FileNotFoundError:
        print("Error: Could not find the student spending CSV file")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main() 