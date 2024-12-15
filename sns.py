import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
regions = ['North', 'South', 'East', 'West']
product_categories = ['Electronics', 'Clothing', 'Furniture', 'Groceries']

data = {
    'Region': np.random.choice(regions, size=500),
    'Sales': np.random.uniform(1000, 10000, size=500).round(2),
    'Profit': np.random.uniform(200, 5000, size=500).round(2),
    'Marketing_Spend': np.random.uniform(500, 3000, size=500).round(2),
    'Product_Category': np.random.choice(product_categories, size=500)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('sales_data.csv', index=False)

print("Synthetic dataset 'sales_data.csv' created!")
