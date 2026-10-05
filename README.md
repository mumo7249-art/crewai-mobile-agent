# CrewAI Mobile Agent

スマホからでも使えるシンプルなCrewAIマルチエージェントシステムです。

## できること
- トピックを入力するだけで、リサーチャーとライターのエージェントが自動で調査・レポート作成
- StreamlitのWeb UIなのでスマホブラウザから操作可能

## ローカルで動かす方法

1. このリポジトリをクローン
```bash
git clone https://github.com/mumo7249-art/crewai-mobile-agent.git
cd crewai-mobile-agent
```

2. 仮想環境を作成して依存関係をインストール
```bash
python -m venv venv
source venv/bin/activate   # Windowsの場合は venv\Scripts\activate
pip install -r requirements.txt
```

3. `.env` ファイルを作成
```bash
cp .env.example .env
```
`.env` を編集してAPIキーを入れてください：
```
OPENAI_API_KEY=sk-xxxxxxxx
# または ANTHROPIC_API_KEY=...
SERPER_API_KEY=xxxxxxxx   # Web検索を使う場合（推奨）
```

4. アプリを起動
```bash
streamlit run app.py
```

ブラウザで `http://localhost:8501` が開きます。

## スマホから使う方法（おすすめ）

### 方法1: Streamlit Community Cloud（一番簡単・無料）
1. [https://share.streamlit.io](https://share.streamlit.io) にGitHubアカウントでログイン
2. 「New app」をクリック
3. このリポジトリを選択
4. Main file path に `app.py` を指定
5. Advanced settings で Secrets にAPIキーを登録（OPENAI_API_KEY など）
6. Deploy！

デプロイ後、生成されたURLをスマホのホーム画面に追加すればアプリのように使えます。

### 方法2: Hugging Face Spaces
同様に無料でデプロイ可能です。

## 注意
- APIキーは絶対にGitHubにコミットしないでください（.envは.gitignoreに入っています）
- 本番利用時はコストに注意（特にGPT-4系）
