import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

# Read the CSV file
csv_file_path = 'path/to/your_file.csv'
df = pd.read_csv('Inventory - Katie Talerico Henry.csv')

# Create the MySQL Engine
engine = create_engine('mysql+mysqlconnector://tarroyo:Password!@localhost/distribution_db')

# Write the Dataframe to the MySQL Table
table_name = 'Distribution'
df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
