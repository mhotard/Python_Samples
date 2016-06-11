import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
        playFile.write(chunk)

 playFile.close()

 import bs4

 res = requests.get("https://automatetheboringstuff.com/chapter11/")
 res.raise_for_status()
 noStarchSoup = bs4.BeautifulSoup(res.text)
 type(noStarchSoup)

 elems = noStarchSoup.select('h2')
 type(elems)
 len(elems)
 type(elems[0])
 elems[0].getText()
 str(elems[0])

 res = requests.get("https://www.reddit.com/", headers = {'User-agent': 'your bot 0.1'})
 res.raise_for_status()
 noStarchSoup = bs4.BeautifulSoup(res.text)
 type(noStarchSoup)

 elems = noStarchSoup.select("a")
 type(elems)
 len(elems)
 type(elems[0])
 elems[0].getText()
 str(elems[0])

[print elems[i] if elems[i].attrs["class" ]== "choice" for i in range(len(elems))]

for i in range(len(elems)):
	if "title may-blank " in elems[i].attrs:

		if elems[i].attrs["title may-blank "]==["choice"]:
			print elems[i]


res = requests.get("http://www.accuweather.com/en/us/cambridge-ma/02139/daily-weather-forecast/329319?day=2")
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
type(soup)

elems = test_temp.select("wx:")

res = requests.get("https://www.reddit.com/r/asoiaf/")
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
type(soup)




