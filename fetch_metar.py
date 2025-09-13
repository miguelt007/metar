import requests
import re
import json

icao = "LPPT"
url = f"https://aviationweather.gov/data/metar/data.txt?ids={icao}&format=raw"

res = requests.get(url)
text = res.text

match = re.search(rf"{icao}\s+\d{{6}}Z.*", text)
metar = match.group(0).strip() if match else "METAR não encontrado."

with open("metar.json", "w") as f:
    json.dump({"icao": icao, "metar": metar}, f, indent=2)
