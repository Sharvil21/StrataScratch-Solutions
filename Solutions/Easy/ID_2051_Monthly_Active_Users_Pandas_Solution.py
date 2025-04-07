#Pandas Solution
# Import your libraries
import pandas as pd

# Start writing code
sf_events['month'] = sf_events['record_date'].dt.month
sf_events['year'] = sf_events['record_date'].dt.year

sf_events.query("month==1 and year == 2021").groupby(['month','year','account_id'])['user_id'].nunique().reset_index()[['account_id','user_id']]

#2nd Solution
# Import your libraries
import pandas as pd

# Start writing code

df = sf_events.loc[(sf_events['record_date'].dt.month==1) & (sf_events['record_date'].dt.year ==2021)]

df.groupby(['account_id'])['user_id'].nunique().to_frame().reset_index()

#Third pandas Solution
# Import your libraries
import pandas as pd

# Start writing code

sf_events.query("record_date.dt.month==1 and record_date.dt.year==2021").groupby('account_id')['user_id'].nunique().to_frame().reset_index()


#
