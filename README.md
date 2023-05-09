# StudyProgram-GPT

## Goに関する環境構築
- `brew install go`

## Flaskのインストール

- `pip install Flask`

## 実行コマンド(以下を順に叩く)

- `export FLASK_APP=app`

- `export FLASK_ENV=development`

- `flask run`

デフォルトではローカルホスト以外からアクセスができないようになっているので，ローカルホスト以外からのアクセスする時は，--host=0.0.0.0を後ろにつけてください．
- `flask run　--host=0.0.0.0`
