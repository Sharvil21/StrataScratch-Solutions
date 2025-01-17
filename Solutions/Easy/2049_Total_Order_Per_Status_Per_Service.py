#Solution without using .agg() method
# Import your libraries
import pandas as pd

# Start writing code
uber_orders.groupby(['service_name','status_of_order'])['number_of_orders'].sum().to_frame('orders_sum').reset_index()

#Solution
