#Pandas Solution
#Filter out the rows first
#Then groupby.
# Import your libraries
import pandas as pd

# Start writing code
library_usage.head()

df = library_usage.loc[(library_usage['age_range'] == '65 to 74 years') & (library_usage['circulation_active_month'] == 'April') & (library_usage['year_patron_registered'] == 2015)]

df.groupby(['year_patron_registered','home_library_definition'],as_index=False).agg(max_total_checkouts=('total_checkouts','max')).sort_values(by='max_total_checkouts',ascending=False)
