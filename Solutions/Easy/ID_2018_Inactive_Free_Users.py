#Solution using .query() method
# Import your libraries
import pandas as pd

# Start writing code
free_users = rc_users.query('status=="free"')
users_in_april = rc_calls.query("date >= '2020-04-01' and date <= '2020-04-30'")['user_id'].unique()

free_users.query("user_id not in @users_in_april")['user_id'].unique()
