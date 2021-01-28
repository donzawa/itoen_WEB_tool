import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Streamlit 超入門')

st.write('プレグレスバーの表示')
'Start!!'

bom = st.empty()
bar = st.progress(0)

for i in range(100):
    bom.text(f'爆発まであと{100 - i}')
    bar.progress(i + 1)
    time.sleep(0.07)

'Done!!!!!'


if st.checkbox('show Image'):
    img = Image.open('img36.jpg')
    st.image(img, caption='awabi odoriyaki', use_column_width = True)

option = st.selectbox(
    'あなたが好きなキャラクターを教えてください',
    ['たんじろう', 'ぜんいつ', 'いのすけ', 'ねずこ']
)
'あなたが好きなキャラクターは', option, 'です！'

text = st.text_input('あなたの趣味を教えてください。')
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'あなたの趣味→', text
'コンディション→', condition

# left_column, right_column = st.beta_columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')

expander = st.beta_expander('水の呼吸　一の型')
expander.write('みなもぎり')