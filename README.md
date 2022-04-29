# 5ch_keeper
To Keep thread active.

# 使い方

## Python のインストール

`Python3.x` なら何でも動く。好きなのをインストール。
https://pythonlinks.python.jp/ja/index.html
Windowsの場合、環境変数を通すみたいなチェックボックスがあればチェックする。

以下のコマンドをコマンドプロンプトで入力し、それっぽいバージョンが表示されれば成功

```shell
python --version
```
エラー文っぽいのが表示されてたら失敗してる。

## ライブラリインストール

`setup.bat` を実行。

## 設定
`setting.json` を開き、URLを保守したいスレのURLに変更。
そこ以外の部分は空気読んで変更しろ。

## 保守実行
`exec.bat` を叩くと30分置きに保守する。時間変えたければ `main.py` の一番下の数字を勘で弄れ。