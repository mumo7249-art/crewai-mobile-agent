import streamlit as st
from dotenv import load_dotenv
import os
from crew import run_research_crew

load_dotenv()

st.set_page_config(
    page_title="CrewAI Research Agent",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# スマホ向けのシンプルなCSS
st.markdown("""
<style>
    .stTextInput > div > div > input {
        font-size: 16px;
    }
    .stButton > button {
        width: 100%;
        height: 3em;
        font-size: 18px;
    }
    .report-box {
        background-color: #f8f9fa;
        padding: 1.2rem;
        border-radius: 10px;
        border: 1px solid #e9ecef;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("🤖 CrewAI Research Agent")
st.caption("スマホからも使えるマルチエージェント調査ツール")

topic = st.text_input(
    "調査したいトピックを入力してください",
    placeholder="例: 2026年のAIエージェントの最新トレンド",
    key="topic_input"
)

col1, col2 = st.columns(2)
with col1:
    model = st.selectbox(
        "使用モデル",
        ["gpt-4o-mini", "gpt-4o", "claude-3-5-sonnet-latest", "gemini/gemini-1.5-flash"],
        index=0
    )
with col2:
    use_search = st.checkbox("Web検索を使う", value=True)

if st.button("調査を開始する", type="primary"):
    if not topic.strip():
        st.warning("トピックを入力してください")
    else:
        with st.spinner("エージェントが調査中です... しばらくお待ちください"):
            try:
                result = run_research_crew(
                    topic=topic.strip(),
                    model=model,
                    use_search=use_search
                )
                st.success("調査完了！")
                st.markdown("### 📄 レポート")
                st.markdown(f'<div class="report-box">{result}</div>', unsafe_allow_html=True)
                
                # ダウンロードボタン
                st.download_button(
                    label="レポートをダウンロード (.md)",
                    data=result,
                    file_name=f"report_{topic[:30].replace(' ', '_')}.md",
                    mime="text/markdown"
                )
            except Exception as e:
                st.error(f"エラーが発生しました: {str(e)}")
                st.info("APIキーが正しく設定されているか確認してください（.env または Streamlit Secrets）")

st.markdown("---")
st.caption("Powered by CrewAI + Streamlit")
