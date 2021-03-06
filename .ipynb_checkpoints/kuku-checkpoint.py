{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import requests\n",
    "from bs4 import BeautifulSoup"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "area1_hotels = ['熱海ニューフジヤホテル', '熱海 金城館', 'ホテル大野屋', 'アタミシーズンホテル']\n",
    "area2_hotels = ['伊東園ホテル箱根湯本', 'ホテル四季彩', '伊東園ホテル熱海館', 'ウオミサキホテル']\n",
    "area3_hotels = ['伊東園ホテル', '伊東園ホテル別館', '伊東園ホテル松川館', '熱川ハイツ', '伊東園ホテル熱川', '伊東園ホテル稲取']\n",
    "area4_hotels = ['下田伊東園ホテルはな岬', '下田海浜ホテル', '伊東園ホテル土肥', '西伊豆クリスタルビューホテル', '西伊豆松崎伊東園ホテル', '大仁ホテル', '伊豆長岡金城館']\n",
    "area5_hotels = ['伊香保グランドホテル', '金太夫', '伊香保温泉とどろき', '伊東園ホテル四万', '伊東園ホテル尾瀬老神山楽荘', 'ホテル湯の陣', '伊東園ホテル草津', 'ホテル湯元']\n",
    "area6_hotels = ['白樺湖ビューホテル', '伊東園ホテル浅間の湯', 'リバーサイド上田館', '小諸グランドキャッスルホテル', 'ホテル水明館', '上諏訪温泉 油屋旅館', '彦根ビューホテル']\n",
    "area7_hotels = ['湯の川観光ホテル祥苑', '南国ホテル', 'ホテル奥久慈館', '鬼怒川ロイヤルホテル', '伊東園ホテルニューさくら', '一柳閣本館']\n",
    "area8_hotels = ['伊東園ホテル塩原', 'ホテルニューもみぢ', 'ホテル湯西川', '東山パークホテル新風月', '伊東園ホテル飯坂 叶や', '鏡が池 碧山亭', '伊東園ホテル磐梯向滝']\n",
    "\n",
    "area5_url = ['339927', '347217', '379726', '304926', '324185', '315400', '304574', '312288']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [],
   "source": [
    "# def kuchi(area_hotel, area_url):\n",
    "#     a = 0\n",
    "#     while a <= len(area_hotel) - 1:\n",
    "#         num = area_url[a]\n",
    "#         url = 'https://www.jalan.net/yad' + num + '/kuchikomi/'\n",
    "#         hotel = area_hotel[a]\n",
    "#         res = requests.get(url)\n",
    "#         soup = BeautifulSoup(res.content, 'html.parser')\n",
    "\n",
    "#         categoryItems = soup.find_all('th')\n",
    "#         kuchikomi_points = soup.find_all('td', attrs={'class': 'jlnpc-kuchikomi__catTable__point'})\n",
    "        \n",
    "#         details = {}\n",
    "#         x = 0\n",
    "#         while x <= len(categoryItems) - 1:\n",
    "#             details[categoryItems[x].text] = float(kuchikomi_points[x].text)\n",
    "#             x += 1\n",
    "        \n",
    "#         datum = details\n",
    "\n",
    "#         datum['ホテル名'] = hotel\n",
    "#         datum[soup.dt.text] = float(soup.find_all('span', attrs={'class', 'jlnpc-kuchikomi__point'})[0].text)\n",
    "\n",
    "#         data.append(datum)\n",
    "#         a += 1\n",
    "        \n",
    "    \n",
    "#     return data\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [],
   "source": [
    "# kuchi(area5_hotels, area5_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "def aiueo(area_hotel, area_url):\n",
    "    data = []\n",
    "    a = 0\n",
    "    while a <= len(area_hotel) - 1:\n",
    "        num = area_url[a]\n",
    "        url = 'https://www.jalan.net/yad' + num + '/kuchikomi/'\n",
    "        hotel = area_hotel[a]\n",
    "        a += 1\n",
    "\n",
    "        res = requests.get(url)\n",
    "        soup = BeautifulSoup(res.content, 'html.parser')\n",
    "\n",
    "        categoryItems = soup.find_all('th')\n",
    "        kuchikomi_points = soup.find_all('td', attrs={'class': 'jlnpc-kuchikomi__catTable__point'})\n",
    "\n",
    "        details = {}\n",
    "\n",
    "        x = 0\n",
    "        while x <= len(categoryItems) - 1:\n",
    "            details[categoryItems[x].text] = float(kuchikomi_points[x].text)\n",
    "            x += 1\n",
    "\n",
    "        datum = details\n",
    "\n",
    "        datum['ホテル名'] = hotel\n",
    "        datum[soup.dt.text] = float(soup.find_all('span', attrs={'class', 'jlnpc-kuchikomi__point'})[0].text)\n",
    "\n",
    "        data.append(datum)\n",
    "\n",
    "    df = pd.DataFrame(data)\n",
    "    df = df[['ホテル名', '総合', '部屋', '風呂', '料理（朝食）', '料理（夕食）', '接客・サービス', '清潔感']]\n",
    "    return df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ホテル名</th>\n",
       "      <th>総合</th>\n",
       "      <th>部屋</th>\n",
       "      <th>風呂</th>\n",
       "      <th>料理（朝食）</th>\n",
       "      <th>料理（夕食）</th>\n",
       "      <th>接客・サービス</th>\n",
       "      <th>清潔感</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>伊香保グランドホテル</td>\n",
       "      <td>3.4</td>\n",
       "      <td>3.3</td>\n",
       "      <td>3.7</td>\n",
       "      <td>3.4</td>\n",
       "      <td>3.2</td>\n",
       "      <td>3.5</td>\n",
       "      <td>3.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>金太夫</td>\n",
       "      <td>3.7</td>\n",
       "      <td>3.5</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.5</td>\n",
       "      <td>3.4</td>\n",
       "      <td>3.7</td>\n",
       "      <td>3.3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>伊香保温泉とどろき</td>\n",
       "      <td>3.6</td>\n",
       "      <td>3.7</td>\n",
       "      <td>3.5</td>\n",
       "      <td>3.4</td>\n",
       "      <td>3.5</td>\n",
       "      <td>3.4</td>\n",
       "      <td>3.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>伊東園ホテル四万</td>\n",
       "      <td>3.4</td>\n",
       "      <td>3.0</td>\n",
       "      <td>4.1</td>\n",
       "      <td>3.5</td>\n",
       "      <td>3.5</td>\n",
       "      <td>3.6</td>\n",
       "      <td>3.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>伊東園ホテル尾瀬老神山楽荘</td>\n",
       "      <td>3.3</td>\n",
       "      <td>3.3</td>\n",
       "      <td>3.8</td>\n",
       "      <td>3.4</td>\n",
       "      <td>3.3</td>\n",
       "      <td>3.0</td>\n",
       "      <td>2.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>ホテル湯の陣</td>\n",
       "      <td>3.5</td>\n",
       "      <td>3.6</td>\n",
       "      <td>3.9</td>\n",
       "      <td>3.3</td>\n",
       "      <td>3.3</td>\n",
       "      <td>3.3</td>\n",
       "      <td>3.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>伊東園ホテル草津</td>\n",
       "      <td>3.7</td>\n",
       "      <td>3.7</td>\n",
       "      <td>4.2</td>\n",
       "      <td>3.5</td>\n",
       "      <td>3.5</td>\n",
       "      <td>3.6</td>\n",
       "      <td>3.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>ホテル湯元</td>\n",
       "      <td>3.2</td>\n",
       "      <td>3.3</td>\n",
       "      <td>3.8</td>\n",
       "      <td>3.3</td>\n",
       "      <td>3.1</td>\n",
       "      <td>3.2</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "            ホテル名   総合   部屋   風呂  料理（朝食）  料理（夕食）  接客・サービス  清潔感\n",
       "0     伊香保グランドホテル  3.4  3.3  3.7     3.4     3.2      3.5  3.1\n",
       "1            金太夫  3.7  3.5  4.0     3.5     3.4      3.7  3.3\n",
       "2      伊香保温泉とどろき  3.6  3.7  3.5     3.4     3.5      3.4  3.2\n",
       "3       伊東園ホテル四万  3.4  3.0  4.1     3.5     3.5      3.6  3.1\n",
       "4  伊東園ホテル尾瀬老神山楽荘  3.3  3.3  3.8     3.4     3.3      3.0  2.8\n",
       "5         ホテル湯の陣  3.5  3.6  3.9     3.3     3.3      3.3  3.2\n",
       "6       伊東園ホテル草津  3.7  3.7  4.2     3.5     3.5      3.6  3.7\n",
       "7          ホテル湯元  3.2  3.3  3.8     3.3     3.1      3.2  3.0"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "aiueo(area5_hotels, area5_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
