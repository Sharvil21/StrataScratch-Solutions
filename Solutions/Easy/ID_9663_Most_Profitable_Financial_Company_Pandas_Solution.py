#Pandas Solution
#Although there is a column called rank already in the table, I created another column called rnk with .rank() and used the 'dense' method for the profit column
#All that's left now to do is to use the .loc[] to filter out those rows where the rnk value is 1, and get teh company and continent columns
# Import your libraries
import pandas as pd

# Start writing code
forbes_global_2010_2014['rnk'] = forbes_global_2010_2014['profits'].rank(method='dense',ascending=False)
forbes_global_2010_2014.loc[forbes_global_2010_2014['rnk'] == 1,['company','continent']]
