#Pandas Solution
# Import your libraries
import pandas as pd

# Start writing code
sf_events['month'] = sf_events['record_date'].dt.month
sf_events['year'] = sf_events['record_date'].dt.year

sf_events.query("month==1 and year == 2021").groupby(['month','year','account_id'])['user_id'].nunique().reset_index()[['account_id','user_id']]
