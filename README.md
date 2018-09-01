# OpenTX Japanese Soundpack (Microsoft Ayumi)
## はじめに (Introduction)

まっく@Betaflight日本語化プロジェクトです。今回、日本語化プロジェクト第二弾として
OpenTX周りの日本語化をゴニョゴニョしたいと思っていますが、まずは手始めとして音源を
日本語化してみました。皆様に利用して頂き、色々と使い勝手を良くしていければと考えます。


## 説明 (Description)

このリポジトリは、OpenTX 日本語サウンドパックを提供しています。
今回、音源の日本語化にはMicrosoft合成音声エンジン(Ayumi)を用いてテキスト読み上げを行いました。
動作確認環境としてOpenTX 2.2.2をベースとし、FrSky Taranis X-Liteでテストを行っています。

このサウンドパックが提供するメッセージフレーズは、次の3つのカテゴリのいずれかに分類されます:

 * OpenTX システムメッセージ (OpenTX system messages)
 * マルチローター関連用語 (Multirotor related)
 * おもしろフレーズ (Funny lines)


## ダウンロードとインストール (Download & Install)

releaseページへ移動し、最新のZIPアーカイブファイルをダウンロードしてください。そして、ご自身の送信機で
使用している対象音源を削除してください。音源は、OpenTX SDカード内の `SOUNDS / en /`ディレクトリです。
ダウンロードしたZIPアーカイブの内容をコピーし、SDカードの `SOUNDS /`ディレクトリにコピーしてください。

現在OpenTXではJapaneseおよびJPの選択項目がないため、他言語で使われるディレクトリと置き換えて利用する
必要がありますのでご了承お願い致します。


## 技術的な詳細について (Technical Details)

`index.csv`ファイルは、音源に含まれるすべてのメッセージフレーズのデータベースとなります。
`tools /`ディレクトリにあるPythonスクリプトは、テキスト読み上げをを行いWAVデータを生成するために
使用しますが、今回この音源は、スクリプトを使用せず別ツールを用いてWAVファイルを生成しています。
またCSVファイルは、下記の項目に分かれています。

 * `_idx` 対象メッセージが最初に抽出されたファイル名
 * `_category` 対象メッセージに割り当てられた旧カテゴリ
 * `category` 対象メッセージに割り当てられた新カテゴリ
 * `directory` 対象メッセージを格納するファイルシステムのパス
 * `_filename`  対象メッセージの旧ファイル名
 * `filename` 対象メッセージの新ファイル名
 * `_text` メッセージフレーズ内容


## クレジット (Credits)

今回、こちらのサウンドパックの提供はPhaeilo氏が提供する【Siri Multirotor Soundpack for OpenTX】
をforkしております。dale3h氏およびPhaeilo氏の、非常にすばらしい英語サウンドパックに感謝致します。

* Inspiration: "Amber" sound pack by Arron Bates (theKM)
* Original "taranis-siri-sound-pack" by: Dale Higgs (dale3h)
* Improved by: Philip Huppert (Phaeilo)
* Japanese Transration by: まっく (t_mac116)


## Siri Multirotor Soundpack for OpenTX (fork元)

fork元はこちら
https://github.com/Phaeilo/opentx-siri-multirotor

