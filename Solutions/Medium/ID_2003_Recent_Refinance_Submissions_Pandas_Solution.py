#Pandas Solution
#First, we merge the dataframe using an innerjoin
#Then, we'll have to first filter out those rows where the type is 'Refinance' first
#AFter that, we create a new column for the most recent date.
#This can be done by using .transform('max') method after .groupby()
#Lastly filter this dataframe where the created_at date is the same as the most recent date, and return the user_id as well as balance
