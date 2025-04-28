print('hello world')

import pandas as pd

url_spotify = "https://gist.githubusercontent.com/cooneycw/b4021d5d872ee4a07239f0ea25c23cd7/raw/spotify_data.csv"
url_nba_stats = "https://gist.githubusercontent.com/cooneycw/a90ce2c2adf1208cfc6359c4fa83d928/raw/nba_stats.csv"

# Read the CSV directly into a pandas DataFrame
df_spotify = pd.read_csv(url_spotify)
df_nba_stats = pd.read_csv(url_nba_stats)

# Now you can work with the data
