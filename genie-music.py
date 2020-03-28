import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
url='https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309'
data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

musices = soup.select('#body-content > div.newest-list > div > table > tbody > tr > td.info')

rank=1
for music in musices:
    title = music.select_one('a.title.ellipsis')
    music_title=title.text.strip()

    artist = music.select_one('a.artist.ellipsis')
    if music_title is not None:
        print(rank, '위', music_title, artist.text)
        rank=rank+1

