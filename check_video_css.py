import urllib.request
import re

url = "https://www.peoplenext.com/"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')

# Search for the video container styles
styles_a5bfda3 = re.findall(r'[^{}]*a5bfda3[^{]*\{[^}]+\}', html)
for s in styles_a5bfda3:
    print(s)

styles_ea1aa0c = re.findall(r'[^{}]*ea1aa0c[^{]*\{[^}]+\}', html)
for s in styles_ea1aa0c:
    print(s)

styles_dc4fb51 = re.findall(r'[^{}]*dc4fb51[^{]*\{[^}]+\}', html)
for s in styles_dc4fb51:
    print(s)
