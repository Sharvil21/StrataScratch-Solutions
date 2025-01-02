#First Solution
# Import your libraries
import pandas as pd

# Start writing code
filtered_df = fb_comments_count.query("created_at > '2020-01-10' and created_at <= '2020-02-10'")

filtered_df.groupby('user_id').agg(number_of_comments=('number_of_comments','sum')).reset_index()
