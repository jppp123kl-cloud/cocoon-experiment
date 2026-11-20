"""Rebuild the two presentation entries without changing archived source files."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]

def sub(text, pattern, replacement, count=1):
    result, n = re.subn(pattern, replacement, text, count=count, flags=re.S)
    if n != count:
        raise ValueError(f"Expected {count} match(es), got {n}: {pattern}")
    return result

show = (ROOT / 'experiment/dashboard_20261110/showcase_5min.html').read_text()
show = sub(show, r'<title>.*?</title>', '<title>信息茧房研究 · 中期展示</title>')
show = show.replace('</head>', '<link rel="stylesheet" href="web/showcase-polish.css">\n</head>')
show = show.replace('<b>破茧助手</b><span>实验交互沙盘</span>', '<b>信息茧房研究</b><span>中期展示</span>')
show = sub(show, r'<div class="timer-wrap">.*?</div>', '')
show = sub(show, r'<button[^>]*data-open="qa"[^>]*>.*?</button>', '')
show = sub(show, r'<a class="btn" href="\./dashboard.html">.*?</a>', '<a class="btn" href="assistant.html" target="_blank" rel="noopener">体验破茧助手 ↗</a>')
show = sub(show, r'<div class="pace">.*?</div>', '')
show = sub(show, r'<aside id="teleprompter".*?</aside>', '')
show = sub(show, r'<button[^>]*data-tab="qa"[^>]*>.*?</button>', '')
show = sub(show, r'<section class="pane" data-pane="qa">.*?</section>', '')
show = show.replace('data-open="qa"', 'data-open="boundary"').replace('老师追问 Q1–Q5', '查看中期进展')
show = show.replace('href="./dashboard.html"', 'href="experiment/dashboard_20261110/dashboard.html" target="_blank" rel="noopener"')
show = sub(show, r'<section class="pane" data-pane="boundary">.*?</section>', '''<section class="pane" data-pane="boundary"><h3>我们走到哪一步了</h3>
<article class="ev"><h4>已完成</h4><p>助手原型、实验程序和小规模模型试验。三个现实议题加一个虚构情境，每个情境只有两名模型读者，不是真人受试者。</p></article>
<article class="ev"><h4>初步观察</h4><p>现实议题在实验前就已答对；虚构情境中，两种提供证据的方法都改善了核心事实回答，加入反思暂未显示额外优势。</p></article>
<article class="ev"><h4>接下来</h4><p>补齐四种信息环境比较、逐轮讨论与记忆更新，再把补充异见、纠错和反思分开检验，并增加独立重复。</p></article>
<p>这些结果用于调整实验设计，还不能证明助手普遍有效。</p></section>''')
show = sub(show, r'<button[^>]*data-open="boundary"[^>]*>规模明细</button>', '')
show = show.replace('>科研边界</button>', '>中期进展</button>').replace('>科研诚实边界与账本防伪</button>', '>中期进展</button>')
show = sub(show, r'(<button[^>]*id="honest-corner"[^>]*>).*?</button>', r'\1小规模模型试验 · 尚待扩大验证　↗</button>')
titles = [
    ('克隆分流', '实验怎么做', '同一起点，比较三种干预', '先阅读 8 轮材料，再复制状态，分别继续阅读、补充证据、加入助手反思。'),
    ('茧房现场', '阅读后的变化', '发言转述了错误数字，答题时仍不确定', '48 张帖子之后，模型发言与答卷呈现出不同变化。'),
    ('平行对决', '干预怎么做', '同样的证据，加入反思会有什么不同？', '保持起点和核查证据一致，比较三条路径的回答。'),
    ('双轨终局', '目前的结果', '证据改善了回答，反思的额外作用仍待验证', '现实议题起点已全对；虚构情境中，两种证据干预的核心事实结果相同。'),
]
for i, (old, name, title, lede) in enumerate(titles):
    show = sub(show, rf'(<section class="scene[^\"]*" id="scene-{i}".*?<h2>).*?</h2>', rf'\g<1>{title}</h2>')
    show = sub(show, rf'(<section class="scene[^\"]*" id="scene-{i}".*?<p class="lede">).*?</p>', rf'\g<1>{lede}</p>')
    show = sub(show, rf'(<button[^>]*data-go="{i}"[^>]*><span class="nc">.*?</span>).*?</button>', rf'\g<1>{name}</button>')
show = re.sub(r'<span class="win">.*?</span>', '', show)
show = show.replace("cur=0,teleMode='solo',timer=null,remain=300,dyeTimers=[]", 'cur=0,dyeTimers=[]')
show = show.replace(",tele=$('teleprompter')", '')
show = sub(show, r'function updateTele\(\).*?(?=function toggleTheme)', '')
show = sub(show, r"  else if\(t.hasAttribute\('data-tele'\)\).*?\n", '')
show = show.replace('  updateTele();\n', '').replace(',[data-tele]', '')
show = sub(show, r"  else if\(ev.key===' '\|\|ev.code==='Space'\).*?\n", '')
show = sub(show, r"  else if\(ev.key==='t'\|\|ev.key==='T'\).*?\n", '')
show = show.replace("$('btn-timer').addEventListener('click',toggleTimer);", '').replace('syncToggles();renderTimer();go(0);', 'syncToggles();go(0);')
data = re.search(r'(<script id="showcase-data" type="application/json">)(.*?)(</script>)', show, re.S)
payload = json.loads(data[2])
payload.pop('qa_cards', None)
for scene in payload['scenes']:
    for key in ('solo', 'team', 'window'):
        scene.pop(key, None)
    _, scene['name'], scene['title'], scene['lede'] = titles[scene['index']]
show = show[:data.start(2)] + json.dumps(payload, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + show[data.end(2):]
(ROOT / 'index.html').write_text(show)

assistant = (ROOT / 'vendor/cocoon-breaker-original/source_cdd042dba34f/index.html').read_text()
assistant = assistant.replace('</head>', '<link rel="stylesheet" href="web/assistant-polish.css">\n</head>')
# Only interface wording changes: original prompts, model calls and navigation stay intact.
before, scripts = assistant.split('<script>', 1)
for old, new in {
    '破茧认知助手支持两种方式体验，请任选一种开始': '先选一种方式，开始了解一个话题。',
    '<div class="icon">🔑</div>': '<div class="icon" aria-hidden="true">01</div>',
    '<div class="icon">🎮</div>': '<div class="icon" aria-hidden="true">02</div>',
    'API 模式</h3>': '连接模型</h3>',
    '输入自己的 API Key<br>体验完整 AI 分析': '填写模型服务密钥<br>分析你关心的话题',
    '模拟模式</h3>': '示例体验</h3>',
    '无需 API Key<br>内置高质量模拟数据': '无需密钥<br>用内置内容了解流程',
    'API Base URL（可选，默认 OpenAI）': '模型服务地址（可选，默认 OpenAI）',
    '<label>API Key</label>': '<label>服务密钥（API Key）</label>',
    '输入任意话题，看到完整认知图景': '多看一面，再做判断。',
    '🔥 今日热点 · 点击即可分析': '话题示例 · 点击填入',
    '输入你想了解的话题，或点击上方热点': '输入你关心的话题，或选择上方示例',
    '多 Agent 分析流水线': '一步步梳理这个话题',
    '基于上方 4 个 Agent 的分析结果生成 · 建议点击展开每个 Agent 查看详细推理过程': '汇总前面四步的结果。点击各步骤，可以查看分析内容。',
    '⚠️ 以下为模拟演示数据，信源链接仅供示意。使用 API 模式可获取真实可点击的信源链接。': '以下为内置示例，来源链接仅作示意。连接模型也不等于已完成事实核查。',
    '第5个Agent': '第五步 · 反思',
    '看完上方分析报告后，输入你对该话题的个人看法、立场和判断依据。第五步 · 反思将对照立场光谱和认知偏差库，帮你发现自己可能忽略的角度。': '看完报告，写下你的看法和依据。助手会结合这段话，提出你可能还没考虑的问题。',
    '回答下面 3 个问题，我们发现你的认知盲区和可能的偏差类型': '回顾你的阅读习惯。这是体验性自查，不是心理测量。',
}.items():
    before = before.replace(old, new)
before = sub(before, r'(<div class="disclaimer">)\s*.*?(</div>)', r'\1\n    课程项目体验原型 · 示例不属于实验数据，分析结果仍需自行核查\n  \2')
assistant = before + '<script>' + scripts
assistant = assistant.replace('</body>', '<script src="web/assistant-polish.js"></script>\n</body>')
(ROOT / 'assistant.html').write_text(assistant)
print('Rebuilt index.html and assistant.html from archived originals.')
