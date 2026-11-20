const {chromium}=require('playwright');
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const {pathToFileURL}=require('node:url');

(async()=>{
  const root=process.argv[2]||path.resolve(__dirname,'..');
  const shots=process.env.COCOON_SCREENSHOT_DIR;
  if(shots)fs.mkdirSync(shots,{recursive:true});
  const read=f=>fs.readFileSync(path.join(root,f),'utf8');
  const original=read('experiment/dashboard_20261110/showcase_5min.html');
  const current=read('index.html');
  // Preserve the four animated scenes; only retarget the two final-scene utility links.
  const stages=s=>[...s.matchAll(/<div class="stage-box">([\s\S]*?)<\/div><\/section>/g)].map(m=>m[1]);
  assert.equal(stages(current).length,4);
  assert.deepEqual(stages(current),stages(original.replaceAll('data-open="qa"','data-open="boundary"').replaceAll('老师追问 Q1–Q5','查看中期进展').replaceAll('href="./dashboard.html"','href="experiment/dashboard_20261110/dashboard.html" target="_blank" rel="noopener"')));
  const payload=s=>JSON.parse(s.match(/<script id="showcase-data" type="application\/json">([\s\S]*?)<\/script>/)[1]);
  for(const [key,value] of Object.entries(payload(original))){
    if(!['scenes','qa_cards'].includes(key))assert.deepEqual(payload(current)[key],value,key);
  }
  // Restore the assistant's existing navigation, prompts and model behavior unchanged.
  const inline=s=>s.replace(/\r\n/g,'\n').match(/<script>([\s\S]*?)<\/script>/)[1];
  assert.equal(inline(read('assistant.html')),inline(read('vendor/cocoon-breaker-original/source_cdd042dba34f/index.html')));
  const browser=await chromium.launch({headless:true,executablePath:process.env.COCOON_BROWSER||(process.platform==='darwin'?'/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge':undefined)});
  try{
    const page=await browser.newPage({viewport:{width:1440,height:900}});
    const errors=[];page.on('pageerror',e=>errors.push(e.message));
    const goto=f=>page.goto(pathToFileURL(path.join(root,f)).href);
    const capture=async name=>{if(shots){await page.waitForTimeout(400);await page.screenshot({path:path.join(shots,name+'.png')});}};
    await goto('index.html');
    assert.equal(await page.locator('#teleprompter,#btn-timer,[data-tab="qa"],[data-open="qa"]').count(),0);
    await page.waitForSelector('#clone-stage.run');
    const motion=await page.locator('#clone-stage .smil').evaluateAll(es=>es.map(e=>e.outerHTML));assert(motion.length>0);
    await capture('midterm-scene-1');
    await page.click('[data-go="1"]');await page.click('[data-act="dye"]');
    await page.waitForFunction(()=>document.getElementById('dye-ind').textContent==='第 8/8 轮');
    assert(await page.locator('#dye-stage .lit').count()>0);
    await capture('midterm-scene-2');
    await page.locator('.scene.active [data-subject-btn="S02"]').click();
    assert.equal(await page.getAttribute('body','data-subject'),'S02');
    assert.equal(await page.textContent('#dye-ind'),'第 0/8 轮');
    await page.click('[data-go="2"]');await page.locator('.scene.active [data-round-btn="2"]').click();
    assert.equal(await page.getAttribute('body','data-round'),'2');
    await page.click('[data-act="pulse"]');await page.waitForTimeout(650);await capture('midterm-scene-3');
    await page.locator('.scene.active button[data-open="source"]').click();assert(await page.locator('#drawer.open').isVisible());
    assert(await page.locator('[data-pane="source"]').isVisible());await page.keyboard.press('Escape');
    await page.click('[data-go="3"]');await page.click('[data-metric-btn="brier"]');
    assert.equal(await page.getAttribute('body','data-metric'),'brier');await page.click('[data-metric-btn="acc"]');await capture('midterm-scene-4');
    await page.click('#btn-theme');assert.equal(await page.getAttribute('html','data-theme'),'dark');await capture('midterm-dark');
    await page.click('.tools [data-open="boundary"]');assert(await page.locator('[data-pane="boundary"]').isVisible());await page.keyboard.press('Escape');
    await page.keyboard.press('ArrowLeft');assert.equal(await page.getAttribute('body','data-scene'),'2');
    await goto('assistant.html');await capture('assistant-mode');
    await page.locator('.mode-card').first().click();assert(await page.locator('#apiInputs').isVisible());await page.click('#backBtn');assert(await page.locator('#apiInputs').isHidden());
    await page.locator('.mode-card').nth(1).focus();await page.keyboard.press('Enter');await page.click('#confirmBtn');assert(await page.locator('#modeModal').isHidden());await capture('assistant-home');
    await page.click('.cocoon-entry');await page.fill('#cocoonTopics','科技、互联网、人工智能');await page.fill('#cocoonChannels','知乎、微信公众号');await page.click('[onclick="generateCocoonProfile()"]');assert(await page.locator('#cocoonResult').isVisible());await page.locator('#cocoonResult [onclick="closeCocoonCheck()"]').click();
    await page.locator('.hot-topic-chip').nth(2).click();await page.click('.topic-input-wrap .btn');
    await page.waitForSelector('#resultSectionInline.active',{timeout:25000});assert.equal(await page.locator('.agent-status.complete').count(),4);
    await page.locator('.agent-header').first().click();
    await page.fill('#mirrorInput','我认为人工智能会取代所有程序员，因为代码都能自动生成。');await page.click('#mirrorBtn');
    await page.waitForSelector('#mirrorGrid .mirror-card');assert(await page.locator('#mirrorResult').isVisible());
    await page.locator('#resultSectionInline').scrollIntoViewIfNeeded();await capture('assistant-report');
    await page.click('[onclick="resetApp()"]');assert(await page.locator('#inputSection').isVisible());assert(await page.locator('#analysisArea').isHidden());
    await page.fill('#topicInput','电动车真的环保吗？');await page.click('.topic-input-wrap .btn');
    await page.click('[onclick="changeMode()"]');assert(await page.locator('#modeModal').isVisible());
    await goto('assistant.html');await page.locator('.mode-card').nth(1).click();await page.click('#confirmBtn');
    await page.fill('#topicInput','电动车真的环保吗？');await page.click('.topic-input-wrap .btn');await page.click('[onclick="stopAnalysis()"]');assert(await page.locator('#stopBar').isHidden());
    for(const width of [1440,1024,768,390,320]){
      await page.setViewportSize({width,height:900});
      for(const file of ['index.html','assistant.html']){
        await goto(file);
        assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),file+' overflow '+width);
        if(file==='assistant.html'){
          await page.locator('.mode-card').nth(1).click();await page.click('#confirmBtn');
          assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'assistant home overflow '+width);
        }
        if(width===390)await capture(file.replace('.html','')+'-mobile');
      }
    }
    assert.deepEqual(errors,[]);
    console.log(JSON.stringify({passed:true,originalAnimatedStages:4,assistantOriginalLogic:'identical',widths:[1440,1024,768,390,320],checks:['clone','eight-round dye','subject and round switching','intervention pulse','metric switch','dark theme','source drawer','progress drawer','mode selection','self-check','four analysis steps','reflection','reset','stop','keyboard'],pageErrors:errors},null,2));
  }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exit(1)});
