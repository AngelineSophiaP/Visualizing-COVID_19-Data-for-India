import pandas as pd

df = pd.read_csv('supermarket_data.csv')
print(df.head(5))
print(df.info)
print(df.isnull().sum())

df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])
df['Day'] = df['DateTime'].dt.day_name()
df['Hour'] = df['DateTime'].dt.hour

branch_revenue = df.groupby('Branch')['Total'].sum()
print(branch_revenue)
branch_revenue_sorted = branch_revenue.sort_values(ascending = False)
print(branch_revenue_sorted)

product_quantity = df.groupby('Product line')['Quantity'].sum()
product_quantity_sorted = product_quantity.sort_values(ascending =False)
print(product_quantity_sorted)

payment_method = df.groupby('Payment').value_counts().idxmax()
print(payment_method)

sales_by_gender = df.groupby('Gender')['Total'].sum().sort_values(ascending = False)
print(sales_by_gender)

sales_by_day = df.groupby('Day')['Total'].sum().sort_values(ascending=False)
print(sales_by_day)

avg_rating_by_branch = df.groupby('Branch')['Rating'].mean().sort_values(ascending = False)
print(avg_rating_by_branch)

correlation = df['Quantity'].corr(df['Total'])
print("Correlation between Quantity and Total:", correlation)

def categorize_rating(rating):
    if rating >= 8:
        return 'High'
    elif rating >= 5:
        return 'Medium'
    else:
        return 'Low'
df['Satisfaction'] = df['Rating'].apply(categorize_rating)

avg_rating_by_city = df.groupby('City')['Rating'].mean().sort_values(ascending=False)
print(avg_rating_by_city)
top_city = avg_rating_by_city.idxmax()
print("City with highest average customer rating:", top_city)
