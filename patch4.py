with open('index.html', 'r') as f:
    content = f.read()

old = '''<section id="join" class="section">
  <div class="container">
    <div class="section-label">Get Involved</div>
    <h2 class="section-title">Join ThinkLab</h2>
    <p class="section-intro">We actively collaborate with students, researchers, and professionals who are passionate about economics and policy. Paid research opportunities available.</p>
    <div class="join-grid">
      <div class="join-card featured">
        <div class="join-badge">Paid Opportunity</div>
        <div class="join-icon">👨‍🎓</div>
        <h3>Research Assistants</h3>
        <p>Undergraduate and graduate students interested in hands-on research experience in economics and policy analysis. Paid positions available for qualified candidates.</p>
        <ul class="join-list">
          <li>Data collection & analysis</li>
          <li>Literature reviews</li>
          <li>Policy brief writing</li>
          <li>Co-authorship opportunities</li>
        </ul>
        <a href="mailto:research@thinklabep.org" class="btn-primary">Apply Now</a>
      </div>
      <div class="join-card">
        <div class="join-icon">🤝</div>
        <h3>Research Collaborators</h3>
        <p>Experienced researchers and faculty interested in collaborative projects, joint publications, and cross-institutional research partnerships.</p>
        <ul class="join-list">
          <li>Joint research projects</li>
          <li>Co-authored publications</li>
          <li>Seminar presentations</li>
          <li>Policy consultations</li>
        </ul>
        <a href="mailto:tahmid@thinklabep.org" class="btn-outline">Get in Touch</a>
      </div>
      <div class="join-card">
        <div class="join-icon">📢</div>
        <h3>Community Members</h3>
        <p>Anyone curious about economics and policy. Follow our work, engage with our content, attend events, and help spread research beyond academic walls.</p>
        <ul class="join-list">
          <li>Access free insights</li>
          <li>Attend public events</li>
          <li>Follow on social media</li>
          <li>Share our research</li>
        </ul>
        <a href="#contact" class="btn-outline">Stay Connected</a>
      </div>
    </div>
  </div>
</section>'''

new = '''<section id="join" class="section">
  <div class="container">
    <div class="section-label">Get Involved</div>
    <h2 class="section-title">Join ThinkLab</h2>
    <p class="section-intro">Paid and volunteer opportunities for students, researchers, and professionals.</p>
    <div class="join-grid" style="grid-template-columns:repeat(4,1fr);gap:1rem">
      <div class="join-card featured" style="padding:1.5rem">
        <div class="join-badge">Paid</div>
        <h3 style="font-size:1.05rem;margin-bottom:0.5rem">Research Assistant</h3>
        <p style="font-size:0.84rem;margin-bottom:1rem">Undergrad & grad students. Data analysis, policy writing, co-authorship.</p>
        <a href="mailto:research@thinklabep.org" class="btn-primary" style="font-size:0.8rem;padding:0.45rem 1rem">Apply</a>
      </div>
      <div class="join-card" style="padding:1.5rem">
        <h3 style="font-size:1.05rem;margin-bottom:0.5rem">Collaborator</h3>
        <p style="font-size:0.84rem;margin-bottom:1rem">Researchers & faculty. Joint projects and co-authored publications.</p>
        <a href="mailto:tahmid@thinklabep.org" class="btn-outline" style="font-size:0.8rem;padding:0.45rem 1rem">Connect</a>
      </div>
      <div class="join-card" style="padding:1.5rem">
        <h3 style="font-size:1.05rem;margin-bottom:0.5rem">Intern</h3>
        <p style="font-size:0.84rem;margin-bottom:1rem">Structured research internship in economics and policy analysis.</p>
        <a href="mailto:research@thinklabep.org" class="btn-outline" style="font-size:0.8rem;padding:0.45rem 1rem">Apply</a>
      </div>
      <div class="join-card" style="padding:1.5rem">
        <h3 style="font-size:1.05rem;margin-bottom:0.5rem">Volunteer</h3>
        <p style="font-size:0.84rem;margin-bottom:1rem">Support research outreach, public engagement, and dissemination.</p>
        <a href="mailto:contact@thinklabep.org" class="btn-outline" style="font-size:0.8rem;padding:0.45rem 1rem">Join</a>
      </div>
    </div>
  </div>
</section>'''

content = content.replace(old, new)
with open('index.html', 'w') as f:
    f.write(content)
print('Done')
