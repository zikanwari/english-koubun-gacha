import streamlit as st
import random
import time

st.title("ルーレットゲーム")

# ルーレットセクションの数
num_sections = 40

spinning = False

# ルーレットをスタート/ストップするためのボタン
start_stop_button = st.button("ルーレットをスタート/ストップ", key="start_stop_button")

if start_stop_button:
    spinning = True
    result = None
    while spinning:
        result = random.randint(1, num_sections)
        st.write(f"ルーレットがスピン中... 結果: {result}")
        time.sleep(0.5)
        stop_button = st.button("ルーレットをストップ", key="stop_button")
        spinning = not stop_button
    
    st.write(f"ルーレットが停止しました。最終結果: {result}")
