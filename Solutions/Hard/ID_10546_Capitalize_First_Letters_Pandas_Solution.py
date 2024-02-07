#Pandas Solution
#Although this is categorised as hard, the solution is easy
#We just create a new column, and use the .title() method to make the first letter uppercase of every word
# Import your libraries
import pandas as pd

# Start writing code
user_content['modified_text'] = user_content['content_text'].str.title()
user_content[['content_text','modified_text']]
