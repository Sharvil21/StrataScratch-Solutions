#First Solution
# Import your libraries
import pandas as pd

# Start writing code
facebook_posts.groupby(facebook_posts['post_date'].dt.day).agg(user_activity=('post_id','count')).reset_index()

#Second Solution
# Import your libraries
import pandas as pd

# Start writing code
facebook_posts.groupby(facebook_posts.post_date.dt.day)['post_id'].count().to_frame().reset_index()
