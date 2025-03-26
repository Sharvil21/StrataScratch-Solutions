#Pandas Solution
#First, we merge the dataframe using an innerjoin
#Then, we'll have to first filter out those rows where the type is 'Refinance' first
#AFter that, we create a new column for the most recent date.
#This can be done by using .transform('max') method after .groupby()
#Lastly filter this dataframe where the created_at date is the same as the most recent date, and return the user_id as well as balance
#We'd be creating two dataframes for this solution
# Import your libraries
import pandas as pd

# Start writing code
df = loans.merge(submissions,left_on='id',right_on='loan_id',how='inner')
df2 = df.loc[df['type']=='Refinance']
df2['most_recent_date'] = df2.groupby('user_id')['created_at'].transform('max')
df2.loc[df2['created_at']==df2['most_recent_date'],['user_id','balance']]
