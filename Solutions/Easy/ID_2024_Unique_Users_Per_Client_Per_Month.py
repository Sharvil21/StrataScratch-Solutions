#First Solution:
# Import your libraries
import pandas as pd

# Start writing code
fact_events['month'] = fact_events['time_id'].dt.month
fact_events.groupby(['client_id','month'])['user_id'].nunique().reset_index()

#Second Solution

