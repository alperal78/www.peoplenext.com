with open("fresh_main_body.html", "r", encoding="utf-8") as f:
    html = f.read()

import re
styles_a5bfda3 = re.findall(r'[^{}]*a5bfda3[^{]*\{[^}]+\}', html)
for s in styles_a5bfda3:
    print(s)

styles_ea1aa0c = re.findall(r'[^{}]*ea1aa0c[^{]*\{[^}]+\}', html)
for s in styles_ea1aa0c:
    print(s)

styles_dc4fb51 = re.findall(r'[^{}]*dc4fb51[^{]*\{[^}]+\}', html)
for s in styles_dc4fb51:
    print(s)
