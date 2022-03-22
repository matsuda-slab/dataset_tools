# データセット作成関連 便利ツール集

## 概要
YOLO形式の学習データセットを用いた学習を行うことを想定し，
アノテーションファイルは，
```
クラス番号 x中央座標 y中央座標 横幅 縦幅
クラス番号 x中央座標 y中央座標 横幅 縦幅
...
```
の形式で書かれたテキストファイルを想定している．

## 手順
1. 作業ディレクトリを以下のようなディレクトリ構成とする．
   workspace は，作業ディレクトリのルートディレクトリを表す．

	 ```
   workspace  
       ├── images  
       └── labels
	 ```

   images : 画像ファイルを置いたディレクトリ
   labels : YOLO形式のアノテーションファイルを置いたディレクトリ

2. classify.sh を使って，images のデータセットを train, valid, test に分類する．

3. create_list.py を使って，画像パスが書かれたリストファイルを作成する．
   学習やテストの際は，このリストファイルをもとに，データセットにアクセスする．

## 各スクリプトについて
* cocodatasets_createpart/main.py  
  coco の instance ファイル (instances_trainval35k.json など) から
  画像ファイルへのパスを羅列したファイル (trainvalno5k.txt みたいなファイル)
  を生成する.

* coco_tools/class_extracter.py  
  COCOデータセットから特定クラスの画像のみを抽出し,
  画像パスを羅列したファイル (hogehoge.txt) を生成する．

* labeling_view/main.py  
  アノテーション情報を元に, 矩形を描画した画像を生成する.  
  正しくアノテーションできているか確認するために使用する.  

* create_list.py  
  train, valid, test のディレクトリ内容を元に, 画像のパスを列挙した
  リストファイルを生成する.
  [ Usage ]
    $ create_list.py {データセットのtrain, valid, testがあるパス}

* classify.sh  
  images のデータセットを, train, valid, test に分類する.  
  [ Usage ]  
    1. データセットのディレクトリ images, labels を用意する
    2. 必要なら, classify.sh の train, valid, test の比率を調整する.
       デフォルトは train : valid : test = 7 : 2 : 1
       必要なら, classify.sh の IMG_FORMAT を変える.
       デフォルトは png
    3. classify.sh {images, labels のあるパス}
       で, 指定したパスに train, valid, test を作成する.
       実行後は以下のようなディレクトリ構成になる．

	```
  workspace  
      ├── images  
      │      ├── train  
      │      ├── valid  
      │      └── test  
      │
      └── labels  
             ├── train  
             ├── valid  
             └── test  
	```
