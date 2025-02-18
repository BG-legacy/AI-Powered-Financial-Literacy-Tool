import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_income_spending():
    # Read the CSV file
    df = pd.read_csv('backend/AI/student_spending (1).csv')
    
    # Calculate total monthly spending for each student
    spending_columns = ['housing', 'food', 'transportation', 'books_supplies', 
                       'entertainment', 'personal_care', 'technology', 
                       'health_wellness', 'miscellaneous']
    
    df['total_spending'] = df[spending_columns].sum(axis=1)
    
    # Create scatter plot
    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=df, x='monthly_income', y='total_spending', alpha=0.5)
    
    # Add trend line
    sns.regplot(data=df, x='monthly_income', y='total_spending', 
                scatter=False, color='red', line_kws={'linestyle': '--'})
    
    # Customize plot
    plt.title('Monthly Income vs Total Spending', fontsize=14, pad=20)
    plt.xlabel('Monthly Income ($)', fontsize=12)
    plt.ylabel('Total Monthly Spending ($)', fontsize=12)
    
    # Calculate correlation coefficient
    correlation = df['monthly_income'].corr(df['total_spending'])
    
    # Add correlation annotation
    plt.annotate(f'Correlation: {correlation:.2f}', 
                xy=(0.05, 0.95), 
                xycoords='axes fraction', 
                fontsize=12)
    
    # Save plot
    plt.savefig('income_spending_scatter.png', bbox_inches='tight', dpi=300)
    plt.close()
    
    # Calculate summary statistics
    summary_stats = {
        'Metric': ['Average Income', 'Average Spending', 'Correlation',
                  'Min Income', 'Max Income', 'Min Spending', 'Max Spending'],
        'Value': [
            df['monthly_income'].mean(),
            df['total_spending'].mean(),
            correlation,
            df['monthly_income'].min(),
            df['monthly_income'].max(),
            df['total_spending'].min(),
            df['total_spending'].max()
        ]
    }
    
    summary_df = pd.DataFrame(summary_stats)
    return summary_df

def main():
    try:
        summary = analyze_income_spending()
        print("\nIncome vs Spending Analysis Summary:")
        print("====================================")
        
        # Format currency values
        for idx, row in summary.iterrows():
            if row['Metric'] != 'Correlation':
                print(f"{row['Metric']}: ${row['Value']:.2f}")
            else:
                print(f"{row['Metric']}: {row['Value']:.2f}")
                
        print("\nScatter plot has been saved as 'income_spending_scatter.png'")
        
    except FileNotFoundError:
        print("Error: Could not find the student spending CSV file")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main() 