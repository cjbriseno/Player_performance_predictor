from nba_api.stats.endpoints import playergamelog
import os

# Example: Lebron James
player_id = '2544'

# Fetch game log
gamelog = playergamelog.PlayerGameLog(
    player_id = player_id,
    season = '2023-24'
)
print(f"\nFetching game log for player id: {player_id}...")

print("\nConverting to DataFrame...")
df = gamelog.get_data_frames()[0]
print(df.head())

print("\nSaving to CSV...")
save_path = "../data/raw/lebron_2023_24_gamelog.csv"
df.to_csv(save_path, index = False)
print(f"Saved to {os.path.abspath(save_path)}")