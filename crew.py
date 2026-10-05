from crewai import Agent, Task, Crew, Process, LLM
from crewai_tools import SerperDevTool
import os

def run_research_crew(topic: str, model: str = "gpt-4o-mini", use_search: bool = True):
    # LLM設定
    llm = LLM(model=model)

    # ツール
    tools = []
    if use_search and os.getenv("SERPER_API_KEY"):
        tools.append(SerperDevTool())

    # エージェント定義
    researcher = Agent(
        role="シニアリサーチャー",
        goal=f"{topic} に関する最新で正確な情報を調査する",
        backstory="あなたは経験豊富なリサーチャーです。信頼できるソースだけを使い、重要なポイントを簡潔にまとめます。",
        tools=tools,
        llm=llm,
        verbose=False,
        allow_delegation=False
    )

    writer = Agent(
        role="プロフェッショナルライター",
        goal="調査結果を読みやすく構造化されたレポートにまとめる",
        backstory="あなたはプロのライターです。読みやすく、わかりやすい文章を書くのが得意です。日本語で自然なレポートを作成します。",
        llm=llm,
        verbose=False,
        allow_delegation=False
    )

    # タスク定義
    research_task = Task(
        description=f"""
        「{topic}」について徹底的に調査してください。
        - 最新の動向・トレンド
        - 主要な企業・ツール・事例
        - 今後の展望
        を中心にまとめてください。
        """,
        expected_output="主要なポイントを整理した調査結果（箇条書き中心）",
        agent=researcher
    )

    writing_task = Task(
        description=f"""
        調査結果をもとに、「{topic}」に関する読みやすいレポートを作成してください。
        以下の構成を推奨します：
        1. 概要
        2. 主要なトレンド・動向
        3. 注目のツール・企業・事例
        4. まとめと今後の展望

        Markdown形式で、見出しを使って見やすく書いてください。
        """,
        expected_output="完成したMarkdown形式のレポート",
        agent=writer,
        context=[research_task]
    )

    # クルー作成と実行
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        process=Process.sequential,
        verbose=False
    )

    result = crew.kickoff()
    return str(result)
