// Make the original clickable cards keyboard accessible without changing their actions.
function prepareCards(root) {
  root.querySelectorAll('.mode-card,.hot-topic-chip,.example-chip,.cocoon-entry,.hot-topics-label,.agent-header').forEach(el => {
    if (el.dataset.keyboardReady) return;
    el.dataset.keyboardReady = 'true';
    el.tabIndex = 0;
    el.setAttribute('role', 'button');
    el.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); el.click(); }
    });
  });
}
prepareCards(document);
new MutationObserver(() => prepareCards(document)).observe(document.getElementById('agentTimeline'), {childList:true,subtree:true});
document.getElementById('topicInput').setAttribute('aria-label', '想了解的话题');
document.getElementById('mirrorInput').setAttribute('aria-label', '你的看法和判断依据');
