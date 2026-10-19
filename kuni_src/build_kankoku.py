#!/usr/bin/env python3
"""「みんなの知らない韓国の世界」生徒用ページ（docs/kankoku.html）を組み立てる。

原稿は kuni_src/tokumaru/ の4本（授業者の作成。本文は変えない）。
原稿を直したら `python3 kuni_src/build_kankoku.py` を1回。
ページは1ファイルで完結する（CSSとJSを中に持つ）ので、HTMLだけを配っても動く。
"""
import html
from pathlib import Path

SRC = Path(__file__).resolve().parent / "tokumaru"
OUT = Path(__file__).resolve().parent.parent / "docs" / "kankoku.html"

CARDS = [
    dict(file="01_idol.md", no="1", color="#e2457d", soft="#fde8ef",
         title="みんなの知らない韓国アイドルの世界",
         who="世界で人気の、架空のK-POPアイドル",
         mission="韓国の文化が世界で人気になった秘密を解き明かそう",
         first="韓国語がわからない人まで、どうしてK-POPに夢中になると思う？"),
    dict(file="02_seoul.md", no="2", color="#0f8f8a", soft="#e0f4f2",
         title="みんなの知らない大都市ソウルの世界",
         who="ソウルの架空の市長",
         mission="ソウルに人が集まる理由と、発展の裏にある問題を解き明かそう",
         first="進学や仕事で、どんな理由ならソウルを選びたい？"),
    dict(file="03_nikkan.md", no="3", color="#e8673c", soft="#fdece5",
         title="みんなの知らない日本と韓国の世界",
         who="韓国で活動する、架空の日本人アイドル",
         mission="日本と韓国の意外なつながりを見つけよう",
         first="日本人の私が韓国で活動していることから、どんなつながりがあると思う？"),
    dict(file="04_keizai.md", no="4", color="#2f62b8", soft="#e6edf9",
         title="みんなの知らない韓国経済の世界",
         who="世界的な電子機器メーカーの、架空の社長",
         mission="韓国が世界的な工業国になれた秘密を解き明かそう",
         first="なぜ韓国の企業は、世界で使われる技術を生み出せるようになったと思う？"),
]


def e(s):
    return html.escape(s, quote=False)


cards_html = []
for c in CARDS:
    body = (SRC / c["file"]).read_text(encoding="utf-8").rstrip("\n")
    pid = "pr" + c["no"]
    cards_html.append(f'''
  <article class="card" style="--c:{c['color']};--s:{c['soft']}">
    <div class="band"><span class="ch">チャプター{c['no']}</span><span class="len">{len(body):,}字</span></div>
    <div class="cb">
      <h2>{e(c['title'])}</h2>
      <dl>
        <div><dt>話す相手</dt><dd>{e(c['who'])}</dd></div>
        <div><dt>ミッション</dt><dd>{e(c['mission'])}</dd></div>
        <div><dt>最初の質問</dt><dd>{e(c['first'])}</dd></div>
      </dl>
      <div class="btns">
        <button class="b-gem" type="button" data-for="{pid}">コピーしてGeminiを開く</button>
        <button class="b-copy" type="button" data-for="{pid}">全文をコピー</button>
      </div>
      <details>
        <summary>プロンプトの中身を見る</summary>
        <pre id="{pid}">{e(body)}</pre>
      </details>
    </div>
  </article>''')

PAGE = f'''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>みんなの知らない韓国の世界｜Geminiで取材しよう</title>
<style>
:root{{--ink:#15181c; --sub:#5b6068; --line:#e3e4e1; --wash:#f6f6f4; --paper:#fff; --accent:#22406e}}
*{{box-sizing:border-box; margin:0; padding:0}}
body{{font-family:"Hiragino Sans","Hiragino Kaku Gothic ProN","Noto Sans JP","Yu Gothic Medium",sans-serif; color:var(--ink); background:var(--wash); line-height:1.75; font-size:17px; -webkit-font-smoothing:antialiased; font-feature-settings:"palt"}}
.wrap{{max-width:1080px; margin:0 auto; padding:0 16px}}
header{{background:#bfe6f3; border-bottom:3px solid var(--ink); padding:34px 0 30px; position:relative; overflow:hidden}}
header::before,header::after{{content:""; position:absolute; border-radius:50%; background:#cfe9a8; opacity:.8}}
header::before{{width:260px; height:260px; left:-80px; top:-90px}}
header::after{{width:320px; height:320px; right:-110px; bottom:-170px}}
header .wrap{{position:relative; z-index:1}}
.kicker{{font-size:13px; font-weight:800; letter-spacing:.12em; color:var(--sub)}}
h1{{font-size:clamp(26px,5vw,42px); line-height:1.3; font-weight:900; margin-top:6px; word-break:auto-phrase}}
h1 .r{{color:#d6001c}}
.intro{{margin-top:12px; max-width:44em; font-size:16.5px}}
.how{{display:grid; grid-template-columns:repeat(3,1fr); gap:12px; margin:26px 0 8px}}
.how div{{background:var(--paper); border:1px solid var(--line); border-radius:8px; padding:14px 16px; font-size:15.5px}}
.how b{{display:inline-grid; place-items:center; width:26px; height:26px; border-radius:50%; background:var(--accent); color:#fff; font-size:14px; margin-right:8px}}
@media(max-width:760px){{ .how{{grid-template-columns:1fr}} }}
main{{padding:22px 0 50px}}
.grid{{display:grid; grid-template-columns:repeat(2,1fr); gap:18px}}
@media(max-width:820px){{ .grid{{grid-template-columns:1fr}} }}
.card{{background:var(--paper); border:1px solid var(--line); border-radius:10px; overflow:hidden; display:flex; flex-direction:column}}
.card .band{{background:var(--c); color:#fff; display:flex; justify-content:space-between; align-items:center; padding:9px 18px; font-weight:800}}
.card .ch{{font-size:15px; letter-spacing:.06em}}
.card .len{{font-size:12.5px; font-weight:600; opacity:.9}}
.card .cb{{padding:18px 18px 16px; display:flex; flex-direction:column; flex:1}}
.card h2{{font-size:clamp(20px,2.6vw,24px); line-height:1.4; font-weight:900; word-break:auto-phrase}}
dl{{margin-top:12px; display:grid; gap:6px}}
dl div{{display:grid; grid-template-columns:6.2em 1fr; gap:8px; font-size:15px}}
dt{{font-weight:800; color:var(--c)}}
.btns{{display:grid; grid-template-columns:1.4fr 1fr; gap:10px; margin-top:auto; padding-top:16px}}
@media(max-width:480px){{ .btns{{grid-template-columns:1fr}} }}
button{{font-family:inherit; font-weight:800; font-size:16px; border-radius:8px; padding:13px 10px; cursor:pointer; line-height:1.3}}
.b-gem{{background:var(--c); color:#fff; border:2px solid var(--c)}}
.b-copy{{background:var(--paper); color:var(--c); border:2px solid var(--c)}}
.b-gem:hover{{filter:brightness(.92)}}
.b-copy:hover{{background:var(--s)}}
button.done{{background:#33513f; border-color:#33513f; color:#fff}}
details{{margin-top:12px; border-top:1px solid var(--line); padding-top:8px}}
summary{{cursor:pointer; font-size:14px; font-weight:700; color:var(--sub)}}
pre{{margin-top:8px; max-height:320px; overflow:auto; background:var(--wash); border:1px solid var(--line); border-radius:6px; padding:12px; font-family:"SF Mono",Menlo,Consolas,monospace; font-size:12.5px; line-height:1.7; white-space:pre-wrap; word-break:break-word}}
.note{{margin-top:24px; background:var(--paper); border-left:4px solid #33513f; padding:14px 18px; font-size:15px}}
.note b{{color:#33513f}}
footer{{border-top:1px solid var(--line); padding:20px 0 34px; font-size:13px; color:var(--sub)}}
.toast{{position:fixed; left:50%; bottom:22px; transform:translateX(-50%) translateY(20px); background:#15181c; color:#fff; padding:12px 20px; border-radius:999px; font-size:15px; font-weight:700; opacity:0; transition:.25s; pointer-events:none; max-width:calc(100% - 32px); text-align:center}}
.toast.show{{opacity:1; transform:translateX(-50%) translateY(0)}}
</style>
</head>
<body>

<header>
  <div class="wrap">
    <div class="kicker">社会科 地理　韓国の学習</div>
    <h1>みんなの知らない<span class="r">韓国の世界</span></h1>
    <p class="intro">きみは新人記者です。4つのうち1つを選んで、Geminiの中の人物に取材しよう。発見したスクープを集めて、最後にテレビ番組みたいな1枚の画像にまとめます。</p>
    <div class="how">
      <div><b>1</b>取材したいチャプターの「コピーしてGeminiを開く」を押す</div>
      <div><b>2</b>開いたGeminiの入力欄に貼り付ける（Ctrl＋V、またはタップして貼り付け）</div>
      <div><b>3</b>そのまま送信する。人物があいさつしてきたら、取材スタート</div>
    </div>
  </div>
</header>

<main>
  <div class="wrap">
    <div class="grid">{"".join(cards_html)}
    </div>
    <div class="note"><b>うまく貼れないときは</b>「全文をコピー」を押してから、自分でGeminiを開いて貼り付けてください。途中で会話がずれたら、新しいチャットでもう一度貼り付けると、最初からやり直せます。画像ができたら、見出しの文字が正しいか、1文字ずつ確かめよう。</div>
  </div>
</main>

<footer>
  <div class="wrap">プロンプトは授業者が作りました。登場する人物はすべて架空です。実在の人物、番組、企業とは関係ありません。</div>
</footer>

<div class="toast" id="toast" role="status" aria-live="polite"></div>

<script>
(function(){{
  var GEMINI='https://gemini.google.com/app';
  var toast=document.getElementById('toast'), tid;
  function say(m){{ toast.textContent=m; toast.classList.add('show'); clearTimeout(tid); tid=setTimeout(function(){{toast.classList.remove('show')}},3200); }}
  // 押した瞬間にコピーする（タブを開く前に、同じ操作の中で済ませる）
  function copy(text){{
    var ok=false;
    try{{
      var ta=document.createElement('textarea');
      ta.value=text; ta.setAttribute('readonly',''); ta.style.position='fixed'; ta.style.top='-9999px'; ta.style.opacity='0';
      document.body.appendChild(ta); ta.focus(); ta.select(); ta.setSelectionRange(0,text.length);
      ok=document.execCommand('copy'); document.body.removeChild(ta);
    }}catch(e){{}}
    if(navigator.clipboard && window.isSecureContext){{ navigator.clipboard.writeText(text).catch(function(){{}}); ok=true; }}
    return ok;
  }}
  function flash(btn,label){{
    var old=btn.textContent; btn.textContent=label; btn.classList.add('done');
    setTimeout(function(){{ btn.textContent=old; btn.classList.remove('done'); }},2200);
  }}
  document.querySelectorAll('button[data-for]').forEach(function(btn){{
    btn.addEventListener('click',function(){{
      var text=document.getElementById(btn.dataset.for).textContent;
      var ok=copy(text);
      if(btn.classList.contains('b-gem')){{
        window.open(GEMINI,'_blank','noopener');
        flash(btn,'コピーしました');
        say(ok?'コピーしました。Geminiの入力欄に貼り付けて、送信しよう':'コピーできませんでした。「プロンプトの中身を見る」から選んでコピーしてください');
      }}else{{
        flash(btn,'コピーしました');
        say(ok?'全文をコピーしました':'コピーできませんでした。「プロンプトの中身を見る」から選んでコピーしてください');
      }}
    }});
  }});
}})();
</script>
</body>
</html>
'''

OUT.write_text(PAGE, encoding="utf-8")
print("wrote", OUT)
