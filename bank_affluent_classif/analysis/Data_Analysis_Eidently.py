import pandas as pd
from evidently.dashboard import Dashboard
from evidently.tabs import DataDriftTab

DATA_SOURCE = r'C:\git\python\projects\bank_affluent_classif\data\bank_customer_data.csv'
df = pd.read_csv(DATA_SOURCE)

# create a dashboard
dashboard = Dashboard(tabs=[DataDriftTab])

# select only numeric columns
df_numeric = df.select_dtypes(include=['int64', 'float64'])

# generate the report for the DataFrame
dashboard.calculate(df_numeric, df_numeric, column_mapping = None)

# save the report as an HTML file
dashboard.save('my_report.html')