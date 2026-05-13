with open('index.html', 'r') as f:
    content = f.read()

old_insights = content[content.find('<!-- BLOG / INSIGHTS -->'):content.find('<!-- CONTACT -->')]

new_tutorials = '''<!-- TUTORIALS -->
<section id="tutorials" class="section section-alt">
  <div class="container">
    <div class="section-label">Free Tutorials</div>
    <h2 class="section-title">Lectures & Tutorials</h2>
    <p class="section-intro">Free economics tutorials for students and the public — rigorous, accessible, and practical.</p>
    <div class="research-grid">
      <div class="research-card">
        <div style="width:40px;height:40px;background:#edf5f0;border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1rem">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2d6147" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
        </div>
        <h3>Microeconomics</h3>
        <p>Consumer theory, firm behavior, market structures, and welfare economics — from fundamentals to advanced topics.</p>
        <div class="research-tags"><span>Consumer Theory</span><span>Markets</span><span>Game Theory</span></div>
        <p style="font-size:0.78rem;color:#c49a1a;margin-top:1rem;font-weight:600">Coming Soon</p>
      </div>
      <div class="research-card">
        <div style="width:40px;height:40px;background:#edf5f0;border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1rem">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2d6147" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
        </div>
        <h3>Macroeconomics</h3>
        <p>GDP, inflation, unemployment, monetary and fiscal policy — understanding economies at the national and global level.</p>
        <div class="research-tags"><span>GDP</span><span>Monetary Policy</span><span>Growth Models</span></div>
        <p style="font-size:0.78rem;color:#c49a1a;margin-top:1rem;font-weight:600">Coming Soon</p>
      </div>
      <div class="research-card">
        <div style="width:40px;height:40px;background:#edf5f0;border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1rem">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2d6147" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
        </div>
        <h3>Econometrics</h3>
        <p>OLS, IV, panel data, time series, and causal inference — statistical tools for rigorous economic analysis.</p>
        <div class="research-tags"><span>OLS</span><span>Panel Data</span><span>Causal Inference</span></div>
        <p style="font-size:0.78rem;color:#c49a1a;margin-top:1rem;font-weight:600">Coming Soon</p>
      </div>
      <div class="research-card">
        <div style="width:40px;height:40px;background:#edf5f0;border-radius:8px;display:flex;align-items:center;justify-content:center;margin-bottom:1rem">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#2d6147" stroke-width="2"><path d="M4 19l4-8 4 4 4-6 4 10"/></svg>
        </div>
        <h3>Mathematics for Economics</h3>
        <p>Calculus, linear algebra, optimization, and probability — the essential mathematical toolkit for economists.</p>
        <div class="research-tags"><span>Calculus</span><span>Optimization</span><span>Linear Algebra</span></div>
        <p style="font-size:0.78rem;color:#c49a1a;margin-top:1rem;font-weight:600">Coming Soon</p>
      </div>
    </div>
  </div>
</section>

'''

content = content.replace(old_insights, new_tutorials)

# Fix research grid to 4 columns for tutorials
content = content.replace(
    '<div class="research-grid">',
    '<div class="research-grid" style="grid-template-columns:repeat(4,1fr)">',
    1  # only first occurrence (research section)
)

with open('index.html', 'w') as f:
    f.write(content)
print('Done')
