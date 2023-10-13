import streamlit as st
import random
import time

st.title("ダイススピンアプリ")

spinning = st.checkbox("スピン中")
result = None

if spinning:
    result = random.randint(1, 40)
    st.write(f"ルーレットがスピン中... 結果: {result}")
else:
    st.write("ルーレットが停止しました。最終結果:", result)
