import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
import kuchikomi_kinugawa_test as ku



area = ['熱海リゾートエリア', '熱海78エリア', '伊東・東伊豆エリア', '中伊豆・西伊豆・下田エリア', '群馬・新潟エリア', '長野エリア', '栃木・茨城・千葉・北海道エリア', '塩原・東北エリア']

area1_hotels = ['熱海ニューフジヤホテル', '熱海 金城館', 'ホテル大野屋', 'アタミシーズンホテル']
area2_hotels = ['伊東園ホテル箱根湯本', 'ホテル四季彩', '伊東園ホテル熱海館', 'ウオミサキホテル']
area3_hotels = ['伊東園ホテル', '伊東園ホテル別館', '伊東園ホテル松川館', '熱川ハイツ', '伊東園ホテル熱川', '伊東園ホテル稲取']
area4_hotels = ['下田伊東園ホテルはな岬', '下田海浜ホテル', '伊東園ホテル土肥', '西伊豆クリスタルビューホテル', '西伊豆松崎伊東園ホテル', '大仁ホテル', '伊豆長岡金城館']
area5_hotels = ['伊香保グランドホテル', '金太夫', '伊香保温泉とどろき', '伊東園ホテル四万', '伊東園ホテル尾瀬老神山楽荘', 'ホテル湯の陣', '伊東園ホテル草津', 'ホテル湯元']
area6_hotels = ['白樺湖ビューホテル', '伊東園ホテル浅間の湯', 'リバーサイド上田館', '小諸グランドキャッスルホテル', 'ホテル水明館', '上諏訪温泉 油屋旅館', '彦根ビューホテル']
area7_hotels = ['湯の川観光ホテル祥苑', '南国ホテル', 'ホテル奥久慈館', '鬼怒川ロイヤルホテル', '伊東園ホテルニューさくら', '一柳閣本館']
area8_hotels = ['伊東園ホテル塩原', 'ホテルニューもみぢ', 'ホテル湯西川', '東山パークホテル新風月', '伊東園ホテル飯坂 叶や', '鏡が池 碧山亭', '伊東園ホテル磐梯向滝']

area1_url = ['311258', '322538', '320536', '339986']
area2_url = ['311769', '346639', '338065', '302560']
area3_url = ['305149', '328682', '340042', '304515', '309109', '322061']
area4_url = ['323164', '341883', '339290', '363720', '315294', '310115', '310148']
area5_url = ['339927', '347217', '379726', '304926', '324185', '315400', '304574', '312288']
area6_url = ['327550', '357704', '311782', '308220', '329500', '346367', '329088']
area7_url = ['331966', '314616', '336960', '327886', '347277', '357172']
area8_url = ['314287', '315528', '350554', '357960', '329711', '301765', '362287']



menu1 = st.beta_expander('じゃらん口コミ点数確認')

with menu1.beta_container():
    kuchikomi_column1, kuchikomi_column2, = st.beta_columns((1, 1))
    kuchi_check1 = kuchikomi_column1.checkbox(area[0], key='1')
    kuchi_check2 = kuchikomi_column2.checkbox(area[1], key='1')
    kuchi_check3 = kuchikomi_column1.checkbox(area[2], key='1')
    kuchi_check4 = kuchikomi_column2.checkbox(area[3], key='1')
    kuchi_check5 = kuchikomi_column1.checkbox(area[4], key='1')
    kuchi_check6 = kuchikomi_column2.checkbox(area[5], key='1')
    kuchi_check7 = kuchikomi_column1.checkbox(area[6], key='1')
    kuchi_check8 = kuchikomi_column2.checkbox(area[7], key='1')

    if kuchi_check1:
        st.subheader(f'<{area[0]}　口コミデータ>')
        data = ku.kuchikomi(area1_hotels, area1_url)
        df = pd.DataFrame(data)
        df = df[['ホテル名', '総合', '部屋', '風呂', '料理（朝食）', '料理（夕食）', '接客・サービス', '清潔感']]
        st.dataframe(df)
        st.button(f'{area[0]}　CSVデータDownLoad')

    if kuchi_check2:
        st.subheader(f'<{area[1]}　　口コミデータ>')
        data = ku.kuchikomi(area2_hotels, area2_url)
        df = pd.DataFrame(data)
        df = df[['ホテル名', '総合', '部屋', '風呂', '料理（朝食）', '料理（夕食）', '接客・サービス', '清潔感']]
        st.dataframe(df)
        st.button(f'{area[1]} CSVデータDownLoad')

    if kuchi_check3:
        st.subheader(f'<{area[2]}　　口コミデータ>')
        data = ku.kuchikomi(area3_hotels, area3_url)
        df = pd.DataFrame(data)
        df = df[['ホテル名', '総合', '部屋', '風呂', '料理（朝食）', '料理（夕食）', '接客・サービス', '清潔感']]
        st.dataframe(df)
        st.button(f'{area[2]}  CSVデータDownLoad')

    if kuchi_check4:
        st.subheader(f'<{area[3]}　　口コミデータ>')
        data = ku.kuchikomi(area4_hotels, area4_url)
        df = pd.DataFrame(data)
        df = df[['ホテル名', '総合', '部屋', '風呂', '料理（朝食）', '料理（夕食）', '接客・サービス', '清潔感']]
        st.dataframe(df)
        st.button(f'{area[3]}  CSVデータDownLoad')

    if kuchi_check5:
        st.subheader(f'<{area[4]}　　口コミデータ>')
        data = ku.kuchikomi(area5_hotels, area5_url)
        df = pd.DataFrame(data)
        df = df[['ホテル名', '総合', '部屋', '風呂', '料理（朝食）', '料理（夕食）', '接客・サービス', '清潔感']]
        st.dataframe(df)
        st.button(f'{area[4]}  CSVデータDownLoad')

    if kuchi_check6:
        st.subheader(f'<{area[5]}　　口コミデータ>')
        data = ku.kuchikomi(area6_hotels, area6_url)
        df = pd.DataFrame(data)
        df = df[['ホテル名', '総合', '部屋', '風呂', '料理（朝食）', '料理（夕食）', '接客・サービス', '清潔感']]
        st.dataframe(df)
        st.button(f'{area[5]}  CSVデータDownLoad')

    if kuchi_check7:
        st.subheader(f'<{area[6]}　　口コミデータ>')
        data = ku.kuchikomi(area7_hotels, area7_url)
        df = pd.DataFrame(data)
        df = df[['ホテル名', '総合', '部屋', '風呂', '料理（朝食）', '料理（夕食）', '接客・サービス', '清潔感']]
        st.dataframe(df)
        st.button(f'{area[6]}  CSVデータDownLoad')

    if kuchi_check8:
        st.subheader(f'<{area[7]}　　口コミデータ>')
        data = ku.kuchikomi(area8_hotels, area8_url)
        df = pd.DataFrame(data)
        df = df[['ホテル名', '総合', '部屋', '風呂', '料理（朝食）', '料理（夕食）', '接客・サービス', '清潔感']]
        st.dataframe(df)
        st.button(f'{area[7]}  CSVデータDownLoad')




df = pd.DataFrame(data)
df = df[['ホテル名', 'URL', '総合', '部屋', '風呂', '料理（朝食）', '料理（夕食）', '接客・サービス', '清潔感']]
df.to_csv('じゃらん口コミ（鬼怒川温泉）.csv', index = False)

st.subheader('')

menu2 = st.beta_expander('販売状況確認')

with menu2.beta_container():
    hanbai_column1, hanbai_column2, = st.beta_columns((1, 1))
    hanbai_check1 = hanbai_column1.checkbox(area[0], key='2')
    hanbai_check2 = hanbai_column2.checkbox(area[1], key='2')
    hanbai_check3 = hanbai_column1.checkbox(area[2], key='2')
    hanbai_check4 = hanbai_column2.checkbox(area[3], key='2')
    hanbai_check5 = hanbai_column1.checkbox(area[4], key='2')
    hanbai_check6 = hanbai_column2.checkbox(area[5], key='2')
    hanbai_check7 = hanbai_column1.checkbox(area[6], key='2')
    hanbai_check8 = hanbai_column2.checkbox(area[7], key='2') 

    if hanbai_check1:
        st.subheader(f'<{area[0]}　販売状況一覧>')
    if hanbai_check2:
        st.subheader(f'<{area[0]}　販売状況一覧>')
    if hanbai_check3:
        st.subheader(f'<{area[0]}　販売状況一覧>')
    if hanbai_check4:
        st.subheader(f'<{area[0]}　販売状況一覧>')
    if hanbai_check5:
        st.subheader(f'<{area[0]}　販売状況一覧>')
    if hanbai_check6:
        st.subheader(f'<{area[0]}　販売状況一覧>')
    if hanbai_check7:
        st.subheader(f'<{area[0]}　販売状況一覧>')
    if hanbai_check8:
        st.subheader(f'<{area[0]}　販売状況一覧>')    









