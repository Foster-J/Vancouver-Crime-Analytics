import pandas as pd
import sqlite3 as sql
from pathlib import Path

def create_database(db_path="database/vancouver_crime.db"):
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    conn = sql.connect(db_path)

    with open("sql/schema/create_tables.sql", 'r')as f:
        schema_sql = f.read()
        conn.executescript(schema_sql)

    with open("sql/indexes/create_indexes.sql")as f:
        index_sql = f.read()
        conn.executescript(index_sql)
    
    conn.commit()
    conn.close()
    
    print(f"Database created at: {db_path}")

def load_data(csv_path="data/cleaned/crime_cleaned.csv",
              db_path="database/vancouver_crime.db"):
    """Load cleaned data into db"""

    # Read Cleaned Data
    df = pd.read_csv(csv_path)

    #Connect to db
    conn = sql.connect(db_path)

    #Prepare data from crime_incidents table
    df_load = df[['TYPE', 'crime_category', 'datetime', 
                  'date', 'YEAR', 'MONTH', 'DAY', 'HOUR', 
                  'MINUTE','day_of_week', 'is_weekend', 
                  'quarter', 'time_of_day','HUNDRED_BLOCK', 
                  'NEIGHBOURHOOD', 'X', 'Y', 'has_coordinates'
                ]].copy()
    
    df_load.columns = ['crime_type', 'crime_category', 'incident_datetime', 
                       'incident_date','year', 'month', 'day',
                       'hour', 'minute','day_of_week', 'is_weekend',
                       'quarter', 'time_of_day','hundred_block', 'neighbourhood',
                       'x_coordinate', 'y_coordinate', 'has_coordinates'
                    ]
    
    #Load to db
    df_load.to_sql("crime_incidents", conn, if_exists='replace', index=False)

    print(f"Loaded {len(df_load)} to db")

    conn.close()

if __name__ =="__main__":
    create_database()
    load_data()
    print("Setup finished")