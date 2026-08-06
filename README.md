# 碩田学園 生成AI研修（せきでん・ワークショップ型）

令和8年8月10日（月）。お三方のための生成AI研修サイトと配布資料。

- 公開URL: https://a-tozak.github.io/sekita-kenshu/ （GitHub Pagesは docs/ 配信）
- 形式: ワークショップ型。話は第1部だけ、第2部はワークA（型をためす）・B（注文をつける）・C（自分のGemを作る）、
  第3部はお一人ずつのページ（国語・研究主任／社会科）で「きょうの一歩」を決めて終わる
- Gemini前提: 全ページ右上に「Geminiを開く」常設。各プロンプトに「コピー」と
  「コピーしてGeminiを開く」（Gem指示文は「コピーしてGemの作成画面を開く」）の2ボタン
- 体裁: 高田小・菰田小の研修サイトと同じ編集ブランド（styles＝紺 #22406e＋老緑 #33513f）
- 本文・図版・配布資料はすべて自作。児童生徒の個人情報・学校内部資料・教科書紙面は含まない

## 構成

```
docs/               GitHub Pages の配信元
  index.html        本編（1 流れ／2 お約束／3 AIの基本／4 手を動かす=ワークA・B・C／
                    5 実例／6 個別の入口／7 配布資料／8 Q&A／9 参考リンク）
  kokugo.html       個別ページ1: 国語科・研究主任の先生へ（教材づくり・校務・研修だより・右腕Gem）
  shakai.html       個別ページ2: 社会科の先生へ（量産・台帳・サイト化・壁打ちGem）
  style.css         共有スタイル
  script.js         ナビ現在地・reveal・プロンプトのコピー（コピーしてGeminiを開く）
  haifu_shiryo.pdf  配布資料（A4×2枚・白黒前提）。print/handout.html から生成
  qr/               本ページQR・School Stock QR
  author.jpg        講師写真
print/handout.html  配布資料の組版元
```

## 更新のしかた

配布資料を直したら、`print/handout.html` を編集してPDFを焼き直す。

```bash
cd print
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
  --no-pdf-header-footer --run-all-compositor-stages-before-draw --virtual-time-budget=8000 \
  --print-to-pdf="../docs/haifu_shiryo.pdf" "file://$PWD/handout.html"
```

QRを作り直すときは `python3 -c "import qrcode; qrcode.make('URL').save('docs/qr/xxx.png')"`。
反映は commit → push（GitHub Pages に数分で反映）。

※読みは「せきでん」。リポジトリ名 sekita-kenshu は初版時の命名のまま
（変えると公開URLも変わるため、変える場合は本人判断で）。

© 2026 外﨑顯博
