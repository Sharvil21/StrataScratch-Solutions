#Pandas Solution
# Import your libraries
import pandas as pd



df = uber_employees.merge(uber_annual_review,left_on='id',right_on='emp_id',how='left')
filtered_df = df.groupby('id_x')['review_date'].count().reset_index()
required_ids = filtered_df.query("review_date == 0")['id_x']
y = list(required_ids)
uber_employees.query(f"id.isin({y})")[['first_name','last_name','hire_date','termination_date']].sort_values(by='hire_date',ascending=False)
