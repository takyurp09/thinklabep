with open('index.html', 'r') as f:
    content = f.read()

# 1. Add Team to nav links
content = content.replace(
    '<li><a href="#about">About</a></li>',
    '<li><a href="#about">About</a></li>\n      <li><a href="#people">Team</a></li>'
)

# 2. Remove founder card from About section
content = content.replace(
    '<div class="about-founder">',
    '<div class="about-founder" style="display:none">'
)

# 3. Fix research icons - remove cheap emojis, use text symbols
content = content.replace('<div class="research-icon">🌡️</div>', '<div class="research-icon">01.</div>')
content = content.replace('<div class="research-icon">📊</div>', '<div class="research-icon">02.</div>')
content = content.replace('<div class="research-icon">🏛️</div>', '<div class="research-icon">03.</div>')

# 4. Rename second pub card to Ongoing Research
content = content.replace(
    '<span class="pub-type upcoming">Coming Soon</span>',
    '<span class="pub-type upcoming">Ongoing Research</span>'
)
content = content.replace(
    '<h3 class="pub-title">More research underway...</h3>',
    '<h3 class="pub-title">Ongoing Research Projects</h3>'
)
content = content.replace(
    'ThinkLab is actively developing new research projects. Follow us on social media or subscribe to stay updated on upcoming publications and working papers.',
    'ThinkLab has several active research projects currently underway. Contact us to learn more about ongoing work and collaboration opportunities.'
)

# 5. Fix Join section - compress and update roles
old_join = '''      <div class="join-grid">
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
    </div>'''

new_join = '''      <div class="join-grid" style="grid-template-columns:repeat(4,1fr);gap:1rem">
        <div class="join-card featured" style="padding:1.5rem">
          <div class="join-badge">Paid</div>
          <h3 style="font-size:1.1rem">Research Assistant</h3>
          <p style="font-size:0.84rem">Undergrad & graduate students. Hands-on research, data analysis, policy writing.</p>
          <a href="mailto:research@thinklabep.org" class="btn-primary" style="font-size:0.8rem;padding:0.5rem 1rem">Apply</a>
        </div>
        <div class="join-card" style="padding:1.5rem">
          <h3 style="font-size:1.1rem">Collaborator</h3>
          <p style="font-size:0.84rem">Researchers & faculty. Joint projects, co-authored publications, policy consultations.</p>
          <a href="mailto:tahmid@thinklabep.org" class="btn-outline" style="font-size:0.8rem;padding:0.5rem 1rem">Connect</a>
        </div>
        <div class="join-card" style="padding:1.5rem">
          <h3 style="font-size:1.1rem">Intern</h3>
          <p style="font-size:0.84rem">Students seeking structured research internship experience in economics and policy.</p>
          <a href="mailto:research@thinklabep.org" class="btn-outline" style="font-size:0.8rem;padding:0.5rem 1rem">Apply</a>
        </div>
        <div class="join-card" style="padding:1.5rem">
          <h3 style="font-size:1.1rem">Volunteer</h3>
          <p style="font-size:0.84rem">Contribute to research dissemination, outreach, and public engagement efforts.</p>
          <a href="mailto:contact@thinklabep.org" class="btn-outline" style="font-size:0.8rem;padding:0.5rem 1rem">Join</a>
        </div>
      </div>'''

content = content.replace(old_join, new_join)

# 6. Compress research section padding
content = content.replace(
    'Our research spans multiple domains at the intersection of economics, environment, and public policy — with a focus on real-world implications.',
    'Economics, environment, and public policy — with a focus on real-world implications.'
)

with open('index.html', 'w') as f:
    f.write(content)
print('Done')
