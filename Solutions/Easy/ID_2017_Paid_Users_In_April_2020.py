#Solution using .query() method.
# Import your libraries
import pandas as pd

# Start writing code
df = rc_calls.merge(rc_users,on='user_id',how='inner').query("status=='paid' and date >= '2020-04-01' and date <= '2020-04-30'")

df['user_id'].nunique()
