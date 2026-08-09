// 碩田学園 生成AI研修 共通スクリプト（ナビ現在地・reveal・プロンプトのコピー）

// active nav on scroll
const navLinks=[...document.querySelectorAll('.nav a')].filter(a=>a.getAttribute('href').startsWith('#'));
const navMap=navLinks.map(a=>({a,el:document.querySelector(a.getAttribute('href'))})).filter(x=>x.el);
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
const io=new IntersectionObserver(es=>es.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target);} }),{threshold:.08});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));

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
