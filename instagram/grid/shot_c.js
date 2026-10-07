const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'}).catch(()=>chromium.launch());
const p=await b.newPage({viewport:{width:1080,height:1350}});
for(let i=1;i<=12;i++){const d=`carrusel-${String(i).padStart(2,'0')}`;fs.mkdirSync(d,{recursive:true});
 fs.copyFileSync(`post-${String(i).padStart(2,'0')}.png`,`${d}/01.png`);
 await p.goto('file://'+process.cwd()+`/${d}.html`,{waitUntil:'load'});await p.waitForTimeout(1500);
 const n=await p.locator('section').count();
 for(let k=0;k<n;k++){await p.locator('section').nth(k).screenshot({path:`${d}/${String(k+2).padStart(2,'0')}.png`});}}
await b.close()})();
