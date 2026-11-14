import csv

output = "#EXTM3U"

try:
    with open("iptv/fonti/televisione.epg", "r") as fileEPG:
        output += " x-tvg-url=\"" + fileEPG.read() + "\""
except FileNotFoundError:
    pass

output += "\n\n"

with open("iptv/fonti/televisione.csv", "r") as fileCSV:
    data = csv.DictReader(fileCSV)

    for row in data:
        output += "#EXTINF:-1 "
        output += "tvg-name=\"" + row["Name"] + "\" "
        output += "tvg-logo=\"" + row["Logo"] + "\" "
        output += "group-title=\"" + row["Group"] + "\" "
        output += "tvg-id=\"" + row["ID"] + "\","
        output += row["Name"] + "\n"
        output += row["URL"] + "\n\n"

with open("iptv/playlist/televisione.m3u8", "w") as fileM3U:
    fileM3U.write(output)
