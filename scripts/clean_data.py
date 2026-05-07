import pandas as pd
import os

print("\nReading raw csv data...")
df = pd.read_csv("../data/raw/lebron_2023_24_gamelog.csv")

print("\nCleaning data...")
df = df[[
        "MATCHUP",
        "WL",
        "MIN",
        "FGM",
        "FGA",
        "FG_PCT",
        "FG3M",
        "FG3A",
        "FG3_PCT",
        "FTM",
        "FTA",
        "FT_PCT",
        "OREB",
        "DREB",
        "REB",
        "AST",
        "STL",
        "BLK",
        "TOV",
        "PF",
        "PTS",
        "PLUS_MINUS",
]]

print(df.columns)

print("\nSaving cleaned data to CSV...")
save_path = "../data/processed/lebron_2023_24_gamelog_cleaned.csv"
df.to_csv(save_path, index = False)
print(f"\nSaved to {os.path.abspath(save_path)}")
