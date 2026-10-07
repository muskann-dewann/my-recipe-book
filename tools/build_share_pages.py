"""Builds one small page per recipe at r/<id>/index.html.
Each page carries that dish's photo, name and description, so a shared link shows a proper
preview on WhatsApp, then opens the recipe on the main site. Also makes 1200x630 preview photos.
Run after adding or renaming a recipe:  python3 tools/build_share_pages.py"""
import os, re, html
from PIL import Image

BASE = 'https://muskann-dewann.github.io/my-recipe-book/'
SITE = 'Muskan’s CookBook'
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(root, 'recipes.js'), encoding='utf-8').read()
recipes = re.findall(r"id: '([^']+)', no: '[^']*', name: '([^']+)'.*?tag: '([^']*)',\s*photo: '([^']+)'", src, re.S)
os.makedirs(os.path.join(root, 'photos/og'), exist_ok=True)
for rid, name, tag, photo in recipes:
    og = f'photos/og/{rid}.jpg'
    if not os.path.exists(os.path.join(root, og)):
        im = Image.open(os.path.join(root, photo)).convert('RGB'); W, H = im.size
        th = int(W * 630 / 1200); top = (H - th) // 2
        im.crop((0, top, W, top + th)).resize((1200, 630), Image.LANCZOS).save(os.path.join(root, og), quality=82, optimize=True, progressive=True)
    n, t = html.escape(name), html.escape(tag)
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{n} · {SITE}</title>
<meta name="description" content="{t}">
<meta property="og:type" content="article"><meta property="og:site_name" content="{SITE}">
<meta property="og:title" content="{n}"><meta property="og:description" content="{t}">
<meta property="og:image" content="{BASE}{og}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:url" content="{BASE}r/{rid}/"><meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{BASE}#{rid}">
<meta http-equiv="refresh" content="0; url=../../#{rid}">
<script>location.replace('../../#{rid}');</script>
</head><body><p><a href="../../#{rid}">Open {n}</a></p></body></html>
'''
    os.makedirs(os.path.join(root, 'r', rid), exist_ok=True)
    open(os.path.join(root, 'r', rid, 'index.html'), 'w', encoding='utf-8').write(page)
    print('built', rid)
