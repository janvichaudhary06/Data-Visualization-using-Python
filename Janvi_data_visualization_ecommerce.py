import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Load dataset
df = pd.read_csv("ecommerce_sales.csv")

print("E-commerce Sales Dataset Preview:")
print(df.head())

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# 1️⃣ Total Revenue by Category
sns.barplot(x='Category', y='Total Revenue', data=df, estimator=sum)
plt.title("Total Revenue by Category")
plt.ylabel("Revenue")
plt.show()

# 2️⃣ Sales Trend Over Time
df_grouped = df.groupby("Date")["Total Revenue"].sum().reset_index()
sns.lineplot(x='Date', y='Total Revenue', data=df_grouped)
plt.title("Sales Trend Over Time")
plt.xticks(rotation=45)
plt.show()

# 3️⃣ Quantity Sold by Product
sns.boxplot(x='Product', y='Quantity Sold', data=df)
plt.title("Quantity Sold by Product")
plt.xticks(rotation=45)
plt.show()

# 4️⃣ Total Revenue by Region
sns.barplot(x='Region', y='Total Revenue', data=df, estimator=sum)
plt.title("Total Revenue by Region")
plt.ylabel("Revenue")
plt.show()

# 5️⃣ Correlation Heatmap
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

print("\n✅ E-commerce Sales Data Visualization Complete.")
