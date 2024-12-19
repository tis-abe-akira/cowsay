# 🐮 AI Fact Cow

AIが教えてくれる面白い事実を、愛らしい牛さんが語ってくれるCLIツールです！

## 特徴 ✨

- 🤖 最新のAIモデル（Claude 3 Sonnet）が厳選した面白い事実を提供
- 🐄 懐かしのcowsayで楽しく表示
- 🎯 シンプルで使いやすいコマンドライン操作

## デモ 🎬

```bash
$ ./main.py
 ____________________________________
< 手首には9本の骨がある。 >
 ------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

## インストール方法 🚀

1. リポジトリをクローン
```bash
git clone [リポジトリURL]
cd cowsay
```

2. 必要なパッケージをインストール
```bash
uv venv
source .venv/bin/activate
uv pip install langchain-community langchain boto3 langchain-aws python-dotenv
```

## 環境設定 ⚙️

1. `.env.example` をコピーして `.env` を作成
```bash
cp .env.example .env
```

2. `.env` ファイルを編集して、AWS認証情報を設定
```env
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_REGION=us-east-1  # お使いのリージョン
```

## 使い方 💫

実行権限を付与して実行するだけ！
```bash
chmod +x main.py
./main.py
```

毎回異なる面白い事実を、かわいい牛さんが教えてくれます。

## 必要要件 📋

- Python 3.11以上
- cowsay
- AWS Bedrockへのアクセス権限

## 技術スタック 🛠

- Python
- langchain
- AWS Bedrock (Claude 3 Sonnet)
- cowsay

## ライセンス 📄

MITライセンス

## 作者 👤

abe.akira

---

面白い事実を共有して、みんなで楽しく学びましょう！ 🎉
