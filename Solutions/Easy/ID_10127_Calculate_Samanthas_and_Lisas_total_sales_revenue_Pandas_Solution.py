#Pandas Solution
#Can just use .loc[] to get the rows directly where salesperson is Samantha Or Lisa
#Then we can just take the sum() of sales_revenue column
# Import your libraries
import pandas as pd

# Start writing code
sales_performance.loc[(sales_performance['salesperson'] == 'Samantha') | (sales_performance['salesperson'] == 'Lisa'),'sales_revenue'].sum()
