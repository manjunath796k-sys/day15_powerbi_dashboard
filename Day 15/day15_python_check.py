import pandas as pd

# =========================================================
# DAY 15 POWER BI - COMPLETE PYTHON CROSS CHECK
# =========================================================

# 1. Load CSV files
customers = pd.read_csv("Capstone Customers.csv")
orders = pd.read_csv("Capstone Orders.csv")

print("=" * 60)
print("DAY 15 POWER BI DASHBOARD - PYTHON CROSS CHECK")
print("=" * 60)

# =========================================================
# 2. Remove duplicate rows
# =========================================================

customers = customers.drop_duplicates()
orders = orders.drop_duplicates()

print("\nAfter removing duplicates:")
print("Customers:", len(customers))
print("Orders:", len(orders))

# =========================================================
# 3. Clean Customers data
# =========================================================

customers["Region"] = (
    customers["Region"]
    .fillna("Unknown")
    .astype(str)
    .str.strip()
    .str.title()
)

customers["Segment"] = (
    customers["Segment"]
    .fillna("Unknown")
    .astype(str)
    .str.strip()
    .str.title()
)

# =========================================================
# 4. Clean Orders data
# =========================================================

orders["Category"] = (
    orders["Category"]
    .fillna("Unknown")
    .astype(str)
    .str.strip()
    .str.title()
)

orders["Sales"] = pd.to_numeric(
    orders["Sales"], errors="coerce"
).fillna(0)

orders["Profit"] = pd.to_numeric(
    orders["Profit"], errors="coerce"
).fillna(0)

orders["Quantity"] = pd.to_numeric(
    orders["Quantity"], errors="coerce"
).fillna(0)

# =========================================================
# 5. Merge Customers and Orders
# =========================================================

merged = pd.merge(
    orders,
    customers[["CustomerID", "CustomerName", "Region", "Segment"]],
    on="CustomerID",
    how="left"
)

# =========================================================
# 6. Merge Customers and Orders
# =========================================================

merged = pd.merge(
    orders,
    customers[["CustomerID", "CustomerName", "Region", "Segment"]],
    on="CustomerID",
    how="left"
)

# =========================================================
# 7. KPI CROSS CHECK
# =========================================================

total_sales = merged["Sales"].sum()
total_profit = merged["Profit"].sum()
profit_margin = (
    total_profit / total_sales * 100
    if total_sales != 0 else 0
)
order_count = merged["OrderID"].nunique()

print("\n" + "=" * 60)
print("1. KPI CROSS CHECK")
print("=" * 60)

print(f"Total Sales      : ₹{total_sales:,.2f}")
print(f"Total Profit     : ₹{total_profit:,.2f}")
print(f"Profit Margin %  : {profit_margin:.2f}%")
print(f"Order Count      : {order_count}")

# =========================================================
# 8. REGION-WISE SALES
# =========================================================

region_sales = (
    merged.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n" + "=" * 60)
print("2. REGION-WISE TOTAL SALES")
print("=" * 60)

print(region_sales.round(2))

# =========================================================
# 9. REGION-WISE PROFIT
# =========================================================

region_profit = (
    merged.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\n" + "=" * 60)
print("5. REGION-WISE TOTAL PROFIT")
print("=" * 60)

print(region_profit.round(2))


# =========================================================
# 10. FINAL VERIFICATION
# =========================================================

print("\n" + "=" * 60)
print("10. FINAL POWER BI VERIFICATION")
print("=" * 60)


print("✓ Region-wise Sales calculated")
print("✓ Region-wise Profit calculated")

print("\nDashboard cross-check completed successfully.")
print("=" * 60)