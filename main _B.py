

import pandas as pd

# Load the dataset
file_path = 'Resources/budget_data.csv'
df = pd.read_csv(file_path)

# 1) Total number of months
total_months = len(df['Date'])

# 2) Net total amount of "Profit/Losses"
net_total = df['Profit/Losses'].sum()

# 3) Changes in "Profit/Losses" over the entire period and average of those changes
df['Change'] = df['Profit/Losses'].diff()
average_change = df['Change'].mean()

# 4) Greatest increase in profits (date and amount)
max_increase_date = df.loc[df['Change'].idxmax(), 'Date']
max_increase_amount = df['Change'].max()

# 5) Greatest decrease in profits (date and amount)
max_decrease_date = df.loc[df['Change'].idxmin(), 'Date']
max_decrease_amount = df['Change'].min()

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total:.2f}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase_date} (${max_increase_amount:.2f})")
print(f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease_amount:.2f})")