import pandas as pd
import numpy as np
from datetime import datetime

YEARS = [2020, 2021, 2022, 2023, 2024]

def load_all_years(dp='data/raw/'):
    """
    Load and combine all years of crime data
    
    :param dp: Data path
    """
    #Data frames
    dfs = []
    for year in YEARS:
        try:
            df = pd.read_csv(f'{dp}crimedata_csv_AllNeighbourhoods_{year}.csv')
            dfs.append(df)
            print(f"{year} successfully loaded: {len(df)} records")
        except FileNotFoundError:
            print(f"{year} file not found")
    
    concatenated = pd.concat(dfs, ignore_index=True)
    print(f"\n Total records: {len(concatenated)}")
    return concatenated

def clean_data(df):
    df_clean = df.copy()

    #Create datetime column
    df_clean["datetime"] = pd.to_datetime( 
        df_clean[['YEAR',
                  'MONTH',
                  'DAY',
                  'HOUR',
                  'MINUTE']]
    )

    #Create date column
    df_clean["date"] = df_clean["datetime"].dt.date

    #Extract time
    df_clean["day_of_week"] = df_clean["datetime"].dt.day_name()
    df_clean["is_weekend"] = df_clean["datetime"].dt.dayofweek >= 5
    df_clean["quarter"] = df_clean["datetime"].dt.quarter
    df_clean["time_of_day"] = pd.cut(
        df_clean['HOUR'],
        bins=[0, 6, 12, 18, 24],
        labels=['NIGHT', 'MORNING', 'AFTERNOON', 'EVENING'],
        include_lowest=True
        )
    
    #Clean neighbourhood names
    df_clean["NEIGHBOURHOOD"] = df_clean["NEIGHBOURHOOD"].str.strip()

    #Create crime types
    def create_crime_types(crime_type):
        crime_type = crime_type.lower()
        
        if "theft" in crime_type:
            return "Property Crime - Theft"
        elif "break" in crime_type or "enter" in crime_type:
            return "Property Crime - Break & Enter"
        elif "mischief" in crime_type or "damage" in crime_type:
            return "Property Crime - Mischief"
        elif "vehicle" in crime_type and "collision" in crime_type:
            return "Vehicle Collision"
        elif "person" in crime_type or "assault" in crime_type:
            return "Violent Crime"
        else:
            return "Other"
    
    df_clean["crime_category"] = df_clean["TYPE"].apply(create_crime_types)
       
    #Remove rows with invalid dates
    df_clean = df_clean[df_clean['datetime'].notna()]
    
    #Sort by datetime
    df_clean = df_clean.sort_values('datetime').reset_index(drop=True)
    
    print(f"\nCleaning complete:")
    print(f"Records after cleaning: {len(df_clean)}")
    print(f"Date range: {df_clean['date'].min()} to {df_clean['date'].max()}")
    
    return df_clean

def save_clean_data(df, output_path='data/cleaned/crime_cleaned.csv'):
    df.to_csv(output_path, index=False)
    print(f"\n Saved cleaned data to: {output_path}")

if __name__ == "__main__":
    df_raw = load_all_years()
    df_clean = clean_data(df_raw)
    save_clean_data(df_clean)

    print(f"\nCrime categories:")
    print(df_clean['crime_category'].value_counts())
    print(f"\nTop 10 neighborhoods:")
    print(df_clean['NEIGHBOURHOOD'].value_counts().head(10))
