import requests
import time
import config
from RiotApiCalls import getPuuid

def collect_summoner_names(start_summoner_name, region_start, tagline, output_file, depth=1):
    api_key = config.api_key
    collected_names = set()
    current_summoner_name = start_summoner_name

    try:
        Summoner = getPuuid(region_start, current_summoner_name, tagline)
        puuid = Summoner['puuid']
        collected_names.add((current_summoner_name, tagline))
        print(f"Collected starting summoner: {current_summoner_name}#{tagline}")

        # Get last 20 match IDs
        match_url = f"https://{region_start}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"
        params = {'start': 0, 'count': 20, 'api_key': api_key}
        MatchIDs = requests.get(match_url, params=params).json()

        for MatchId in MatchIDs:
            match_data_url = f"https://{region_start}.api.riotgames.com/lol/match/v5/matches/{MatchId}"
            try:
                r = requests.get(match_data_url, params={'api_key': api_key})
                if r.status_code == 429:
                    print("Rate limited. Sleeping for 10 seconds...")
                    time.sleep(10)
                    continue
                MatchData = r.json()
                if 'info' not in MatchData or 'participants' not in MatchData['info']:
                    continue

                for participant in MatchData['info']['participants']:
                    name = participant.get('riotIdGameName')
                    tag = participant.get('riotIdTagline', '')
                    if name and tag:
                        collected_names.add((name, tag))

            except Exception as e:
                print(f"Error fetching match {MatchId}: {e}")
            time.sleep(1)  # rate limit safety

    except Exception as e:
        print(f"Error collecting from {current_summoner_name}: {e}")

    # Write results
    with open(output_file, 'a', encoding='utf-8') as f:
        for name, tag in collected_names:
            f.write(f"{name} #{tag}\n")

    print(f"Saved {len(collected_names)} names to {output_file}")


if __name__ == "__main__":
    start_summoner_name = "Andolos"
    region_start = "europe"
    tagline = "EUW "
    output_file = "summoner_names.txt"
    collect_summoner_names(start_summoner_name, region_start, tagline, output_file)
