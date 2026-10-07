const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'}).catch(()=>chromium.launch());
const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+process.cwd()+'/carrusel.html',{waitUntil:'load'});await p.waitForTimeout(2500);
for(let i=1;i<=8;i++){await p.locator('#s'+i).screenshot({path:`slide-0${i}.png`});}
await b.close()})();
