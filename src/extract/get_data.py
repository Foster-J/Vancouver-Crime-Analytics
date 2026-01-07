import pandas as pd

OFFSET = "OFFSET TO PROTECT PRIVACY"
RESTRICTED = "Restricted"

crimestats_2020 = "data/raw/crimedata_csv_AllNeighbourhoods_2020.csv" 
crimestats_2021 = "data/raw/crimedata_csv_AllNeighbourhoods_2021.csv"
crimestats_2022 = "data/raw/crimedata_csv_AllNeighbourhoods_2022.csv"
crimestats_2023 = "data/raw/crimedata_csv_AllNeighbourhoods_2023.csv"
crimestats_2024 = "data/raw/crimedata_csv_AllNeighbourhoods_2024.csv"
string_cols = ["TYPE", "HUNDRED_BLOCK", "NEIGHBOURHOOD"]

df = pd.read_csv(crimestats_2020)

#Returns number of rows and cols
# print("Dataset Shape", df.shape)
# print("\nColumn names and types:")
# print(df.dtypes)

#Drop irrelevent columns
# df = df.drop(columns=["HUNDRED_BLOCK"])

#Replacing value from hundred block col
df["HUNDRED_BLOCK"] = df["HUNDRED_BLOCK"].replace({"OFFSET TO PROTECT PRIVACY": "Restricted"})
print(df.iloc[0:10])