import requests
from bs4 import BeautifulSoup



class scrap20:


    async def rubl_dollar(self):
        URL = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0&oq=%D0%BA%D1%83%D1%80%D1%81&aqs=chrome.0.0i131i433i512l8j0i131i433j0i131i433i512.1587j0j15&sourceid=chrome&ie=UTF-8'
        HEADERS = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
        html = requests.get(URL, headers = HEADERS)

        soup = BeautifulSoup(html.text, 'html.parser')
    
        items = soup.find_all('div', class_ ='VgAgW PZPZlf')
   
        datas = []

        for item in items:
            datas.append(
                item.find('span',class_ = 'DFlfde SwHCTb').get_text()#old code
        )

        return datas[0]

    async def rubl_euro(self):
        URL = 'https://www.google.com/search?q=%D0%9A%D0%A3%D0%A0%D0%A1+%D0%95%D0%92%D0%A0%D0%9E&oq=%D0%9A%D0%A3%D0%A0%D0%A1+%D0%95%D0%92%D0%A0%D0%9E&aqs=chrome..69i57j0i131i433i512j0i433i512j0i131i433i512j0i512j0i131i433i512l3j0i433i512l2.6108j1j7&sourceid=chrome&ie=UTF-8'
        HEADERS = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}
        html = requests.get(URL, headers = HEADERS)

        soup = BeautifulSoup(html.text, 'html.parser')
    
        items = soup.find_all('div', class_ ='dDoNo ikb4Bb gsrt')
   
        datas = []

        for item in items:
            datas.append(
                item.find('span',class_ = 'DFlfde SwHCTb').get_text()#old code
        )

        return datas[0]