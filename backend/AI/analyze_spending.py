import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Read the CSV file
df = pd.read_csv('backend/AI/student_spending (1).csv')

# Get spending columns (excluding non-spending columns)
spending_columns = ['monthly_income', 'financial_aid', 'tuition', 'housing', 'food', 
                   'transportation', 'books_supplies', 'entertainment', 'personal_care',
                   'technology', 'health_wellness', 'miscellaneous']

# Create a figure with subplots
fig, axes = plt.subplots(4, 3, figsize=(20, 16))
fig.suptitle('Distribution of Student Spending by Category\nShowing Number of Students per Spending Range', fontsize=16, y=0.95)

# Flatten axes array for easier iteration
axes = axes.flatten()

# Create histograms for each spending column
for idx, column in enumerate(spending_columns):
    # Create histogram on respective subplot
    axes[idx].hist(df[column], bins=30, color='skyblue', edgecolor='black')
    
    # Add mean and median lines
    mean_val = df[column].mean()
    median_val = df[column].median()
    axes[idx].axvline(mean_val, color='red', linestyle='--', alpha=0.8, label=f'Mean: ${mean_val:.0f}')
    axes[idx].axvline(median_val, color='green', linestyle='--', alpha=0.8, label=f'Median: ${median_val:.0f}')
    
    # Add title and labels
    axes[idx].set_title(f'{column.replace("_", " ").title()}\nTotal Students: {len(df)}', fontsize=12)
    axes[idx].set_xlabel('Amount ($)', fontsize=10)
    axes[idx].set_ylabel('Number of Students', fontsize=10)
    axes[idx].grid(True, alpha=0.3)
    
    # Add legend
    axes[idx].legend(fontsize=8)
    
    # Rotate x-axis labels for better readability
    axes[idx].tick_params(axis='x', rotation=45)

# Adjust layout to prevent overlap
plt.tight_layout()

# Save the plot
plt.savefig('backend/AI/spending_distribution.png', bbox_inches='tight', dpi=300)
plt.close() 