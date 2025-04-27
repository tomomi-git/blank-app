import streamlit as st
from PIL import Image

# タイトル
st.title("テスト（画像表示アプリ）")

# 画像のアップロード
uploaded_file = st.file_uploader("画像を選択してください", type=["png", "jpg", "jpeg"])