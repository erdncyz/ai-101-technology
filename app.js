const $=s=>document.querySelector(s), presenter=new URLSearchParams(location.search).has('presenter');
let index=Math.min(slides.length-1,Math.max(0,(parseInt(location.hash.slice(1))||1)-1)),elapsed=0,running=false,lastTick=Date.now(),demoTimers=[],presenterWindow=null;
const fmt=s=>`${String(Math.floor(s/60)).padStart(2,'0')}:${String(s%60).padStart(2,'0')}`;
function go(n){
 if(!Number.isInteger(n)||n<0||n>=slides.length)return;
 demoTimers.forEach(clearTimeout);demoTimers=[];
 document.querySelectorAll('video').forEach(v=>v.pause());
 index=n;
 render();
 sync();
 // File previews may reject even fragment navigation. Keep slide state in memory.
 if(location.protocol!=='file:'){
  try{history.replaceState(null,'','#'+(n+1));}catch(_){}
 }
}
function render(){const s=slides[index];if(presenter){document.body.className='presenter';$('#stage').innerHTML=`<section class="presenter-view"><p class="share-warning">KONUŞMACI EKRANI · Paylaşımda yalnızca sunum penceresini seç.</p><div id="pTimer">${fmt(elapsed)} <small>/ 10:00</small></div><p>${index+1} / ${slides.length} · Bu slayt: ${s.time} saniye</p><h1>${s.title}</h1><div class="p-controls"><button onclick="command('prev')">← Önceki</button><button onclick="command('timer')">Başlat / Duraklat</button><button onclick="command('next')">Sonraki →</button><button onclick="command('reset')">Sayacı sıfırla</button></div><p id="notesText">${s.notes}</p><p class="next-title">SONRAKİ: ${slides[index+1]?.title||'Sunum tamamlandı.'}</p></section>`;return;}applyBodyChrome();$('#stage').innerHTML=`<section class="slide ${s.theme}" aria-label="Slayt ${index+1}: ${s.title}">${s.html}</section>`;$('#sectionLabel').textContent=s.label;$('#counter').textContent=`${String(index+1).padStart(2,'0')} / ${slides.length}`;$('#prev').disabled=index===0;$('#next').disabled=index===slides.length-1;$('#progress').style.width=`${(index+1)/slides.length*100}%`;document.title=`${index+1} · ${s.title} — AI 101`;}
function toggleTimer(){running=!running;lastTick=Date.now();tick();sync();}
function tick(){const now=Date.now();if(running){elapsed+=Math.floor((now-lastTick)/1000);lastTick+=Math.floor((now-lastTick)/1000)*1000;}if($('#timer'))$('#timer').textContent=`${running?'Ⅱ':'▷'} ${fmt(elapsed)}`;if($('#notesTimer'))$('#notesTimer').textContent=fmt(elapsed);if($('#pTimer'))$('#pTimer').innerHTML=`${fmt(elapsed)} <small>/ 10:00</small>`;if(!presenter)sync();}
function startTalk(){if(!running)toggleTimer();go(1);}
function runDemo(){$('.console').classList.remove('running');void $('.console').offsetWidth;$('.console').classList.add('running');document.querySelectorAll('.demo-row').forEach(r=>r.classList.remove('lit'));demoTimers.forEach(clearTimeout);document.querySelectorAll('.demo-row').forEach((r,i)=>demoTimers.push(setTimeout(()=>r.classList.add('lit'),400+i*1800)));$('#demoBtn').textContent='Tekrar oynat ↗';}
function applyBodyChrome(){
 const s=slides[index];
 const classes=[];
 if(presenter){document.body.className='presenter';return;}
 if(s.theme.includes('light'))classes.push('light');
 if(document.documentElement.classList.contains('present'))classes.push('present');
 document.body.className=classes.join(' ');
}
function syncFsButton(){
 const on=!!document.fullscreenElement||document.documentElement.classList.contains('present');
 const btn=$('#fsBtn');
 if(btn){btn.title=on?'Tam ekrandan çık (F / Esc)':'Tam ekran (F)';}
}
async function fullscreen(){
 // Native fullscreen tarayıcı barını gizler.
 // macOS’ta diğer ekran siyahsa: Sistem Ayarları → Masaüstü ve Dock →
 // “Ekranların ayrı Spaces’leri var” AÇIK olmalı (sonra çıkış/giriş).
 try{
  if(document.fullscreenElement){
   await document.exitFullscreen();
   return;
  }
  document.documentElement.classList.add('present');
  applyBodyChrome();
  const root=document.documentElement;
  const req=root.requestFullscreen||root.webkitRequestFullscreen;
  if(!req)throw new Error('unsupported');
  const result=req.call(root);
  if(result&&typeof result.then==='function')await result;
  toast('Tam ekran · diğer ekran siyahsa Spaces ayarını aç');
 }catch(e){
  const on=document.documentElement.classList.toggle('present');
  applyBodyChrome();
  syncFsButton();
  toast(on
   ?'Yedek sunum modu · Chrome’da Görünüm → Tam Ekrana Gir'
   :'Sunum modu kapandı');
 }
}
document.addEventListener('fullscreenchange',()=>{
 const on=!!document.fullscreenElement;
 document.documentElement.classList.toggle('present',on);
 applyBodyChrome();
 syncFsButton();
});
document.addEventListener('webkitfullscreenchange',()=>{
 const on=!!(document.fullscreenElement||document.webkitFullscreenElement);
 document.documentElement.classList.toggle('present',on);
 applyBodyChrome();
 syncFsButton();
});
function openOverview(){$('#modalContent').innerHTML='<h2>Sunum akışı</h2><p>'+slides.length+' sahne · 10 dakika</p><div class="overview-grid">'+slides.map((s,i)=>`<button class="${i===index?'current':''}" onclick="closeModal();go(${i})"><span>${String(i+1).padStart(2,'0')} / ${s.time} SN</span>${s.title}</button>`).join('')+'</div>';$('#modal').showModal();}
function closeModal(){$('#modal').close();}
let directPresenter=null;
window.addEventListener('pagehide',()=>{try{if(directPresenter&&!directPresenter.closed)directPresenter.close();}catch(_){}});
function openPresenterWindow(){
 try{
  if(directPresenter&&!directPresenter.closed){
   directPresenter.focus();
   toast('Not penceresi zaten açık — laptop ekranına taşı.');
   return;
  }
  const popup=window.open('about:blank','ai101-presenter-direct','width=1100,height=900,left=80,top=60');
  if(!popup){toast('Pop-up engellendi. Tarayıcıda bu site için pop-up’a izin ver, veya P ile paneli kullan.');return;}
  const doc=popup.document;
  doc.open();
  doc.write('<!doctype html><html lang="tr"><head><meta charset="utf-8"><title>Konuşmacı · AI 101</title><style>body{margin:0;background:#101013;color:#eee;font-family:-apple-system,BlinkMacSystemFont,Arial,sans-serif}main{max-width:920px;margin:auto;padding:38px}header{color:#aaa;font-size:13px;line-height:1.5}h1{font-size:38px;letter-spacing:-1px}#remoteTimer{font-size:48px;color:#ff916d;margin:24px 0}#remotePosition{color:#bbb}nav{display:flex;flex-wrap:wrap;gap:10px}button{font:inherit;color:#eee;background:#202025;border:1px solid #555;border-radius:9px;padding:12px 18px;cursor:pointer}button:disabled{opacity:.3;cursor:default}button:focus-visible{outline:2px solid #ff916d}#remoteBody{font-size:23px;line-height:1.65;white-space:pre-wrap}#remoteNext{border-top:1px solid #444;padding-top:20px;color:#aaa}#remoteStatus{color:#9bd5ad;font-size:13px;margin-top:18px}.setup{background:#ff774d18;border-left:2px solid #ff916d;padding:12px 14px;margin:0 0 22px;font-size:14px;line-height:1.55;color:#e8cfc3}</style></head><body><main><header>KONUŞMACI EKRANI · Bu pencereyi laptop’ta tut</header><p class="setup">1) Bu not penceresini kendi ekranına sürükle<br>2) Ana sunum penceresini projeksiyona taşı<br>3) Sunumda F ile tam ekran · oklarla ilerle</p><div id="remoteTimer"></div><div id="remotePosition"></div><h1 id="remoteTitle"></h1><nav><button id="remotePrev">← Önceki</button><button id="remoteToggle">Başlat / Duraklat</button><button id="remoteForward">Sonraki →</button><button id="remoteReset">Sayacı sıfırla</button></nav><p id="remoteStatus">Ana sunuma bağlı · oklar burada da çalışır</p><p id="remoteBody"></p><p id="remoteNext"></p></main></body></html>');
  doc.close();
  doc.getElementById('remotePrev').addEventListener('click',()=>go(index-1));
  doc.getElementById('remoteForward').addEventListener('click',()=>go(index+1));
  doc.getElementById('remoteToggle').addEventListener('click',()=>toggleTimer());
  doc.getElementById('remoteReset').addEventListener('click',()=>{elapsed=0;running=false;tick();sync();});
  doc.addEventListener('keydown',e=>{
   if(e.altKey||e.ctrlKey||e.metaKey)return;
   if(e.key==='ArrowRight'||e.key==='PageDown'||e.key===' '){e.preventDefault();go(index+1);}
   if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();go(index-1);}
   if(e.key.toLowerCase()==='t'){e.preventDefault();toggleTimer();}
  });
  directPresenter=popup;
  presenterWindow=null;
  updateDirectPresenter();
  if($('#speakerNotes'))closeNotes();
  toast('Not penceresini laptop’a taşı · sunumu projeksiyonda F ile aç');
  popup.focus();
 }catch(error){
  directPresenter=null;
  if(!$('#speakerNotes'))openPresenter();
  toast('Ayrı pencere açılamadı. Not paneli açık — P ile kapatıp açabilirsin.');
 }
}
function updateDirectPresenter(){
 if(!directPresenter||directPresenter.closed)return;
 try{
  const doc=directPresenter.document,s=slides[index];
  doc.getElementById('remoteTimer').textContent=fmt(elapsed)+' / 10:00';
  doc.getElementById('remotePosition').textContent=(index+1)+' / '+slides.length+' · Bu slayt: '+s.time+' saniye';
  doc.getElementById('remoteTitle').textContent=s.title;
  const body=doc.getElementById('remoteBody');
  if(body.textContent!==s.notes){body.textContent=s.notes;directPresenter.scrollTo(0,0);}
  doc.getElementById('remoteNext').textContent='SONRAKİ: '+(slides[index+1]?.title||'Sunum tamamlandı.');
  doc.getElementById('remotePrev').disabled=index===0;
  doc.getElementById('remoteForward').disabled=index===slides.length-1;
  doc.getElementById('remoteToggle').textContent=running?'Duraklat':'Başlat';
 }catch(error){directPresenter=null;toast('Konuşmacı bağlantısı kapandı. Not panelini yeniden açabilirsin.');}
}
const targetOrigin=location.origin==='null'?'*':location.origin;
function sync(){updateNotes();updateDirectPresenter();if(presenterWindow&&!presenterWindow.closed)presenterWindow.postMessage({type:'ai101-state',index,elapsed,running},targetOrigin);}
let commandSequence=0,pendingCommands=new Map();
function localCommand(action){
 if(action==='prev')go(index-1);
 if(action==='next')go(index+1);
 if(action==='timer')toggleTimer();
 if(action==='reset'){elapsed=0;running=false;tick();}
}
function command(action){
 if(!window.opener||window.opener.closed){localCommand(action);return;}
 const requestId=++commandSequence;
 const fallback=setTimeout(()=>{
  pendingCommands.delete(requestId);
  localCommand(action);
  toast('Ana sunumla bağlantı yok; yalnızca bu penceredeki notlar ilerliyor.');
 },1000);
 pendingCommands.set(requestId,fallback);
 try{window.opener.postMessage({type:'ai101-command',action,requestId},targetOrigin);}
 catch(_){clearTimeout(fallback);pendingCommands.delete(requestId);localCommand(action);}
}

window.addEventListener('message',e=>{if(location.origin!=='null'&&e.origin!==location.origin)return;if(presenter&&e.source===window.opener&&e.data?.type==='ai101-ack'){clearTimeout(pendingCommands.get(e.data.requestId));pendingCommands.delete(e.data.requestId);return;}if(presenter&&e.source===window.opener&&e.data?.type==='ai101-state'){let changed=index!==e.data.index;index=e.data.index;elapsed=e.data.elapsed;running=false;if(changed)render();tick();}else if(!presenter&&e.source===presenterWindow&&e.data?.type==='ai101-command'){e.source.postMessage({type:'ai101-ack',requestId:e.data.requestId},targetOrigin);const a=e.data.action;if(a==='prev')go(index-1);if(a==='next')go(index+1);if(a==='timer')toggleTimer();if(a==='reset'){elapsed=0;running=false;tick();}}});
function toast(t){$('#toast').textContent=t;$('#toast').style.display='block';setTimeout(()=>$('#toast').style.display='none',4500);}
window.addEventListener('hashchange',()=>{const n=Math.min(slides.length-1,Math.max(0,(parseInt(location.hash.slice(1))||1)-1));if(n!==index)go(n);});
window.addEventListener('keydown',e=>{if(e.altKey||e.ctrlKey||e.metaKey||e.target.closest('video,input,textarea'))return;if($('#modal').open)return;if(e.key==='Escape'){if(document.fullscreenElement||document.webkitFullscreenElement){e.preventDefault();(document.exitFullscreen||document.webkitExitFullscreen).call(document);return;}if(document.documentElement.classList.contains('present')){e.preventDefault();document.documentElement.classList.remove('present');applyBodyChrome();syncFsButton();return;}}if(['ArrowRight','ArrowDown','PageDown',' ','ArrowLeft','ArrowUp','PageUp','Home','End'].includes(e.key)){if(e.key===' '&&e.target.closest('button,a'))return;e.preventDefault();}if(presenter){if(['ArrowRight','PageDown',' '].includes(e.key))command('next');if(['ArrowLeft','PageUp'].includes(e.key))command('prev');if(e.key.toLowerCase()==='t')command('timer');return;}if(['ArrowRight','ArrowDown','PageDown',' '].includes(e.key))go(index+1);if(['ArrowLeft','ArrowUp','PageUp'].includes(e.key))go(index-1);if(e.key==='Home')go(0);if(e.key==='End')go(slides.length-1);if(e.key.toLowerCase()==='f')fullscreen();if(e.key.toLowerCase()==='g')openOverview();if(e.key.toLowerCase()==='p')openPresenter();if(e.key.toLowerCase()==='n')openPresenterWindow();if(e.key.toLowerCase()==='t')toggleTimer();});
let touch=null;$('#stage').addEventListener('touchstart',e=>{if(e.target.closest('video,button'))return;touch=[e.changedTouches[0].clientX,e.changedTouches[0].clientY];},{passive:true});$('#stage').addEventListener('touchend',e=>{if(!touch)return;const dx=e.changedTouches[0].clientX-touch[0],dy=e.changedTouches[0].clientY-touch[1];if(Math.abs(dx)>65&&Math.abs(dx)>Math.abs(dy)*1.5)go(index+(dx<0?1:-1));touch=null;},{passive:true});

function chooseTask(button,n){document.querySelectorAll('.choice-grid button').forEach(b=>{b.classList.remove('selected');b.setAttribute('aria-pressed','false');});button.classList.add('selected');button.setAttribute('aria-pressed','true');const answers=['AI ilgili bölümü bulabilir. Kararın güncelliğini ve kaynağını kontrol edersin.','AI ilk hâli kurabilir. Neyin kullanıcıya değer kattığını birlikte sınarsınız.','AI seçenekleri karşılaştırabilir. Hangi ödünleşimi kabul edeceğinize siz karar verirsiniz.','AI konuşmaya hazırlanmanı sağlayabilir. İlişkiyi kurmak ve konuşmayı yapmak sana kalır.'];$('#taskAnswer').textContent=answers[n];}
function fanView(n,button){document.querySelectorAll('.fan-tabs button').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));const views=[['“İlk 25 dakikada ne kaçırdım?”','Önemli olayların kısa özeti.<br>İzleyebileceğin ilgili anlara bağlantılar.'],['“Burada neden ofsayt verildi?”','Pozisyonun anlaşılır açıklaması.<br>Kuralı ilgili görüntüyle birlikte keşfetme.'],['“Bu değişiklik oyunu nasıl etkiler?”','Diziliş ve oyuncu rolleri üzerinden olası etkiler.<br>Doğrulanmış olay ile yorumun ayrı gösterimi.']];$('#fanOutput').innerHTML='<div class="fan-question">'+views[n][0]+'</div><div class="fan-response"><span>ÖNERİLEN DENEYİM</span><p>'+views[n][1]+'</p></div>';}

function revealMath(button){document.querySelectorAll(".quiz-options button").forEach(b=>b.classList.remove("selected"));button.classList.add("selected");document.querySelector("#mathAnswer").innerHTML="<strong>0,95¹⁰ ≈ %60</strong><span>Tüm adımların doğru olması gerektiği varsayımda.<br>Bu yüzden ara kontrol, test ve düzeltme döngüsü kurarız.</span>";}

function revealDelivery(){document.querySelector("#deliveryAnswer").innerHTML="<span>UÇTAN UCA SÜRE</span><strong>≈ %23</strong><p>azalır. 12 kat değil.</p>";}

function openPresenter(){
 let panel=document.querySelector('#speakerNotes');
 if(panel){closeNotes();return;}
 panel=document.createElement('aside');
 panel.id='speakerNotes';
 panel.setAttribute('aria-label','Konuşmacı notları');
 panel.innerHTML='<div class="notes-head"><b>Konuşmacı notları</b><button onclick="closeNotes()" aria-label="Notları kapat">×</button></div><p class="notes-warning">Bu panel ekran paylaşımında görünür. Gizli notlar için ayrı pencereyi kullanıp yalnızca sunumu paylaş.</p><div class="notes-controls"><button onclick="go(index-1)" aria-label="Notlarda önceki slayt">←</button><span id="notesPosition"></span><button onclick="go(index+1)" aria-label="Notlarda sonraki slayt">→</button><button onclick="toggleTimer()" id="notesTimer">00:00</button></div><h2 id="notesTitle"></h2><p id="notesBody"></p><p id="notesNext"></p><button class="notes-popout" onclick="openPresenterWindow()">Ayrı pencerede aç ↗</button><p class="notes-hint">Ayrı pencere açılmıyorsa notları bu panelden kullanabilirsin.</p>';
 document.body.appendChild(panel);
 $('#presenterBtn')?.setAttribute('aria-expanded','true');
 updateNotes();
 panel.querySelector('button')?.focus();
}
function updateNotes(){
 if(!$('#speakerNotes'))return;
 const s=slides[index];
 $('#notesPosition').textContent=(index+1)+' / '+slides.length+' · '+s.time+' sn';
 $('#notesTitle').textContent=s.title;
 $('#notesBody').textContent=s.notes;
 $('#notesNext').textContent='Sonraki: '+(slides[index+1]?.title||'Sunum tamamlandı.');
 $('#notesTimer').textContent=fmt(elapsed);
}
function closeNotes(){
 $('#speakerNotes')?.remove();
 $('#presenterBtn')?.setAttribute('aria-expanded','false');
}
window.addEventListener('keydown',e=>{if(e.key==='Escape'&&$('#speakerNotes'))closeNotes();});

function openInfo(){
 $('#modalContent').innerHTML=`<h2>${slides.length} sahne · 10 dakika</h2>
 <p>Oklar / boşluk: ilerle · F: tam ekran · Esc: çık · G: sahne seçici · P: not paneli · N: 2. ekran notları · T: sayaç. Diğer ekran siyahsa: Sistem Ayarları → Masaüstü ve Dock → “Ekranların ayrı Spaces’leri var” açık olsun. 11. sahnede kısa videoyu oynat.</p>
 <h2>Kaynaklar ve önerilen bağlantılar</h2>
 <ul class="source-list">
  <li><a href="https://developers.openai.com/api/docs/models" target="_blank" rel="noopener">OpenAI Model Catalog — model seçimi ve API fiyatları</a></li>
  <li><a href="https://mercury-ai-bench.netlify.app/" target="_blank" rel="noopener">Mercury AI Bench — işe göre model ve fiyat-performans</a></li>
  <li><a href="https://www.youtube.com/@venelin_valkov/videos" target="_blank" rel="noopener">Venelin Valkov — aynı prompt ile model karşılaştırmaları</a></li>
  <li><a href="https://cloud.google.com/blog/products/infrastructure/measuring-the-environmental-impact-of-ai-inference" target="_blank" rel="noopener">Google — medyan Gemini isteminin enerji ölçümü</a></li>
  <li><a href="https://modelcontextprotocol.io/" target="_blank" rel="noopener">Model Context Protocol — resmi dokümantasyon</a></li>
  <li><a href="https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/" target="_blank" rel="noopener">OpenAI — agent oluşturma rehberi</a></li>
  <li><a href="https://www.canirun.ai/model/qwen3-8b" target="_blank" rel="noopener">CanIRun.ai — Qwen 3 8B donanım gereksinimi</a></li>
  <li><a href="https://huggingface.co/models?inference_provider=all&sort=trending" target="_blank" rel="noopener">Hugging Face — model kataloğu</a></li>
  <li><a href="https://huggingface.co/docs/hub/en/local-apps" target="_blank" rel="noopener">Hugging Face — modelleri lokal çalıştırma</a></li>
  <li><a href="https://www.promptingguide.ai/" target="_blank" rel="noopener">Prompt Engineering Guide</a></li>
  <li><a href="https://agentskills.io/" target="_blank" rel="noopener">Agent Skills — açık format ve resmî spesifikasyon</a></li>
  <li><a href="https://github.com/openai/plugins" target="_blank" rel="noopener">OpenAI Plugins — güncel OpenAI skill ve plugin örnekleri</a></li>
  <li><a href="https://github.com/anthropics/skills" target="_blank" rel="noopener">Anthropic Skills — resmî skill örnekleri</a></li>
  <li><a href="https://skills.sh/" target="_blank" rel="noopener">skills.sh — topluluk skill dizini</a></li>
  <li><a href="https://github.com/garrytan/gstack" target="_blank" rel="noopener">gstack — resmi GitHub deposu</a></li>
  <li><a href="https://graphify.com/" target="_blank" rel="noopener">Graphify — ürün ve güvenlik açıklamaları</a></li>
 </ul>
 <p>Fiyatlar 8 Eylül 2026 tarihinde erişilen resmi katalogdaki USD / 1M token liste fiyatlarıdır ve değişebilir. CanIRun.ai kartı erişilen sayfa verilerinden sadeleştirilmiştir. Skill kaynaklarında resmî depolar başlangıç noktası, skills.sh ise keşif dizini olarak gösterilir; herhangi bir skill kullanılmadan önce içeriği, scriptleri, izinleri ve sürümü incelenmelidir. Graphify sahnesi, sitenin kendi FastAPI graph ekran görüntüsünü kullanır; çevrimdışıyken temsili grafik gösterilir. Graphify güvenlik iddiaları üretici beyanıdır; kurumsal kullanım ayrıca kaynak, paket, izin ve veri akışı incelemesi gerektirir.</p>
 <p><a href="Konusmaci-notlari.md" download>Konuşmacı metnini indir ↗</a></p>`;
 $('#modal').showModal();
}

function parseSpeakerNotes(md){
 const heading=/^##\s+(\d+)\.\s+(.+?)\s+—\s+(\d+)\s+sn\s*$/gm;
 const hits=[];
 let m;
 while((m=heading.exec(md))){
  hits.push({n:+m[1],title:m[2].trim(),time:+m[3],at:m.index});
 }
 return hits.map((hit,i)=>{
  const start=md.indexOf('\n',hit.at)+1;
  const end=i+1<hits.length?hits[i+1].at:md.length;
  return {n:hit.n,title:hit.title,time:hit.time,notes:md.slice(start,end).replace(/^\s+|\s+$/g,'')};
 });
}
function applySpeakerNotes(md){
 parseSpeakerNotes(md).forEach(sec=>{
  const slide=slides[sec.n-1];
  if(!slide)return;
  slide.title=sec.title;
  slide.time=sec.time;
  slide.notes=sec.notes;
 });
}
function moveSlide(from,to){
 const [slide]=slides.splice(from,1);
 slides.splice(to,0,slide);
}
async function loadSpeakerNotesMarkdown(){
 const embedded=typeof SPEAKER_NOTES_MD==='string'?SPEAKER_NOTES_MD:'';
 if(location.protocol==='file:')return embedded;
 try{
  const res=await fetch('Konusmaci-notlari.md',{cache:'no-store'});
  if(res.ok)return await res.text();
 }catch(err){
  console.warn('Konuşmacı notları fetch edilemedi, gömülü kopya kullanılıyor:',err);
 }
 return embedded;
}
async function boot(){
 try{
  const md=await loadSpeakerNotesMarkdown();
  if(!md)throw new Error('not metni boş');
  applySpeakerNotes(md);
  const missing=slides.findIndex(s=>!s.notes);
  if(missing!==-1){
   if(typeof SPEAKER_NOTES_MD==='string'&&SPEAKER_NOTES_MD&&md!==SPEAKER_NOTES_MD){
    applySpeakerNotes(SPEAKER_NOTES_MD);
   }
   if(slides.findIndex(s=>!s.notes)!==-1)throw new Error('Eksik not: slayt '+(missing+1));
  }
 }catch(err){
  console.warn('Konuşmacı notları yüklenemedi:',err);
  slides.forEach((s,i)=>{
   if(!s.title)s.title='Slayt '+(i+1);
   if(!s.time)s.time=40;
   if(!s.notes)s.notes='';
  });
  toast('Konuşmacı notları yüklenemedi.');
 }
 moveSlide(5,2);
 render();
 setInterval(tick,1000);
}
boot();
