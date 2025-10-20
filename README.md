## League of Legends Relational Database for Match Prediction

### Context

This dataset contains detailed match and player data from League of Legends, one of the most popular multiplayer online battle arena (MOBA) games in the world. It includes 35,000 matches and contains 78,000 summoner statistics, capturing a wide range of in-game statistics, such as champion selection, player performance metrics, match outcomes, and more.

The dataset is structured to support a variety of analyses, including:

- Predicting match outcomes based on team compositions and player stats
- Evaluating player performance and progression over time
- Exploring trends in champion popularity and win rates
- Building machine learning models for esports analytics

Whether you are interested in competitive gaming, data science, or predictive modeling, this dataset provides a rich source of structured data to explore the dynamics of League of Legends at scale.

### Dataset Information

Data was collected from Riot Games API using Python script(link) from Patch 25.19 

The datase consists of 7 csv files:

- **MatchStatsTbl** - Match Stats given a summonerID and MatchID.Contains K/D/A, Items, Runes,Ward Score, Summoner Spells, Baron Kills, Dragon Kills, Lane, DmgTaken/Dealt, Total Gold, cs,Mastery Points and Win/Loss
- **TeamMatchStatsTbl** - Containes Red/Blue Champions,Red/Blue BaronKills,Blue/Red Turret Kills, Red/Blue Kills, RiftHearaldKills and Win/loss
-**MatchTbl**- Contains MatchID,Rank,Match Duration and MatchType.
-**RankTbl **- Contains RankID and RankName
-**ChampionTbl**- Contains ChampionID and ChampionName 
-**ItemTbl** - Contains ItemID,ItemName and ItemLink(Image) 
-**SummonerTbl** - Contains SummonerID and SummonerName
-**SummonerMatchTbl** - Links MatchID,SummonerID and ChampionID

### Database Features

- This dataset contains 35,422 League of Legends matches and 78,863 summoner statistics from those games.
- Uses Data from over 2,381 summoners.
- Consists of data only from Europe West(EUW)
- Data is sampled from Unranked to Challenger tiers.

### Limitations

The Riot API only provides the "BOTTOM" lane for bot-lane players.
During Data collection, roles were inferred by combining chapions that often played support with CS metrics to distinguish ADC vs Support — especially for ambiguous picks like Senna or off-meta choices.

### Acknowledgements/Privacy

Data is collected using the official Riot Games API. We thank Riot Games for providing the data and tools that make this project possible. This dataset is not endorsed or certified by Riot Games.
No personal or identifiable player data (e.g., Summoner Names, Summoner IDs, or PUUIDs) are included.
The SummonerTbl has been intentionally excluded from this public release.

### Running the Database

```
mysql -u league_user -pmysql -u league_user -p
USE LeagueStats;
```

Copy and Paste the 'TableSetupNoData.txt' script into the terminal, Then open the CollectSummoner.py file and enter a summoner name (Line 56, seen below) and run the script which will populate a text file. After this run the DataCollection.py Script to start populating the database.

```python
if __name__ == "__main__":
    start_summoner_name = ""
    region_start = "europe"
    tagline = "EUW "
    output_file = "summoner_names.txt"
    collect_summoner_names(start_summoner_name, region_start, tagline, output_file)
```
## Find the Dataset on [Kaggle](https://www.kaggle.com/datasets/nathansmallcalder/lol-match-history-and-summoner-data-80k-matches)

## Config File

to run the project you will need a Riot Games API Key then create a config.py file.

```python
api_key = "RGAPI"
```
