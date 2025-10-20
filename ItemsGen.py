import requests

def get_latest_version():
    url = "https://ddragon.leagueoflegends.com/api/versions.json"
    resp = requests.get(url)
    resp.raise_for_status()
    versions = resp.json()
    return versions[0]

def fetch_items(version, locale="en_US"):
    url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/{locale}/item.json"
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()["data"]

    items = {}
    for key, meta in data.items():
        item_id = int(key)
        name = meta["name"].replace('"', "'")  
        items[item_id] = name
    return items

def save_items_as_tuples(items, path="lol_items.sql"):
    with open(path, "w", encoding="utf-8") as f:
        for item_id, name in sorted(items.items()):
            f.write(f'({item_id}, "{name}"),\n')

def main():
    version = get_latest_version()
    print("Latest Data Dragon version:", version)
    items = fetch_items(version)
    print("Number of items fetched:", len(items))
    save_items_as_tuples(items)
    print("Saved to lol_items.sql")

if __name__ == "__main__":
    main()
