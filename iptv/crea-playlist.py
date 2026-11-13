import csv
from pathlib import Path

csvFile = Path("iptv/iptv-televisione.csv")
if csvFile.exists():
    print("CSV esiste")

m3uFile = Path("iptv/iptv-televisione.m3u8")
if m3uFile.exists():
    print("M3U8 esiste")

with open("iptv/iptv-televisione.csv", "r") as f:
    data = csv.DictReader(f)
    for row in data:
        output = ("#EXTINF: -1 tvg-name=\"" + row["Name"] + "\"," + row["Name"] + "\n")
        output += (row["URL"] + "\n")
        print(output)

with open("iptv/iptv-televisione.m3u8", "w") as fileM3U:
    fileM3U.write(output)
