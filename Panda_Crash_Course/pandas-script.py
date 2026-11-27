import pandas as pd

# -------------------------------
# 1. Loading Dataset
# -------------------------------

df = pd.read_csv("retail_sales.csv")

print("Dataset Loaded")
print(df.head())

# -------------------------------
# 2. Dataset Overview
# -------------------------------

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nData Types")
print(df.dtypes)

print("\nSummary Statistics")
print(df.describe())

# -------------------------------
# 3. Selecting Columns
# -------------------------------

print("\nSelecting Single Column")
print(df["Product"].head())

print("\nSelecting Multiple Columns")
print(df[["Customer", "Product", "Price"]].head())

# -------------------------------
# 4. Filtering Data
# -------------------------------

print("\nOrders where Category = Electronics")

electronics = df[df["Category"] == "Electronics"]

print(electronics.head())

# Multiple Conditions

high_value = df[(df["Price"] > 10000) & (df["Category"] == "Electronics")]

print("\nHigh Value Electronics Orders")
print(high_value.head())

# -------------------------------
# 5. Adding New Columns
# -------------------------------

df["Total_Sales"] = df["Quantity"] * df["Price"]

print("\nTotal Sales Column Added")
print(df.head())

# -------------------------------
# 6. Sorting Data
# -------------------------------

sorted_df = df.sort_values(by="Price", ascending=False)

print("\nTop Expensive Products")
print(sorted_df.head())

# -------------------------------
# 7. Handling Missing Values
# -------------------------------

print("\nMissing Values")
print(df.isnull().sum())

# -------------------------------
# 8. Unique Values
# -------------------------------

print("\nUnique Cities")
print(df["City"].unique())

print("\nNumber of Unique Products")
print(df["Product"].nunique())

# -------------------------------
# 9. Value Counts
# -------------------------------

print("\nProduct Frequency")
print(df["Product"].value_counts())

# -------------------------------
# 10. GroupBy Operations
# -------------------------------

print("\nTotal Sales by Category")

sales_by_category = df.groupby("Category")["Total_Sales"].sum()

print(sales_by_category)

# Multiple Aggregations

print("\nCategory Statistics")

category_stats = df.groupby("Category")["Total_Sales"].agg(["sum", "mean", "max"])

print(category_stats)

# -------------------------------
# 11. Group By City
# -------------------------------

city_sales = df.groupby("City")["Total_Sales"].sum()

print("\nCity Wise Sales")
print(city_sales)

# -------------------------------
# 12. Pivot Table
# -------------------------------

pivot = pd.pivot_table(
    df,
    values="Total_Sales",
    index="City",
    columns="Category",
    aggfunc="sum"
)

print("\nPivot Table")
print(pivot)

# -------------------------------
# 13. Date Operations
# -------------------------------

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month

monthly_sales = df.groupby("Month")["Total_Sales"].sum()

print("\nMonthly Sales")
print(monthly_sales)

# -------------------------------
# 14. Top Customers
# -------------------------------

top_customers = df.groupby("Customer")["Total_Sales"].sum().sort_values(ascending=False)

print("\nTop Customers")
print(top_customers.head())

# -------------------------------
# 15. Export Processed Data
# -------------------------------

df.to_csv("processed_sales.csv", index=False)

print("\nProcessed data saved!")