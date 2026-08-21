import urllib.request
import re

url = "https://www.peoplenext.com/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')

# Search for elementor-element-4192a6b and find all inline styles in html associated with 4192a6b
styles_4192a6b = re.findall(r'[^{}]*4192a6b[^{]*\{[^}]+\}', html)
print("Styles found for 4192a6b in live site:")
for s in styles_4192a6b:
    print(s)

# Also let's check the exact section HTML in live site
idx_4192 = html.find('data-id="4192a6b"')
print("\nHTML around data-id=4192a6b:")
print(html[idx_4192-50:idx_4192+1200])
