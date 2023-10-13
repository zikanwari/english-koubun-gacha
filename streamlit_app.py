import streamlit as st
import random
import time

def main():
    st.title("ルーレットゲーム")

    spinning = False
    result = None

    if not spinning:
        if st.button("スタート"):
            spinning = True
            while spinning:
                result = random.randint(1, 40)
                st.write(f"ルーレットがスピン中... 結果: {result}")
                time.sleep(0.5)
                spinning = not st.button("ストップ")
        st.write("ルーレットが停止しました。最終結果: {result}")

if __name__ == "__main__":
    main()
