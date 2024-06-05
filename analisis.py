import pandas as pd

# Path to the CSV file
file_path = 'data.csv'

# Read the data from the CSV file
df = pd.read_csv(file_path)

# Convert 'marketcap' to numeric, assuming it's already in a suitable format
df['marketcap'] = pd.to_numeric(df['marketcap'].replace(',', '', regex=True))

# Define market cap thresholds for categorization (these are arbitrary examples)
thresholds = {
    'Small': 50_000_000_000,  # Companies with a market cap less than $50 billion
    'Medium': 100_000_000_000,  # Companies with a market cap between $50 billion and $100 billion
    'Large': float('inf')  # Companies with a market cap over $100 billion
}

# Function to categorize each row
def categorize_marketcap(row):
    if row['marketcap'] < thresholds['Small']:
        return 'Small'
    elif row['marketcap'] < thresholds['Medium']:
        return 'Medium'
    else:
        return 'Large'

# Apply the function to the DataFrame
df['Size Category'] = df.apply(categorize_marketcap, axis=1)

# Print results
print(df[['Name', 'marketcap', 'Size Category']])

# Save the results to a new CSV file if needed
df.to_csv('categorized_data.csv', index=False)
