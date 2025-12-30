import pandas as pd

# --- Day 1: Setup & Load Data ---
# Loading the dataset from the CSV file
file_path = './sales_data.csv'
df = pd.read_csv(file_path)

# --- Day 2: Explore Data ---
# Checking the basic structure of the data
print("Data Shape:", df.shape)
print("Data Columns:", df.columns.tolist())
# print(df.info()) # To check data types

# --- Day 3: Clean Data ---
# Checking for missing values
missing_values = df.isnull().sum().sum()
if missing_values > 0:
    # Fill numeric missing values with 0 or drop them based on context
    df = df.fillna(0)
    print(f"Handled {missing_values} missing values.")

# Removing duplicate rows if any exist
duplicates_count = df.duplicated().sum()
if duplicates_count > 0:
    df = df.drop_duplicates()
    print(f"Removed {duplicates_count} duplicate rows.")

# --- Day 4: Analyze Sales ---
# Calculation 1: Total Revenue
total_revenue = df['Total_Sales'].sum()

# Calculation 2: Best-selling product (by revenue)
product_revenue = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
best_selling_product = product_revenue.index[0]

# Calculation 3: Average Sale Value
avg_sale = df['Total_Sales'].mean()

# Calculation 4: Top Region
top_region = df.groupby('Region')['Total_Sales'].sum().idxmax()

# --- Day 5: Create Report ---
# Formatted output with insights
print("\n" + "="*40)
print("       SALES PERFORMANCE REPORT")
print("="*40)
print(f"Total Revenue:         ₹{total_revenue:,.2f}")
print(f"Average Order Value:   ₹{avg_sale:,.2f}")
print(f"Best-Selling Product:  {best_selling_product}")
print(f"Top Performing Region: {top_region}")
print("-" * 40)
print("Insights:")
print(f"- {best_selling_product} is the primary revenue driver.")
print(f"- {top_region} is the most profitable region.")
print("="*40)