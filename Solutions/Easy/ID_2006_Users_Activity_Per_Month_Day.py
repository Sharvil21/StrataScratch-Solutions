#First Solution
# Import your libraries
import pandas as pd

# Start writing code
facebook_posts.groupby(facebook_posts['post_date'].dt.day).agg(user_activity=('post_id','count')).reset_index()

#Second Solution: This time without .agg() method and using .to_frame() method to convrt to dataframe and .reset_index() method to get the desired output
# Import your libraries
import pandas as pd

# Start writing code
facebook_posts.groupby(facebook_posts.post_date.dt.day)['post_id'].count().to_frame().reset_index()
