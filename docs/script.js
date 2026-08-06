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
