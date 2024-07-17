# Import Dependencies
import pandas as pd
import mysql.connector
import os
from sqlalchemy import create_engine
from sqlalchemy import text

# Folder path of CSV files
folder_path = '/Users/Justin/dev/SaaS/Alchemetrics/testing/VSG/Inventory/'

def extract_artist_name(file_name):
    # Split the filename to get the part after the hyphen and before the .csv
    artist_name = file_name.split('- ')[-1].replace('.csv', '')
    return artist_name

# Iterate through each CSV file
for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(folder_path, file_name)
        df = pd.read_csv(file_path)
        
        # Extract artist name from file name
        artist_name = extract_artist_name(file_name)
        
        # Add artist name to the DataFrame
        df['Artist'] = artist_name
        
        # Table name
        table_name = 'Inventory'
        
        # Create the MySQL Engine
        engine = create_engine('mysql+mysqlconnector://Justin:Password!@localhost/Vicinanza Studios & Gallery')
        
        # Fetch the last UID from the database
        with engine.connect() as connection:
            result = connection.execute(text(f"SELECT MAX(UID) FROM {table_name};"))
            last_uid = result.scalar()

        # If the table is empty, set last_uid to 0
        if last_uid is None:
            last_uid = 0

        # Adjust the UIDs in the DataFrame
        df['UID'] = range(last_uid + 1, last_uid + 1 + len(df))
        
        # Write the Dataframe to the MySQL Table
        try:
            df.to_sql(name=table_name, con=engine, if_exists='append', index=False)
            print(f'Data from {file_name} inserted successfully into MySQL table {table_name}')
        except Exception as e:
            print(f'Error inserting data from {file_name} into MySQL table {table_name}: {str(e)}')
