from nba_api.stats.endpoints import playergamelog

# Example: Lebron James
player_id = '2544'

gamelog = playergamelog.PlayerGameLog(
    player_id = player_id,
    season = '2023-24'
)

df = gamelog.get_data_frames()[0]

print(df.head())