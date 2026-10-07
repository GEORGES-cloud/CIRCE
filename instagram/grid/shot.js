const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'}).catch(()=>chromium.launch());
const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+process.cwd()+'/grid.html',{waitUntil:'load'});await p.waitForTimeout(2500);
for(let i=1;i<=12;i++){await p.locator('#p'+i).screenshot({path:`post-${String(i).padStart(2,'0')}.png`});}
await b.close()})();
