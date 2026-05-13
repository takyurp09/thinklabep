with open('index.html', 'r') as f:
    content = f.read()

people_section = """
<!-- PEOPLE -->
<section id="people" class="section section-alt">
  <div class="container">
    <div class="section-label">Our People</div>
    <h2 class="section-title">The Team</h2>
    <div style="max-width:340px">
      <div class="founder-card">
        <div class="founder-img-wrap">
          <img src="assets/images/tahmid.jpg" alt="Muhammad Taky Tahmid" class="founder-img" />
        </div>
        <div class="founder-info">
          <h3>Muhammad Taky Tahmid</h3>
          <p class="founder-title">Founder &amp; Research Director</p>
          <p class="founder-bio">Economist and researcher focused on climate economics, development, and applied policy analysis.</p>
          <div class="founder-links">
            <a href="mailto:tahmid@thinklabep.org" class="founder-link">tahmid@thinklabep.org</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
"""

content = content.replace('<!-- RESEARCH -->', people_section + '\n<!-- RESEARCH -->')

with open('index.html', 'w') as f:
    f.write(content)
print('Done')
