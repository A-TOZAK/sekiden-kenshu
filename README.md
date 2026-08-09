# 碩田学園 生成AI研修（せきでん・ワークショップ型）

令和8年8月10日（月）。**中学校の先生お三方**（国語科・研究主任／社会科）のための生成AI研修サイトと配布資料。
文面・プロンプト例はすべて中学校前提（「生徒」「中学校の…」）。School Stockの棚は小学校向けなので、
サイト上は「中学校版がほしい教材があればお知らせください」の形で案内している。

- 公開URL: https://a-tozak.github.io/sekita-kenshu/ （GitHub Pagesは docs/ 配信）
- 形式: 診断型ワークショップ（2026-08-09 全面改訂）。背骨は外﨑の論文「生成AI活用力の発達系統モデル」＝
  第1部で5段階の地図と現在地チェック（15項目・Web上で判定可）、第2部はワークA・B・C、
  第3部はお一人ずつのページ＋お三方共通「学校の仕事」（gakko.html）で「きょうの一歩」を決めて終わる
- 論文の系統表・15項目チェックは本人が公開OKと判断済み（2026-08-09）。号刀悠貴先生（札幌新陽高校）の
  進路指導×NotebookLM実践は、アイデアソンShowcase発表の要約として掲載（スライド転載なし・名の読みは載せない）
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
  shakai.html       個別ページ2: 社会科の先生へ（量産・台帳・サイト化＝地域教材事例集の実例つき・壁打ちGem）
  gakko.html        個別ページ3: 学校の仕事へ＝お三方共通（進路×NotebookLM・仕事の分解・自動化の階段・組織に手渡す）
  worksheet_genzaichi.pdf  ワークシート（できることチェック15項目＋仕事の分解。論文付録Aと同内容）
  kinyurei_3nin.pdf        記入例（実態のちがう3人）
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
