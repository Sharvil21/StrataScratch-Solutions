#Pandas Solution
#We'll have to use the .loc[] method to filter 
# Import your libraries
import pandas as pd

# Start writing code
forbes_global_2010_2014.loc[(forbes_global_2010_2014['sector']== 'Financials') & ((forbes_global_2010_2014['continent']== 'Asia') | (forbes_global_2010_2014['continent']== 'Europe')),'company']

#Another Pandas Solution using .query() method
