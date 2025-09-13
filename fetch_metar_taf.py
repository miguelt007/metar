import requests
import re
import json

icao = "LPPT"

# METAR
metar_url = f"https://aviationweather.gov/data/metar/data.txt?ids={icao}&format=raw"
metar_res = requests.get(metar_url)
metar_match = re.search(rf"{icao}\s+\d{{6}}Z.*", metar_res.text)
metar = metar_match.group(0).strip() if metar_match else "METAR não encontrado."

# TAF
taf_url = f"https://aviationweather.gov/data/taf/data.txt?ids={icao}&format=raw"
taf_res = requests.get(taf_url)
taf_match = re.search(rf"{icao}\s+TAF\s+\d{{6}}Z.*", taf_res.text)
taf = taf_match.group(0).strip() if taf_match else "TAF não encontrado."

# Salvar
with open("metar.json", "w") as f:
    json.dump({"icao": icao, "metar": metar}, f, indent=2)

with open("taf.json", "w") as f:
    json.dump({"icao": icao, "taf": taf}, f, indent=2)
