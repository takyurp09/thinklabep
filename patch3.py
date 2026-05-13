with open('index.html', 'r') as f:
    content = f.read()

# 1. About section - make full width (remove grid, span whole page)
content = content.replace(
    '<div class="about-grid">',
    '<div class="about-grid" style="grid-template-columns:1fr;max-width:720px">'
)

# 2. Remove research icon duplicates (01. text inside icon div)
content = content.replace('<div class="research-icon">01.</div>', '')
content = content.replace('<div class="research-icon">02.</div>', '')
content = content.replace('<div class="research-icon">03.</div>', '')

# 3. Remove research num divs
content = content.replace('<div class="research-num">01</div>', '')
content = content.replace('<div class="research-num">02</div>', '')
content = content.replace('<div class="research-num">03</div>', '')

# 4. Add SVG icons for research cards
content = content.replace(
    '<h3>Climate Economics</h3>',
    '''<div style="width:40px;height:40px;background:#edf5f0;border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1rem">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2d6147" stroke-width="2"><path d="M12 2a10 10 0 1 0 0 20A10 10 0 0 0 12 2z"/><path d="M12 6v6l4 2"/></svg>
    </div>
    <h3>Climate Economics</h3>'''
)
content = content.replace(
    '<h3>Development Economics</h3>',
    '''<div style="width:40px;height:40px;background:#edf5f0;border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1rem">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2d6147" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
    </div>
    <h3>Development Economics</h3>'''
)
content = content.replace(
    '<h3>Applied Policy Analysis</h3>',
    '''<div style="width:40px;height:40px;background:#edf5f0;border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1rem">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2d6147" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
    </div>
    <h3>Applied Policy Analysis</h3>'''
)

# 5. Shorten research card text
content = content.replace(
    'Studying the economic consequences of climate shocks, environmental policy, and the links between climate change and industrial structure in developing economies.',
    'Economic consequences of climate shocks and environmental policy in developing economies.'
)
content = content.replace(
    'Examining economic growth, poverty, structural transformation, and the role of institutions and policy in driving sustainable development outcomes.',
    'Economic growth, poverty, structural transformation, and the role of institutions in development.'
)
content = content.replace(
    'Translating rigorous economic research into actionable policy recommendations across fiscal, trade, labor, and environmental policy domains.',
    'Translating research into actionable recommendations across fiscal, trade, and labor policy.'
)

# 6. Reduce section padding
content = content.replace('.section { padding: 6rem 0; }', '.section { padding: 4rem 0; }')
content = content.replace('.section-alt { background: var(--paper); }', '.section-alt { background: var(--paper); }\n.research-card { padding: 1.4rem; }')

with open('index.html', 'w') as f:
    f.write(content)
print('Done')
