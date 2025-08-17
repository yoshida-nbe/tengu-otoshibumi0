import streamlit as st
import google.generativeai as genai
import os

# -------------------------------------------------------------
# 1. 基本設定とAPIキーのセットアップ
# -------------------------------------------------------------
st.set_page_config(page_title="AIブログアシスタント", page_icon=":天狗:")

st.title("👺 推し！どくしょ指南")
st.write("キーワードやテーマを入力するだけで、いけてる👺が八艘跳びをくりだしつつ今読むべき世界文学を提案します。")

try:
  api_key = st.secrets["GOOGLE_API_KEY"]
  genai.configure(api_key=api_key)
  model = genai.GenerativeModel('gemini-1.5-flash-latest')
except KeyError:
  st.error("APIキーが設定されていません。")
  st.stop()

# -------------------------------------------------------------
# 2. ユーザーからの入力
# -------------------------------------------------------------
topic = st.text_input("キーワードやテーマを入力してください。", placeholder="例：読むだけで元気になるブンガク")

# -------------------------------------------------------------
# 3. ボタンが押されたときの処理
# -------------------------------------------------------------
if st.button("👺にうかがっちゃう"):
  if topic:  # キーワードが入力されている場合
    with st.spinner("👺が推し候補をさがしています...🔍"):
      prompt = f"""
      以下のキーワードに基づいて、今読むべき、推しの世界文学を提案してください。
      推しポイントや、ここに萌える、というポイントをわかりやすく提示し、その理由も教えてください。文体は、テンション高めの天狗が現代人につたえているように表現してください。
      キーワード: {topic}
      """
      try:
        # AIモデルの呼び出しと応答の表示
        response = model.generate_content(prompt)
        # 結果を表示
        st.subheader("👺が推す世界文学✨")
        st.write(response.text)
      except Exception as e:
        st.error(f"👺が🤡になりました: {e}")
  else:
    st.warning("👺キーワードがテーマがはいっとらんぞ。")
