#First Solution
# Import your libraries
import pandas as pd

# Start writing code
df2 = twitch_sessions.groupby('user_id')['session_type'].nunique().reset_index()

df2[df2['session_type'] > 1]['user_id']

#
