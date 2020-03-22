import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

musics_info = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
rank = 0

for music_info in musics_info:
    title_el = music_info.select('td.info > a.title.ellipsis')
    artist_el = music_info.select('td.info > a.artist.ellipsis')

    if title_el:
        rank = rank + 1
        title = title_el[0].text
        artist = artist_el[0].text
        print(rank, title.lstrip(), artist)

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1)