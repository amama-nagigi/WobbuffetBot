FROM python:3.6

# 必要なライブラリをインストール
RUN pip install discord
RUN pip install jaconv

# ソースをコンテナ内にコピー
COPY ./src/ ./src/

# 作業フォルダを設定しコマンド実行
WORKDIR ./src/
CMD ["python", "main.py"]
