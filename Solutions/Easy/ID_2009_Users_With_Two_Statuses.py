#First Solution
# Import your libraries
import pandas as pd

# Start writing code
df2 = twitch_sessions.groupby('user_id')['session_type'].nunique().reset_index()

df2[df2['session_type'] > 1]['user_id']

#Second Solution
# Import your libraries
import pandas as pd

# Start writing code
result = twitch_sessions.groupby('user_id')['session_type'].nunique().to_frame('n_types').reset_index()
result = result[result['n_types'] == 2]['user_id']

