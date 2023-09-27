import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="古文単語ガチャ")

# タイトルと説明
st.title('古文単語ガチャ')

st.write('古文単語をランダムに表示して、勉強をサポートします！')
st.write('がんばってください！')

# Load the data
@st.cache
def load_data():
    return pd.read_excel("古文単語リスト.xlsx")

words_df = load_data()

# ガチャ機能
if st.button('ガチャを引く！'):
    rarity_probs = {
        'N': 0.4,
        'R': 0.3,
        'SR': 0.2,
        'SSR': 0.1
    }
    chosen_rarity = np.random.choice(list(rarity_probs.keys()), p=list(rarity_probs.values()))
    subset_df = words_df[words_df['レア度'] == chosen_rarity]
    selected_word = subset_df.sample().iloc[0]
    
    st.header(f"単語名: {selected_word['単語']}")
    st.subheader(f"レア度: {selected_word['レア度']}")

    # 意味を確認するボタンを追加
    if st.button('意味を確認する'):
        st.write(f"意味: {selected_word['意味']}")
