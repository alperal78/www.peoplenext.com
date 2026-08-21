import urllib.request
import ssl
import re

ssl_context = ssl._create_unverified_context()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

url = "https://www.peoplenext.com/success-factors/"

print(f"Downloading raw live HTML from: {url}")
try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ssl_context, timeout=15) as response:
        raw_html = response.read().decode('utf-8', errors='ignore')
        
    print(f"Successfully downloaded. Size: {len(raw_html)} bytes.")
    
    # 1. Search for c5e697 in the raw HTML head style blocks
    head_match = re.search(r'<head>(.*?)</head>', raw_html, re.DOTALL | re.IGNORECASE)
    if head_match:
        head_content = head_match.group(1)
        style_tags = re.findall(r'<style[^>]*>(.*?)</style>', head_content, re.DOTALL | re.IGNORECASE)
        print(f"Found {len(style_tags)} style tags in live head.")
        
        found_style = False
        for idx, style_content in enumerate(style_tags):
            if "c5e697" in style_content:
                found_style = True
                print(f"\n--- FOUND 'c5e697' in Live Head Style Tag {idx} ---")
                # Let's print selectors containing c5e697
                rules = style_content.split("}")
                for r in rules:
                    if "c5e697" in r:
                        print(f"  Rule: {r.strip()}}}")
                        
        if not found_style:
            print("c5e697 NOT found in any live head style tags!")
    else:
        print("Head section not found in raw HTML")
        
    # 2. Let's find all CSS stylesheet link elements in the raw head
    if head_match:
        links = re.findall(r'<link[^>]+href=[\'"]([^"\']+\.css[^"\']*)[\'"]', head_content, re.IGNORECASE)
        print(f"\nFound {len(links)} CSS links in live head:")
        for l in links:
            if "wpfc-minified" in l or "post-1470" in l or "elementor/css" in l:
                print(f"  - {l}")
except Exception as e:
    print(f"Error downloading live HTML: {e}")
