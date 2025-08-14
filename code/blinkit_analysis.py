# importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import Raw Data
df = pd.read_csv("C:/Users/rasto/OneDrive/Desktop/Python for Data Analyst/Projects/blinkit_data.csv")

# Sample Data 
print(df.head(10))

# Size of Data 
print("Size of Data: ",df.shape)

# Field Info
print(df.columns)

# Data types
print(df.dtypes)

# Data Cleaning
print(df['Item Fat Content'].unique())

df['Item Fat Content'] = df['Item Fat Content'].replace({'LF': 'Low Fat','low fat':'Low Fat','reg':'Regular'})
# print(df['Item Fat Content'].unique())

# --------Business Requirements----------

# KPI's Requirements:-

# Total Sales
total_sales = df['Sales'].sum()

# Average Sales
avg_sales = df['Sales'].mean()

# no. of items sold
no_of_items_sold = df['Sales'].count()

# Average Ratings
avg_rating = df['Rating'].mean()

# Display
print(f"Total Sales: ${total_sales:,.0f}")
print(f"Average Sales: {avg_sales:,.0f}")
print(f"No. of items Sold: {no_of_items_sold:,.0f}")
print(f"Average Rating: {avg_rating:,.0f}")

# Charts Requirements

# Total Sales by Fat Content
sales_by_fat = df.groupby('Item Fat Content')['Sales'].sum()

plt.pie(sales_by_fat, labels=sales_by_fat.index, autopct='%.0f%%',startangle=90)
plt.title('Sales by Fat Content')
plt.axis('equal')
plt.show()

# Total Sales by items
sales_by_type = df.groupby('Item Type')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(10,6))
bars = plt.bar(sales_by_type.index, sales_by_type.values)

plt.xticks(rotation=90)
plt.xlabel('Item Type')
plt.ylabel('Total Sales')
plt.title('Total Sales by Item Type')

for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),f'{bar.get_height():,.0f}', ha='center', va='bottom',fontsize = 8)

plt.tight_layout()
plt.show()

# Fat Content Outlet for Total Sales
grouped = df.groupby(['Outlet Location Type','Item Fat Content'])['Sales'].sum().unstack()
grouped = grouped[['Regular','Low Fat']]

ax = grouped.plot(kind='bar',figsize=(8,5),title='Outlet ')
plt.xlabel('Outlet Location Tier')
plt.ylabel('Total Sales')
plt.legend(title='Item Fat Content')
plt.tight_layout()
plt.show()

# Total Sales by Outlet Establishment
sales_by_year = df.groupby('Outlet Establishment Year')['Sales'].sum().sort_index()

plt.figure(figsize=(9,5))
plt.plot(sales_by_year.index, sales_by_year.values, marker='o', linestyle='-')

plt.xlabel('Outlet Establishment Year')
plt.ylabel('Total Sales')
plt.title('Outlet Establishment')

for x , y in zip(sales_by_year.index, sales_by_year.values):
    plt.text(x, y, f'{y:,.0f}', ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()

# Sales by Outlet Size
sales_by_size = df.groupby('Outlet Size')['Sales'].sum()

plt.figure(figsize=(4, 4))
plt.pie(sales_by_size, labels=sales_by_size.index, autopct='%1.1f%%', startangle=90)
plt.title('Outlet Size')
plt.tight_layout()
plt.show()

# Sales by Outlet Location
sales_by_location = df.groupby('Outlet Location Type')['Sales'].sum().reset_index()
sales_by_location = sales_by_location.sort_values('Sales', ascending=False)

plt.figure(figsize=(8,3))
ax = sns.barplot(x='Sales', y='Outlet Location Type', data=sales_by_location)

plt.title('Total Sales by Outlet Location Type')
plt.xlabel('Total Sales')
plt.ylabel('Outlet Location Type')

plt.tight_layout()
plt.show()
