# pascol voc to coco
Convert pascol voc annotation xml to COCO json format.

1. pip install lxml
2. python voc2coco.py xmllist.txt ../Annotations output.json

The xmllist.txt is the list of xml file names to convert.
000005.xml
000007.xml
000009.xml

The "../Annotations" is the place where all xmls located.

The "output.json" is the output json file.
---
### 2022/11/08 說明
* 將VOC格式的XML統一轉成coco-json
* 指令:`python voc2coco2.py output.txt ./xml output.json`
* `output.txt` 裡面是所有xml的list
* `./xml` 裡面是放所有圖片的標註xml
* `output.json` 是要輸出的檔案名稱
