import csv

with open("iptv-televisione.csv", "r") as f:
    data = csv.DictReader(f)
    for row in data:
        output = ("#EXTINF: -1 tvg-name=\"" + row["Name"] + "\"," + row["Name"] + "\n")
        output += (row["URL"] + "\n")
        print(output)

with open("iptv-televisione.m3u8", "w") as fileM3U:
    fileM3U.write(output)
