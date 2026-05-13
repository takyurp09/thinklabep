with open('index.html', 'r') as f:
    content = f.read()

# Fix tutorials grid to 4 columns in the tutorials section specifically
content = content.replace(
    '<div class="research-grid">',
    '<div class="research-grid" style="grid-template-columns:repeat(4,1fr);gap:1rem">',
    2  # second occurrence = tutorials section
)

with open('index.html', 'w') as f:
    f.write(content)
print('Done')
