// 碩田学園 生成AI研修 共通スクリプト（ナビ現在地・reveal・プロンプトのコピー）

// active nav on scroll
var navLinks=[...document.querySelectorAll('.nav a')].filter(a=>a.getAttribute('href').startsWith('#'));
var navMap=navLinks.map(a=>({a,el:document.querySelector(a.getAttribute('href'))})).filter(x=>x.el);
if(navMap.length){
  const onScroll=()=>{
    const y=window.scrollY+90;
    let cur=null;
    for(const m of navMap){ if(m.el.offsetTop<=y) cur=m; }
    navLinks.forEach(l=>l.classList.remove('active'));
    if(cur) cur.a.classList.add('active');
  };
  document.addEventListener('scroll',onScroll,{passive:true}); onScroll();
}

// reveal
var _sk_io=new IntersectionObserver(es=>es.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('in'); _sk_io.unobserve(e.target);} }),{threshold:.08});
document.querySelectorAll('.reveal').forEach(el=>_sk_io.observe(el));

// プロンプトのコピー（「コピー」と「コピーしてGeminiを開く」）
async function copyText(pre){
  try{
    await navigator.clipboard.writeText(pre.innerText);
    return true;
  }catch(e){
    const r=document.createRange(); r.selectNode(pre);
    getSelection().removeAllRanges(); getSelection().addRange(r);
    try{ document.execCommand('copy'); getSelection().removeAllRanges(); return true; }
    catch(e2){ return false; }
  }
}
// 左メニュー（サイト全体の階層ドロワー）
(function(){
  const bar=document.querySelector('header.bar .wrap');
  if(!bar) return;
  const btn=document.createElement('button');
  btn.className='menu-btn'; btn.type='button'; btn.setAttribute('aria-label','メニューを開く');
  btn.innerHTML='☰<span> メニュー</span>';
  bar.insertBefore(btn,bar.firstChild);
  const R=location.pathname.includes('/jiten/')?'../':'';
  const wrap=document.createElement('div'); wrap.className='drawer-wrap';
  wrap.innerHTML=`<div class="drawer-bg"></div>
  <nav class="drawer" aria-label="サイト全体のメニュー">
    <div class="dh">碩田学園 生成AI研修</div>
    <div class="dg">研修本編（きょうの問い）</div>
    <a href="slide/">スライド版（投影用・24枚）</a>
    <a href="index.html#nagare">本日の流れ</a>
    <a href="index.html#kihon">問い1｜AIを使うとは</a>
    <a href="index.html#chizu">　地図：活用力の5段階</a>
    <a href="index.html#genzaichi">　いまの現在地チェック</a>
    <a href="index.html#tsukuru">問い2｜プロンプトはどう書くか</a>
    <a href="index.html#tsukaimichi">問い3｜どれを何に使うか</a>
    <div class="dg">じっくり試す（個別）</div>
    <a href="kokugo.html">国語科・研究主任の先生へ</a>
    <a href="shakai.html">社会科の先生へ</a>
    <a href="gakko.html">学校の仕事へ（お三方共通）</a>
    <div class="dg">じてん（辞書）</div>
    <a href="jiten/">じてんの目次</a>
    <a href="jiten/gemini.html">Gemini</a>
    <a href="jiten/notebooklm.html">Gemini Notebook</a>
    <a href="jiten/docs.html">ドキュメント</a>
    <a href="jiten/sheets.html">スプレッドシート</a>
    <a href="jiten/slides.html">スライド</a>
    <a href="jiten/forms.html">フォーム</a>
    <a href="jiten/classroom.html">Classroom</a>
    <a href="jiten/drive.html">ドライブ</a>
    <a href="jiten/index.html#kyoyu">共有権限のしくみ</a>
    <a href="jiten/prompts.html">プロンプト集</a>
    <div class="dg">資料とアンケート</div>
    <a href="haifu_shiryo.pdf" target="_blank" rel="noopener">配布資料（PDF）</a>
    <a href="worksheet_genzaichi.pdf" target="_blank" rel="noopener">ワークシート（現在地と分解）</a>
    <a href="kinyurei_3nin.pdf" target="_blank" rel="noopener">記入例（実態のちがう3人）</a>
    <a href="index.html#anketo">研修アンケート</a>
  </nav>`;
  wrap.querySelectorAll('a').forEach(a=>{const h=a.getAttribute('href');if(h&&!h.startsWith('http'))a.setAttribute('href',R+h);});
  document.body.appendChild(wrap);
  btn.addEventListener('click',()=>wrap.classList.add('open'));
  wrap.querySelector('.drawer-bg').addEventListener('click',()=>wrap.classList.remove('open'));
  wrap.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>wrap.classList.remove('open')));
})();

// 現在地チェック（15項目・「使う」の列で最初に外れた段階が現在地の見立て）
const ckBox=document.getElementById('cklist');
if(ckBox){
  const STAGES={
    1:{name:'言語化期',label:'目的をことばにする',step:'きょうの型1を1回ためして、出てきた事実（日付・数字・名前）をひとつ、自分で確かめてみてください。それが最初の一歩です。'},
    2:{name:'模倣期',label:'型を借りる',step:'型を1本だけ決めて、1週間おなじ型を使い続けてみてください。効いた注文のメモが、次の段階の材料になります。'},
    3:{name:'適合期',label:'自分の仕事に合わせる',step:'仕事をひとつ選んで手順に分解し、「任せる・自分でやる・行わない」の札を付けてみてください。配布のワークシート（うら面）がそのまま使えます。'},
    4:{name:'構築期',label:'仕組みにする',step:'毎回書いている前提（学年・文体・読み手）をGemに常設してください。その先の自動化は「学校の仕事」のページにあります。'},
    5:{name:'移転期',label:'組織に手渡す',step:'同じ質問が3回来たものを、A4半分の紙にしてみてください。渡す紙の下書きの型は「学校の仕事」のページにあります。'}
  };
  const btn=document.getElementById('ck-judge');
  const out=document.getElementById('ck-result');
  btn&&btn.addEventListener('click',()=>{
    let cur=null;
    for(const s of [1,2,3,4,5]){
      const el=ckBox.querySelector(`input[data-stage="${s}"][data-fn="u"]`);
      if(el && !el.checked){ cur=s; break; }
    }
    let h,p;
    if(cur===null){
      h='現在地の見立て：第5段階 移転期のただ中です';
      p='「使う」の列がすべて○の方は、次の課題は自分の腕ではなく「手渡し方」です。同じ質問が3回来たものを紙にする、から始めてください。';
    }else{
      const st=STAGES[cur];
      h=`現在地の見立て：第${cur}段階 ${st.name}（${st.label}）`;
      p=`次の一歩：${st.step}`;
    }
    out.innerHTML=`<h4>${h}</h4><p>${p}</p><p style="color:var(--sub); font-size:13px; margin-top:8px">段階が人によって違うのは当然のことで、低い段階は恥ではありません。経験年数と段階は比例しません。この見立ては診断の入口であって、成績ではありません。</p>`;
    out.classList.add('show');
    out.scrollIntoView({behavior:'smooth',block:'nearest'});
  });
}

document.querySelectorAll('.prompt').forEach(box=>{
  const pre=box.querySelector('pre');
  const btnCopy=box.querySelector('.copy');
  const btnOpen=box.querySelector('.copyopen');
  if(btnCopy){
    btnCopy.addEventListener('click',async()=>{
      await copyText(pre);
      btnCopy.textContent='コピーしました'; btnCopy.classList.add('done');
      setTimeout(()=>{ btnCopy.textContent='コピー'; btnCopy.classList.remove('done'); },1800);
    });
  }
  if(btnOpen){
    const url=btnOpen.dataset.url||'https://gemini.google.com/app';
    const label=btnOpen.textContent;
    btnOpen.addEventListener('click',async()=>{
      await copyText(pre);
      btnOpen.textContent='コピーしました。貼り付けてください'; btnOpen.classList.add('done');
      window.open(url,'_blank','noopener');
      setTimeout(()=>{ btnOpen.textContent=label; btnOpen.classList.remove('done'); },2600);
    });
  }
});


// 文字サイズ切り替え（標準/1.5倍/2倍・全ページ・localStorageで記憶）
(function(){
  const css=`.fs-btns{display:flex;gap:4px;align-items:center;margin-left:12px}
.fs-btns .fsb{font-family:inherit;font-weight:800;font-size:12px;color:#767b83;background:none;border:1px solid #e6e6e3;border-radius:4px;padding:5px 9px;cursor:pointer;white-space:nowrap}
.fs-btns .fsb.on{color:#fff;background:#22406e;border-color:#22406e}
.menu-btn{font-weight:800;font-size:13px;color:#15181c;background:none;border:1px solid #e6e6e3;border-radius:4px;padding:6px 12px;cursor:pointer;margin-right:14px;white-space:nowrap;font-family:inherit}
.drawer-wrap{position:fixed;inset:0;z-index:100;pointer-events:none}
.drawer-wrap .drawer-bg{position:absolute;inset:0;background:rgba(14,15,17,.4);opacity:0;transition:opacity .25s}
.drawer-wrap .drawer{position:absolute;top:0;left:0;bottom:0;width:min(320px,86vw);background:#fff;border-right:1px solid #e6e6e3;transform:translateX(-100%);transition:transform .25s;overflow-y:auto;padding:22px 0 40px}
.drawer-wrap.open{pointer-events:auto}.drawer-wrap.open .drawer-bg{opacity:1}.drawer-wrap.open .drawer{transform:none}
.drawer .dh{font-weight:800;color:#0e0f11;padding:0 22px 12px;border-bottom:1px solid #e6e6e3;margin-bottom:8px}
.drawer .dg{font-size:11.5px;font-weight:800;letter-spacing:.06em;color:#33513f;padding:16px 22px 4px}
.drawer a{display:block;padding:7px 22px;font-size:14px;color:#15181c;text-decoration:none}
.drawer a:hover{background:#f6f6f4}`;
  const st=document.createElement('style'); st.textContent=css; document.head.appendChild(st);
  const bar=document.querySelector('header.bar .wrap'); if(!bar) return;
  const box=document.createElement('div'); box.className='fs-btns';
  box.innerHTML='<button class="fsb" data-z="1">文字 標準</button><button class="fsb" data-z="1.5">1.5倍</button><button class="fsb" data-z="2">2倍</button>';
  const brand=bar.querySelector('.brand');
  if(brand&&brand.nextSibling) bar.insertBefore(box,brand.nextSibling); else bar.appendChild(box);
  function apply(z){
    document.querySelectorAll('section, .hero, .page-hero, footer, .crumb, .fig, .concept2, .perm2').forEach(el=>el.style.zoom=(z==1?'':z));
    box.querySelectorAll('.fsb').forEach(b=>b.classList.toggle('on',b.dataset.z==z));
    try{localStorage.setItem('sekiden_fs',z)}catch(e){}
  }
  box.querySelectorAll('.fsb').forEach(b=>b.addEventListener('click',()=>apply(b.dataset.z)));
  let z=1; try{z=localStorage.getItem('sekiden_fs')||1}catch(e){}
  apply(z);
})();


// QR表示ボタン＋右下の相談窓口
(function(){
  const R=location.pathname.includes('/jiten/')?'../':'';
  const css=`.qr-btn{font-family:inherit;font-weight:800;font-size:12px;color:#22406e;background:none;border:1px solid #22406e;border-radius:4px;padding:5px 10px;cursor:pointer;margin-left:8px;white-space:nowrap}
.qr-btn:hover{background:#eceff5}
.qr-modal{position:fixed;inset:0;z-index:200;display:none;place-items:center;background:rgba(14,15,17,.55)}
.qr-modal.open{display:grid}
.qr-card{background:#fff;border-radius:8px;padding:28px 30px;text-align:center;max-width:88vw}
.qr-card img{width:min(340px,70vw);height:auto;display:block;margin:0 auto}
.qr-card .u{font-size:13px;color:#767b83;margin-top:12px;word-break:break-all}
.qr-card .c{margin-top:14px;font-weight:800;font-size:13px;color:#22406e;cursor:pointer;border:1px solid #22406e;border-radius:4px;padding:6px 16px;background:none;font-family:inherit}
.soudan-fab{position:fixed;right:18px;bottom:18px;z-index:90;background:#33513f;color:#fff;font-weight:800;font-size:14px;padding:12px 18px;border-radius:999px;text-decoration:none;box-shadow:0 4px 16px rgba(0,0,0,.25);white-space:nowrap}
.soudan-fab:hover{background:#274031;color:#fff;text-decoration:none}
@media(max-width:600px){.soudan-fab{font-size:13px;padding:10px 15px}}`;
  const st=document.createElement('style'); st.textContent=css; document.head.appendChild(st);
  const bar=document.querySelector('header.bar .wrap');
  if(bar){
    const b=document.createElement('button'); b.className='qr-btn'; b.type='button'; b.textContent='QR';
    const fs=bar.querySelector('.fs-btns');
    if(fs) fs.appendChild(b); else bar.appendChild(b);
    const m=document.createElement('div'); m.className='qr-modal';
    m.innerHTML=`<div class="qr-card"><img src="${R}qr/sekita_qr.png" alt="このサイトのQRコード"><div class="u">a-tozak.github.io/sekiden-kenshu</div><button class="c" type="button">とじる</button></div>`;
    document.body.appendChild(m);
    b.addEventListener('click',()=>m.classList.add('open'));
    m.addEventListener('click',e=>{ if(e.target===m||e.target.classList.contains('c')) m.classList.remove('open'); });
  }
  const fab=document.createElement('a'); fab.className='soudan-fab';
  fab.href='https://lin.ee/Tay8XPQ'; fab.target='_blank'; fab.rel='noopener';
  fab.textContent='相談窓口';
  document.body.appendChild(fab);
})();
