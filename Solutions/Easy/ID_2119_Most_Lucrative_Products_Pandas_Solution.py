#Pandas Solution
# Import your libraries
import pandas as pd

# Start writing code
df = online_orders.query("date_sold.dt.year == 2022 and date_sold.dt.month >= 1 and date_sold.dt.month <= 6 ")
df['revenue'] = df['units_sold']*df['cost_in_dollars']

df.groupby('product_id',as_index=False).agg(total_revenue=('revenue','sum')).sort_values(by='total_revenue',ascending=False).iloc[:5]
