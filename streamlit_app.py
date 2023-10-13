import streamlit as st
import random
import time

st.title("ルーレットゲーム")

spinning = False
result = None

# スピン中に表示するテキストエリア
spin_text = st.empty()

if not spinning:
    if st.button("スタート"):
        spinning = True
        while spinning:
            result = random.randint(1, 40)
            spin_text.text(f"ルーレットがスピン中... 結果: {result}")
            time.sleep(0.5)
            spinning = not st.button("ストップ")
        spin_text.text("ルーレットが停止しました。最終結果: {result}")
