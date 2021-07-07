import collections
import csv

limit = 50

import re
import random

c = collections.Counter()
o = collections.Counter()

invalids = re.compile("0?(20|21|22|23|24|25|26|30|31|32|33|78|79|80|81)")
dics = {}
sets = set()
with open("JD2018_ListeEnluminures.csv", encoding="latin") as f:
	reader = csv.DictReader(f, delimiter=";")
	for line in reader:
		lot = line.get("LOT")
		image = line.get("IMAGE")
		if line.get("Division") != "Mss":
			continue
		if lot and line["Acceptée"] == "VRAI":
			url = f"{lot}.{image.replace('/', '_')}.jpg http://visualiseur.bnf.fr/ConsulterElementNum?O=IFN-{lot}&E=JPEG&Deb={image}&Fin={image}&Param=E"
			if url in sets:
				continue
			siecle = line["Dt"]
			o += collections.Counter([line["Dt"]])
			if "16" in siecle or "17" in siecle or "18" in siecle or "20" in siecle or "19" in siecle:
				continue
			elif "14" in siecle or "13" in siecle:
				if random.random() >= 0.2:
					continue
			elif "14" in siecle or "13" in siecle:
				if random.random() >= 0.2:
					continue
			elif "9" in siecle or "11" in siecle or "12" in siecle or "10" in siecle:
				if random.random() >= 0.3:
					continue
			elif "15" in siecle:
				if random.random() >= 0.15:
					continue
			else: 
				continue
			#if invalids.match(lot):
			#	continue
			c += collections.Counter([line["Dt"]])
			sets.add(url)
			dics[lot] = line
			limit -= 1

with open("mandragore.txt", "w") as f:
	f.write("\n".join(sets))

print(len(sets))
print(c)

for siecle in o:
	print(f"{siecle}	{o[siecle]}	{c.get(siecle, 0)}")