# OpenTX Japanese Soundpack (Microsoft Ayumi)
## 説明 (Description)

このリポジトリは、OpenTXの日本語サウンドパックを提供しています。
今回、日本語化にはMicrosoft合成音声エンジンを用いたAyumiによりテキスト読み上げを行いました。
適用環境としてOpenTX 2.2.2をベースとし、FrSky Taranis X-Liteでテストを行っています。

This repository contains an OpenTX soundpack which was generated using the
Ayumi voice of Microsoft's text-to-speech engine.  It is compatible with
OpenTX 2.2.2 and was tested on the FrSky Taranis X-Lite.

このサウンドパックが提供するフレーズは、次の3つのカテゴリのいずれかに分類されます:

The phrases provided by this soundpack fall into one of three categories:

 * OpenTX システムメッセージ (OpenTX system messages)
 * マルチローター関連用語 (Multirotor related)
 * おもしろフレーズ (Funny lines)


## ダウンロードとインストール (Download & Install)

releaseページへ移動し、最新のZIPアーカイブファイルをダウンロードしてください。そして、ご自身の送信機で
使用している音源を削除してください。音源は、OpenTX SDカード内の `SOUNDS / en /`ディレクトリとなります。
ダウンロードしたZIPアーカイブの内容をコピーし、SDカードの `SOUNDS /`ディレクトリにコピーしてください。

Go to the releases page and download the latest ZIP archive. Delete the
`SOUNDS/en/` directory on your OpenTX SD card. Extract the archive and copy
its contents to the `SOUNDS/` directory of the SD card.


## 技術的な詳細について (Technical Details)

`index.csv`ファイルには、すべてのメッセージのデータベースを含みます。
`tools /`ディレクトリにあるPythonスクリプトは、テキスト読み上げを使用してこのデータを
処理するために使用されます。CSVファイルは、下記で説明する列が使用されます。

 * `_idx` 対象メッセージが最初に抽出されたファイル名
 * `_category` 対象メッセージに割り当てられた旧カテゴリ
 * `category` 対象メッセージに割り当てられた新カテゴリ
 * `directory` 対象メッセージを格納するファイルシステムのパス
 * `_filename`  対象メッセージの旧ファイル名
 * `filename` 対象メッセージの新ファイル名
 * `_text` メッセージ内容


The file `index.csv` contains the database of all messages. Python scripts in
the `tools/` directory are used to process this data using text-to-speech. The
CSV file uses the following columns:

 * `_idx` filename from which this message was originally extracted
 * `_category` original category assigned to this message
 * `category` new category assigned to this message
 * `directory` file system path to store this message in
 * `_filename` original filename of this message
 * `filename` new filename of this message
 * `_text` spoken words of the message


## クレジット (Credits)

* Inspiration: "Amber" sound pack by Arron Bates (theKM)
* Original "taranis-siri-sound-pack" by: Dale Higgs (dale3h)
* Improved by: Philip Huppert (Phaeilo)
* Japanese Transration by: まっく (t_mac116)


