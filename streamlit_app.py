import streamlit as st
import random

st.title("ルーレットゲーム")

spinning = False
result = None

if not spinning:
    if st.button("スタート"):
        spinning = True
        result = random.randint(1, 40)
else:
    if st.button("ストップ"):
        spinning = False

if spinning:
    st.write(f"ルーレットがスピン中... 結果: {result}")
else:
    st.write("ルーレットが停止しました。最終結果: {result}")
