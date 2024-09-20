import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="英語構文ガチャ")

# タイトルと説明
st.title('英語構文ガチャ')

st.write('英語の構文をランダムに表示します。')

# Load the data
@st.cache
def load_data():
    return pd.read_csv("untitled.xlsx")

words_df = load_data()

# ガチャ機能
if st.button('ガチャを引く！(英→日)'):
    selected_word = words_df.sample().iloc[0]
    
    # セッションステートに選択された単語を保存
    st.session_state.selected_word = selected_word
    st.session_state.display_meaning = False

if 'selected_word' in st.session_state:
    st.header(f"英文: {st.session_state.selected_word['english']}")

    # 意味を確認するボタンを追加
    if st.button('和訳を確認する'):
        st.session_state.display_meaning = True

    if st.session_state.display_meaning:
        st.write(f"和訳: {st.session_state.selected_word['japanese']}")

if st.button('ガチャを引く！(日→英)'):
    selected_word = words_df.sample().iloc[0]
    
    # セッションステートに選択された単語を保存
    st.session_state.selected_word = selected_word
    st.session_state.display_meaning = False

if 'selected_word' in st.session_state:
    st.header(f"和文: {st.session_state.selected_word['japanese']}")

    # 意味を確認するボタンを追加
    if st.button('英訳を確認する'): 
        st.session_state.display_meaning = True

    if st.session_state.display_meaning:
        st.write(f"英訳: {st.session_state.selected_word['english']}")
