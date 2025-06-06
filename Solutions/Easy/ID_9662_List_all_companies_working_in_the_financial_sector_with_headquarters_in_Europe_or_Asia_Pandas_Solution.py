#Pandas Solution
#We'll have to use the .loc[] method to filter 
# Import your libraries
import pandas as pd

# Start writing code
forbes_global_2010_2014.loc[(forbes_global_2010_2014['sector']== 'Financials') & ((forbes_global_2010_2014['continent']== 'Asia') | (forbes_global_2010_2014['continent']== 'Europe')),'company']

#Another Pandas Solution using .query() method
#WE'll also have to use the .isin() method for filtering for Europe and Asia
import pandas as pd

df = forbes_global_2010_2014
result = df[(df['sector'] == 'Financials') & (df['continent'].isin(['Europe', 'Asia']))]['company']
