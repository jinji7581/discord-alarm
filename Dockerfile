
FROM python:3.11-slim

# コンテナ内の作業ディレクトリ
WORKDIR /app

# キャッシュ効率のため requirements だけ先にコピー
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Botのコードをコピー
COPY . /app

# 起動コマンド
CMD ["python", "src/bot.py"]
