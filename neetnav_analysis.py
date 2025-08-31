# Neetnav Financial PDF Analysis (2023–2024)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Create DataFrame from extracted financials
data = {
    "Year": [2023, 2024],
    "Revenue_from_operations": [15.6, 15.6],
    "Other_income": [11.8, 1.1],
    "Total_income": [27.4, 16.7],
    "Finance_costs": [169.5, 304.1],
    "Depreciation": [1.9, 1.9],
    "Other_expenses": [56.7, 38.2],
    "Total_expenses": [228.1, 344.2],
    "Profit_before_tax": [-200.7, -327.5],
    "Deferred_tax": [-0.2, -0.2],
    "Net_profit": [-200.5, -327.3]
}

df = pd.DataFrame(data)

# Step 2: Summary statistics
print("🔍 Summary Statistics:")
print(df.describe())

# Step 3: Total Income vs Total Expenses
plt.figure(figsize=(8, 5))
plt.plot(df["Year"], df["Total_income"], marker="o", label="Total Income")
plt.plot(df["Year"], df["Total_expenses"], marker="o", label="Total Expenses")
plt.title("Total Income vs Total Expenses (2023-2024)")
plt.xlabel("Year")
plt.ylabel("₹ in Lakh")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 4: Profit Before Tax Comparison
plt.figure(figsize=(8, 5))
sns.barplot(x="Year", y="Profit_before_tax", data=df, palette="coolwarm")
plt.title("Profit Before Tax (2023 vs 2024)")
plt.ylabel("₹ in Lakh")
plt.tight_layout()
plt.show()

# Step 5: Expense Breakdown
df_expenses = df[["Year", "Finance_costs", "Depreciation", "Other_expenses"]]
df_expenses.set_index("Year").plot(kind="bar", stacked=True, figsize=(10, 6))
plt.title("Expense Breakdown by Year")
plt.ylabel("₹ in Lakh")
plt.xlabel("Year")
plt.tight_layout()
plt.show()

# Step 6: Summary of Findings
print("\n📌 Key Findings:")
print("1. Total income decreased from ₹27.4 Lakh in 2023 to ₹16.7 Lakh in 2024.")
print("2. Finance costs nearly doubled from ₹169.5 Lakh to ₹304.1 Lakh.")
print("3. Net loss increased from ₹200.5 Lakh to ₹327.3 Lakh despite reduced other expenses.")