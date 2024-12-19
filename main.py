#!/usr/bin/env python3
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage
import subprocess
import sys
from dotenv import load_dotenv
import os

def get_interesting_fact():
    """BedrockChatを使用して面白い事実を取得する"""
    # 環境変数を読み込む
    load_dotenv()
    
    chat = ChatBedrock(
        model_id="anthropic.claude-3-haiku-20240307-v1:0",
        region_name=os.getenv('AWS_REGION', 'us-east-1'),
        credentials_profile_name=os.getenv('AWS_PROFILE', None)
    )
    messages = [HumanMessage(content="面白い事実を一つ教えてください。できるだけ短く簡潔に答えてください。")]
    response = chat.invoke(messages)
    return response.content

def say_with_cow(message):
    """cowsayを使用してメッセージを表示する"""
    try:
        subprocess.run(["cowsay", message], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running cowsay: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    try:
        fact = get_interesting_fact()
        say_with_cow(fact)
    except Exception as e:
        print(f"エラーが発生しました: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
