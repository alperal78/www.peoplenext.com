import urllib.request
import re

url = "https://www.peoplenext.com/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')

# Search for 4192a6b styles
styles = re.findall(r'[^{}]*4192a6b[^{]*\{[^}]+\}', html)
for s in styles:
    print(s)

# Also container max-width in Elementor
cw = re.findall(r'(\.elementor-section\.elementor-section-boxed\s*>\s*\.elementor-container\s*\{[^}]+\})', html)
print("Section boxed container:", cw)
