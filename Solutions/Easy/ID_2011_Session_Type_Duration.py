#Solution
# Import your libraries
import pandas as pd

# Start writing code
twitch_sessions['duration'] = (twitch_sessions['session_end']- twitch_sessions['session_start']).dt.total_seconds()

twitch_sessions.groupby('session_type')['duration'].mean().reset_index()
