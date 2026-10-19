#!/usr/bin/env python3
"""世界の国を学ぶ授業のプロンプト集（docs/kuni.html）を、kuni_src/ の原稿から組み立てる。

原稿を直したら `python3 kuni_src/build_kuni.py` を1回。
生徒用プロンプト＝00_header ＋ 単元カード ＋ 10_engine ＋ 出力の型（20_typeA / 21_typeB / 壁打ちが作る型C）。
ページ内の組み立て機能（JS）も同じ順で組む。
"""
import html
from pathlib import Path

SRC = Path(__file__).resolve().parent
OUT = SRC.parent / "docs" / "kuni.html"


def rd(name):
    return (SRC / name).read_text(encoding="utf-8").rstrip("\n")


HEADER = rd("00_header.txt")
ENGINE = rd("10_engine.txt")
TYPE_A = rd("20_typeA.txt")
TYPE_B = rd("21_typeB.txt")
KABE = rd("30_kabeuchi.txt")
CARD_KR = rd("40_card_korea.txt")
CARD_BLANK = rd("41_card_blank.txt")
SAMPLE_YAML = rd("50_sample_korea.yaml")


def assemble(card, out_type):
    return "\n\n".join([HEADER, "■【単元カード】（授業ごとに差しかえる部分）\n" + card, ENGINE, out_type])


KOREA_FULL = assemble(CARD_KR, TYPE_B)
SAMPLE_FULL = "以下のYAMLの設計どおりに、画像を1枚生成してください。\n\n" + SAMPLE_YAML


def e(s):
    return html.escape(s, quote=False)


def prompt_box(title, body, pid="", open_url=None, open_label=None, long=False):
    pid_attr = f' id="{pid}"' if pid else ""
    cls = "prompt long" if long else "prompt"
    n = len(body)
    extra = ""
    if open_url:
        extra = f'<div class="pa"><button class="copyopen" type="button" data-url="{open_url}">{open_label}</button></div>'
    return f'''<div class="{cls}">
      <div class="ph"><span class="ttl">{title}<span class="cnt">（{n:,}字）</span></span><button class="copy" type="button">コピー</button></div>
      <pre{pid_attr}>{e(body)}</pre>
      {extra}
    </div>'''


BOARD_SVG = '''<svg viewBox="0 0 960 540" role="img" aria-labelledby="bd-t" class="board-fig">
  <title id="bd-t">知らない世界ボードの配置図。左にタイトルと司会の円、右に金のパネル3枚、下に資料の帯。</title>
  <rect width="960" height="540" fill="#bfe6f3"/>
  <circle cx="120" cy="110" r="120" fill="#cfe9a8" opacity=".75"/>
  <circle cx="880" cy="470" r="150" fill="#cfe9a8" opacity=".75"/>
  <!-- title -->
  <rect x="38" y="26" width="300" height="130" rx="6" fill="#fff" fill-opacity=".55" stroke="#22406e" stroke-dasharray="6 5"/>
  <text x="188" y="76" text-anchor="middle" font-size="24" font-weight="800" fill="#15181c">タイトル1行目（黒）</text>
  <text x="188" y="120" text-anchor="middle" font-size="30" font-weight="800" fill="#d6001c">タイトル2行目（赤）</text>
  <text x="188" y="146" text-anchor="middle" font-size="14" fill="#5b6068">各9字以内</text>
  <!-- host -->
  <circle cx="170" cy="330" r="118" fill="#fff" stroke="#e85aa4" stroke-width="16"/>
  <circle cx="170" cy="330" r="106" fill="none" stroke="#7a4bb5" stroke-width="5"/>
  <text x="170" y="322" text-anchor="middle" font-size="19" font-weight="800" fill="#15181c">司会の円</text>
  <text x="170" y="348" text-anchor="middle" font-size="14" fill="#5b6068">オリジナルのキャラ</text>
  <path d="M232 214 h136 a12 12 0 0 1 12 12 v52 a12 12 0 0 1 -12 12 h-90 l-22 22 l2 -22 h-26 a12 12 0 0 1 -12 -12 v-52 a12 12 0 0 1 12 -12z" fill="#fff" stroke="#15181c" stroke-width="2"/>
  <text x="300" y="246" text-anchor="middle" font-size="17" font-weight="800" fill="#15181c">吹き出し</text>
  <text x="300" y="270" text-anchor="middle" font-size="15" font-weight="800" fill="#d6001c">（BEFORE）</text>
  <!-- panels -->
  <g font-weight="800">
    <rect x="378" y="22" width="548" height="136" rx="6" fill="#fff8e6" stroke="#c9a227" stroke-width="9"/>
    <rect x="396" y="40" width="170" height="100" fill="#e9e3d2" stroke="#c9a227" stroke-width="3"/>
    <text x="481" y="96" text-anchor="middle" font-size="15" fill="#5b6068">場面イラスト</text>
    <text x="746" y="78" text-anchor="middle" font-size="19" fill="#15181c">1行目　つかみ（黒・14字以内）</text>
    <text x="746" y="118" text-anchor="middle" font-size="25" fill="#d6001c">2行目　主役の言葉（赤）</text>
    <rect x="378" y="176" width="548" height="136" rx="6" fill="#fff8e6" stroke="#c9a227" stroke-width="9"/>
    <rect x="396" y="194" width="170" height="100" fill="#e9e3d2" stroke="#c9a227" stroke-width="3"/>
    <text x="481" y="250" text-anchor="middle" font-size="15" fill="#5b6068">場面イラスト</text>
    <text x="746" y="250" text-anchor="middle" font-size="22" fill="#15181c">パネル2（AFTER）</text>
    <rect x="378" y="330" width="548" height="136" rx="6" fill="#fff8e6" stroke="#c9a227" stroke-width="9"/>
    <rect x="396" y="348" width="170" height="100" fill="#e9e3d2" stroke="#c9a227" stroke-width="3"/>
    <text x="481" y="404" text-anchor="middle" font-size="15" fill="#5b6068">場面イラスト</text>
    <text x="746" y="404" text-anchor="middle" font-size="22" fill="#15181c">パネル3（AFTER）</text>
  </g>
  <!-- band -->
  <rect x="0" y="494" width="960" height="46" fill="#fff"/>
  <text x="24" y="524" font-size="16" fill="#3d4148">資料の帯（使った資料を30字以内で）</text>
</svg>'''

PAGE = f'''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>世界の国の授業プロンプト集｜碩田学園 生成AI研修</title>
<script>document.documentElement.className += ' js';</script>
<link rel="stylesheet" href="style.css">
<style>
.prompt.long pre{{max-height:420px; overflow:auto}}
.prompt .cnt{{font-weight:400; margin-left:.4em}}
.flow.f4{{grid-template-columns:repeat(4,1fr)}}
@media(max-width:900px){{ .flow.f4{{grid-template-columns:1fr 1fr}} }}
@media(max-width:560px){{ .flow.f4{{grid-template-columns:1fr}} }}
.kv{{margin-top:22px; border:1px solid var(--line); background:var(--paper)}}
.kv .r{{display:grid; grid-template-columns:9.5em 1fr; border-top:1px solid var(--line)}}
.kv .r:first-child{{border-top:0}}
.kv .k{{padding:12px 16px; background:var(--wash); font-weight:800; font-size:15px}}
.kv .v{{padding:12px 16px; font-size:15.5px}}
@media(max-width:600px){{ .kv .r{{grid-template-columns:1fr}} }}
.builder{{margin-top:22px; border:1px solid var(--line); background:var(--paper); padding:20px 22px}}
.builder textarea{{width:100%; min-height:220px; font-family:var(--font-mono); font-size:13px; line-height:1.7; padding:12px; border:1px solid #c9ccd1; border-radius:4px; resize:vertical}}
.builder .row{{display:flex; flex-wrap:wrap; gap:10px 22px; align-items:center; margin-top:14px; font-size:15.5px}}
.builder label{{cursor:pointer}}
.builder .go{{font-family:var(--font-ja); font-weight:800; font-size:15px; color:#fff; background:var(--accent); border:0; border-radius:4px; padding:10px 22px; cursor:pointer}}
.builder .go:hover{{background:#182f52}}
.builder .msg{{margin-top:12px; font-size:14.5px; color:var(--moss); font-weight:700; min-height:1.5em}}
.builder .msg.ng{{color:#b3261e}}
#build-out{{display:none}}
#build-out.show{{display:block}}
.board-fig{{display:block; width:100%; height:auto; border:1px solid var(--line); margin-top:22px}}
details.parts{{margin-top:18px; border:1px solid var(--line); background:var(--paper)}}
details.parts summary{{cursor:pointer; padding:14px 18px; font-weight:800; font-size:16px}}
details.parts .in{{padding:0 18px 18px}}
.chk li{{margin:6px 0 6px 1.3em; font-size:16px}}
h2,h3{{word-break:auto-phrase}}
</style>
</head>
<body>

<header class="bar">
  <div class="wrap">
    <div class="brand"><a href="index.html">碩田学園　生成AI研修</a></div>
    <nav class="nav">
      <a href="kokugo.html">国語</a>
      <a href="shakai.html" class="active">社会</a>
      <a href="gakko.html">学校の仕事</a>
      <a class="go-gemini" href="https://chatgpt.com/" target="_blank" rel="noopener">ChatGPTを開く</a>
    </nav>
  </div>
</header>

<div class="wrap"><div class="crumb"><a href="index.html">はじめに</a> › <a href="shakai.html">社会科の先生へ</a> › 世界の国の授業プロンプト集</div></div>

<div class="page-hero">
  <div class="wrap">
    <div class="kicker-ja">社会科の先生へ　追加のページ</div>
    <h1>世界の国を学ぶ授業のプロンプト集</h1>
    <p class="tagsub">中国の「ツッコミ先生」をもとに、どの国の授業でも使える形に組み直しました。授業者がChatGPTと相談して単元カードを作り、このページで生徒用プロンプトに組み立てます。最後に生徒のAIが、BEFOREとAFTERを比べられる画像の指示を出します。</p>
  </div>
</div>

<!-- ===== 使い方 ===== -->
<section>
  <div class="wrap reveal">
    <h2>このページの使い方</h2>
    <p class="lead">プロンプトを2つに分けました。授業を設計するための「相談用」と、生徒に配る「生徒用」です。生徒用は、どの国でも変わらない共通部分に、授業ごとの単元カードを差しこんで作ります。</p>
    <div class="flow f4">
      <div class="step">
        <div class="t">STEP</div><div class="n">1</div>
        <h3>ChatGPTと相談する</h3>
        <p>下の①を貼り付けて、問いと活動を決めます。最後に単元カードが出てきます。</p>
      </div>
      <div class="step">
        <div class="t">STEP</div><div class="n">2</div>
        <h3>このページで組み立てる</h3>
        <p>②の欄に単元カードを貼って「組み立てる」を押すと、生徒用プロンプトの全文ができます。</p>
      </div>
      <div class="step">
        <div class="t">STEP</div><div class="n">3</div>
        <h3>先生が試運転する</h3>
        <p>新しいチャットに貼り、生徒の役で最後まで1回通します。分かっている生徒と分からない生徒の2通りがおすすめです。</p>
      </div>
      <div class="step">
        <div class="t">STEP</div><div class="n">4</div>
        <h3>生徒に配る</h3>
        <p>Classroomなどで配ります。生徒は全文を貼り付けて、最初の一文を送るだけです。</p>
      </div>
    </div>
    <div class="tip"><b>Gemが使えなくても動くように作っています。</b>生徒用プロンプトは、チャットの最初のメッセージとして貼り付ける前提です。貼り付けるとAIは「準備OK」とだけ返して、生徒の入力を待ちます。Gemが使えるようになったら、同じ全文をGemの指示欄に入れればそのまま使えます。</div>
  </div>
</section>

<!-- ===== 分析 ===== -->
<section class="band">
  <div class="wrap reveal">
    <h2><span class="secno">0</span>中国のプロンプトを読んで分かったこと</h2>
    <p class="lead">中国の「ツッコミ先生 Ver.4」は、よく練られています。他の国に広げるにあたり、よいところはそのまま残し、国ごとに変わる部分だけを切り出しました。</p>
    <div class="grid c3">
      <div class="cell"><div class="cn">1</div><h3>最初の言葉を原文のまま持ち続ける</h3><p>BEFOREを最初に取り出して、最後まで変えません。比べる相手が最初から決まっているので、成長が見えます。</p></div>
      <div class="cell"><div class="cn">2</div><h3>途中で役割を切りかえる</h3><p>前半は考える相手、後半は表現の相棒です。生徒にゼロから言葉を作らせないので、45分に収まります。</p></div>
      <div class="cell"><div class="cn">3</div><h3>質問攻めを止めるしくみがある</h3><p>同じ質問をくり返さない、ヒントは4段階、2回つまずいたら教える。AIの癖を先回りして止めています。</p></div>
      <div class="cell"><div class="cn">4</div><h3>資料を4段階で確かめる</h3><p>確かめられない資料を「正しい」と言わせません。人口の資料で経済成長の原因まで言えない、という線引きもあります。</p></div>
      <div class="cell"><div class="cn">5</div><h3>「決定」のあとに戻らない</h3><p>この決まりが何か所にも書かれています。別の案を出し続けるAIの癖を、しっかり止めています。</p></div>
      <div class="cell"><div class="cn">6</div><h3>最後は空欄のない画像の指示</h3><p>実際の会話から書いた画像生成プロンプトを、1つのコードブロックで出させます。生徒はコピーするだけです。</p></div>
    </div>
    <div class="menu">
      <div class="head"><span class="badge">＋</span><h3>他の国で使うために変えたこと</h3></div>
      <div class="body">
        <ol class="steps">
          <li>国ごとに変わる部分（学習の問い、扱う内容、つながりの例、事実の注意）を「単元カード」として切り出しました。残りは、どの国でもそのまま使える共通部分です。</li>
          <li>チャットに貼り付けたときの最初の動きを足しました。AIは「準備OK」とだけ返して待ちます。生徒が「ルールを忘れて」と言っても役割を変えません。</li>
          <li>作品の形を「出力の型」として差しかえられるようにしました。中国のポスターが型A、知らない世界ボードが型Bです。相談の中で新しい型Cも作れます。</li>
          <li>画像に入れる文字に字数の上限を付けました。画像生成AIは、長い日本語の文字がくずれやすいためです。</li>
          <li>実在の人物の顔、番組名やロゴ、国旗を絵に描かないことを決まりに入れました。番組の雰囲気だけを借りています。</li>
          <li>先生の合図を「資料タイム」「作品タイム」「まとめタイム」にそろえました。中国版の「コピー解禁」もそのまま使えます。</li>
        </ol>
      </div>
    </div>
  </div>
</section>

<!-- ===== ① 壁打ち ===== -->
<section id="kabeuchi">
  <div class="wrap reveal">
    <h2><span class="secno">1</span>授業者の相談用プロンプト（ChatGPT）</h2>
    <p class="lead">ChatGPTの新しいチャットに、全文を貼り付けて送信します。AIが1つずつ質問してくるので、答えていくと授業の形が決まります。いちばん大事なのはSTEP 4です。BEFOREとAFTERの組み合わせを3案出させ、「並べると何の成長が見えるか」で選びます。</p>
    {prompt_box("相談用｜世界の国を学ぶBEFORE→AFTER授業の設計", KABE, "p-kabe", "https://chatgpt.com/", "コピーしてChatGPTを開く", long=True)}
    <div class="tip"><b>最後に出てくるのは「単元カード」です。</b>コードブロックの中身をコピーして、すぐ下の②に貼ってください。途中で「出力して」と言えば、その時点の内容でカードを出します。</div>
  </div>
</section>

<!-- ===== ② 組み立て ===== -->
<section class="band" id="kumitate">
  <div class="wrap reveal">
    <h2><span class="secno">2</span>生徒用プロンプトを組み立てる</h2>
    <p class="lead">ChatGPTが出した単元カード（型Cを選んだときは、型Cの部分もいっしょに）を、下の欄に貼り付けてください。共通部分と出力の型をつなげて、生徒用プロンプトの全文を作ります。</p>
    <div class="builder">
      <textarea id="card-in" placeholder="【単元カード】から【単元カードここまで】までを貼り付けます"></textarea>
      <div class="row">
        <span>出力の型：</span>
        <label><input type="radio" name="otype" value="A"> 型A　キャッチフレーズ＋A4横ポスター</label>
        <label><input type="radio" name="otype" value="B" checked> 型B　知らない世界ボード</label>
        <label><input type="radio" name="otype" value="C"> 型C　相談で作った型</label>
      </div>
      <div class="row"><button class="go" type="button" id="build-go">組み立てる</button></div>
      <div class="msg" id="build-msg">カードの「成果物の型」を読んで、型は自動で選ばれます。</div>
    </div>
    <div id="build-out">
      {prompt_box("できあがり｜生徒用プロンプト（これを生徒に配ります）", "", "p-built", long=True)}
    </div>
    <details class="parts">
      <summary>手で書くときの、空の単元カード</summary>
      <div class="in">
        <p style="font-size:15.5px; margin-top:4px">ChatGPTを使わずに、自分で書くこともできます。〔〕の中を書きかえて、上の欄に貼ってください。</p>
        {prompt_box("空の単元カード", CARD_BLANK)}
      </div>
    </details>
  </div>
</section>

<!-- ===== ③ 韓国 ===== -->
<section id="kankoku">
  <div class="wrap reveal">
    <h2><span class="secno">3</span>見本：みんなの知らない韓国の世界</h2>
    <p class="lead">型Bで組み立てた、そのまま配れる見本です。生徒は最初に「私が思う韓国のイメージは『〇〇』です。」と送ります。そのイメージが司会キャラの吹き出し（BEFORE）になり、対話で分かった3つのテーマが金のパネル（AFTER）になります。</p>
    <div class="kv">
      <div class="r"><div class="k">学習の問い</div><div class="v">韓国はなぜ短い期間で、製品や文化を世界に広める国になったのだろう？</div></div>
      <div class="r"><div class="k">BEFORE</div><div class="v">最初のイメージ（例：K-POPとキムチの国）</div></div>
      <div class="r"><div class="k">AFTER</div><div class="v">番組ボードの3つのテーマ（工業化と輸出、首都への集中、文化の広がりなど）</div></div>
      <div class="r"><div class="k">比べると見えること</div><div class="v">「知っている韓国」から「なぜそうなったかを説明できる韓国」への変化</div></div>
    </div>
    {prompt_box("生徒用｜みんなの知らない韓国の世界（型B）", KOREA_FULL, "p-korea", long=True)}
    <div class="tip"><b>単元カードの中身は、教科書と照らし合わせてからお使いください。</b>扱う要因や年代は、一般的な中学校地理の教科書の範囲で書いています。お使いの教科書の言葉に合わせて、カードだけを直してください。</div>
  </div>
</section>

<!-- ===== ④ ボード ===== -->
<section class="band" id="board">
  <div class="wrap reveal">
    <h2><span class="secno">4</span>知らない世界ボードの設計図（YAML）</h2>
    <p class="lead">画像生成AIに「どこに、何を、どんな字で置くか」を伝えるために、YAMLという書き方で配置を決めています。YAMLは、項目の名前と中身を「名前: 中身」の形で並べる書き方です。言葉で頼むより、配置がぶれにくくなります。</p>
    {BOARD_SVG}
    <div class="grid c3">
      <div class="cell"><div class="cn">左上</div><h3>タイトル2行</h3><p>1行目は黒、2行目は赤で大きく。白の太いフチどりで、各9字以内です。</p></div>
      <div class="cell"><div class="cn">左下</div><h3>司会の円と吹き出し</h3><p>ピンクと紫のリングの円に、オリジナルのキャラを入れます。吹き出しに生徒のBEFOREを原文のまま入れます。</p></div>
      <div class="cell"><div class="cn">右</div><h3>金のパネル3枚</h3><p>左に場面のイラスト、右に見出し2行。1行目は「つかみ」、2行目は赤の「主役の言葉」です。</p></div>
    </div>
    <p style="margin-top:22px; max-width:46em">下は、韓国の見本の中身を入れた完成形です。先生が見本のボードを作って生徒に見せるときや、画像生成AIの癖を確かめるときに、そのまま貼り付けて使えます。横長16:9です。A4横で印刷したいときは、aspect_ratio の行を "1.414:1" に書きかえてください。</p>
    {prompt_box("先生用の見本｜韓国のボード（YAML・そのまま画像生成に使えます）", SAMPLE_FULL, "p-sample", long=True)}
    <div class="tip"><b>できた画像は、文字を1つずつ確かめてください。</b>画像生成AIは、日本語の文字を少し変えてしまうことがあります。生徒用プロンプトにも、最後に確かめるよう伝える一文を入れています。</div>
  </div>
</section>

<!-- ===== ⑤ 部品 ===== -->
<section id="buhin">
  <div class="wrap reveal">
    <h2><span class="secno">5</span>部品の全文</h2>
    <p class="lead">組み立てに使っている部品です。ふだんは見なくてかまいません。共通部分の決まりを確かめたいときや、型を自分で直したいときにお使いください。</p>
    <details class="parts">
      <summary>共通部分（最初の動きと、ツッコミ先生の本体）</summary>
      <div class="in">
        {prompt_box("共通部分　最初の動き", HEADER, "p-header")}
        {prompt_box("共通部分　ツッコミ先生の本体（1〜12）", ENGINE, "p-engine", long=True)}
      </div>
    </details>
    <details class="parts">
      <summary>出力の型A　キャッチフレーズ＋A4横のポスター（中国版の形）</summary>
      <div class="in">{prompt_box("出力の型A", TYPE_A, "p-typeA", long=True)}</div>
    </details>
    <details class="parts">
      <summary>出力の型B　知らない世界ボード（YAMLのひな形つき）</summary>
      <div class="in">{prompt_box("出力の型B", TYPE_B, "p-typeB", long=True)}</div>
    </details>
    <div class="extra">
      <div>
        <div class="ex-k">試運転で見るところ</div>
        <ul class="chk">
          <li>貼り付けた直後に「準備OK」とだけ返すか</li>
          <li>同じ質問をくり返していないか</li>
          <li>「決定」のあとに、別の案を出してこないか</li>
          <li>最後の画像の指示に、空欄や〔〕が残っていないか</li>
        </ul>
      </div>
    </div>
    <div class="next">
      <a href="shakai.html"><b>← 社会科の先生へ</b>もとのページ</a>
      <a href="gakko.html"><b>学校の仕事へ →</b>お三方共通のページ</a>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="foot-base">
      <div><span class="lw">碩田学園　生成AI研修</span>　追加のページ（令和8年10月）</div>
      <div>© 2026 外﨑顯博</div>
    </div>
    <div class="note-local">本ページのプロンプトと図は、資料作成者が中国版「ツッコミ先生 Ver.4」の考え方をもとに作り直したものです。中国版の原文は掲載していません。実在の番組名、人物、ロゴは使っていません。</div>
  </div>
</footer>

<script src="script.js"></script>
<script>
(function(){{
  const T=id=>document.getElementById(id).textContent.replace(/\\n+$/,'');
  const inp=document.getElementById('card-in');
  const msg=document.getElementById('build-msg');
  const out=document.getElementById('build-out');
  const pre=document.getElementById('p-built');
  const radios=[...document.querySelectorAll('input[name=otype]')];
  function pick(v){{ radios.forEach(r=>r.checked=(r.value===v)); }}
  function cut(s,a,b){{ const i=s.indexOf(a); if(i<0) return null; const j=s.indexOf(b,i); return j<0? s.slice(i) : s.slice(i,j+b.length); }}
  inp.addEventListener('input',()=>{{
    const s=inp.value;
    if(s.indexOf('【出力の型C】')>=0 || /成果物の型[：:]\\s*型?C/.test(s)) pick('C');
    else if(/成果物の型[：:]\\s*型?A/.test(s)) pick('A');
    else if(/成果物の型[：:]\\s*型?B/.test(s)) pick('B');
  }});
  document.getElementById('build-go').addEventListener('click',()=>{{
    const s=inp.value.replace(/^```[a-z]*\\n?/gm,'').trim();
    msg.classList.remove('ng');
    if(!s){{ msg.textContent='単元カードを貼り付けてください。'; msg.classList.add('ng'); return; }}
    let card=cut(s,'【単元カード】','【単元カードここまで】');
    if(!card){{ card=s.split('【出力の型C】')[0].trim(); }}
    const v=(radios.find(r=>r.checked)||{{}}).value;
    let typ;
    if(v==='A') typ=T('p-typeA');
    else if(v==='B') typ=T('p-typeB');
    else{{
      const c=cut(s,'【出力の型C】','【出力の型Cここまで】');
      if(!c){{ msg.textContent='型Cの部分（【出力の型C】から【出力の型Cここまで】）が見つかりません。ChatGPTに「型Cも同じコードブロックに出して」と頼んでください。'; msg.classList.add('ng'); return; }}
      typ=c.replace('【出力の型C】','').replace('【出力の型Cここまで】','').trim();
    }}
    const full=[T('p-header'),'■【単元カード】（授業ごとに差しかえる部分）\\n'+card,T('p-engine'),typ].join('\\n\\n');
    pre.textContent=full;
    out.querySelector('.cnt').textContent='（'+full.length.toLocaleString()+'字）';
    out.classList.add('show');
    const left=(card.match(/〔/g)||[]).length;
    msg.textContent = left>0 ? '組み立てました。単元カードに〔〕が'+left+'か所残っています。書きかえてから配ってください。' : '組み立てました。下の「コピー」で全文をコピーできます。';
    if(left>0) msg.classList.add('ng');
    out.scrollIntoView({{behavior:'smooth',block:'start'}});
  }});
}})();
</script>
</body>
</html>
'''

OUT.write_text(PAGE, encoding="utf-8")
print("wrote", OUT, len(PAGE), "chars")
print("korea full:", len(KOREA_FULL), "kabe:", len(KABE))
