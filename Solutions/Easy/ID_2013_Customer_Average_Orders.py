#Solution
# Import your libraries
import pandas as pd

# Start writing code
postmates_orders.agg({'customer_id':'nunique','amount':'mean'}).reset_index()
