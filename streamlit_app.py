import streamlit as st
import random
import time

st.title("ダイススピンアプリ")

spinning = st.checkbox("スピン中")
result = None

while spinning:
    result = random.randint(1, 40)
    st.write(f"ルーレットがスピン中... 結果: {result}")
