import pandas as pd
import requests
from bs4 import BeautifulSoup

area1_hotels = ['熱海ニューフジヤホテル', '熱海 金城館', 'ホテル大野屋', 'アタミシーズンホテル']
area2_hotels = ['伊東園ホテル箱根湯本', 'ホテル四季彩', '伊東園ホテル熱海館', 'ウオミサキホテル']
area3_hotels = ['伊東園ホテル', '伊東園ホテル別館', '伊東園ホテル松川館', '熱川ハイツ', '伊東園ホテル熱川', '伊東園ホテル稲取']
area4_hotels = ['下田伊東園ホテルはな岬', '下田海浜ホテル', '伊東園ホテル土肥', '西伊豆クリスタルビューホテル', '西伊豆松崎伊東園ホテル', '大仁ホテル', '伊豆長岡金城館']
area5_hotels = ['伊香保グランドホテル', '金太夫', '伊香保温泉とどろき', '伊東園ホテル四万', '伊東園ホテル尾瀬老神山楽荘', 'ホテル湯の陣', '伊東園ホテル草津', 'ホテル湯元']
area6_hotels = ['白樺湖ビューホテル', '伊東園ホテル浅間の湯', 'リバーサイド上田館', '小諸グランドキャッスルホテル', 'ホテル水明館', '上諏訪温泉 油屋旅館', '彦根ビューホテル']
area7_hotels = ['湯の川観光ホテル祥苑', '南国ホテル', 'ホテル奥久慈館', '鬼怒川ロイヤルホテル', '伊東園ホテルニューさくら', '一柳閣本館']
area8_hotels = ['伊東園ホテル塩原', 'ホテルニューもみぢ', 'ホテル湯西川', '東山パークホテル新風月', '伊東園ホテル飯坂 叶や', '鏡が池 碧山亭', '伊東園ホテル磐梯向滝']

area1_url = ['', '', '', '', '', '', '', '']
area2_url = ['', '', '', '', '', '', '', '']
area3_url = ['', '', '', '', '', '', '', '']
area4_url = ['', '', '', '', '', '', '', '']
area5_url = ['339927', '347217', '379726', '304926', '324185', '315400', '304574', '312288']
area6_url = ['', '', '', '', '', '', '', '']
area7_url = ['', '', '', '', '', '', '', '']
area8_url = ['', '', '', '', '', '', '', '']

def kuchikomi(area_hotel, area_url):
    data = []
    a = 0
    while a <= len(area_hotel) - 1:
        num = area_url[a]
        url = 'https://www.jalan.net/yad' + num + '/kuchikomi/'
        hotel = area_hotel[a]
        a += 1

        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')

        categoryItems = soup.find_all('th')
        kuchikomi_points = soup.find_all('td', attrs={'class': 'jlnpc-kuchikomi__catTable__point'})

        details = {}

        x = 0
        while x <= len(categoryItems) - 1:
            details[categoryItems[x].text] = float(kuchikomi_points[x].text)
            x += 1

        datum = details

        datum['ホテル名'] = hotel
        datum[soup.dt.text] = float(soup.find_all('span', attrs={'class', 'jlnpc-kuchikomi__point'})[0].text)

        data.append(datum)

    # df = pd.DataFrame(data)
    # df = df[['ホテル名', '総合', '部屋', '風呂', '料理（朝食）', '料理（夕食）', '接客・サービス', '清潔感']]
    return data

def oo(a, b):
    return a + b
