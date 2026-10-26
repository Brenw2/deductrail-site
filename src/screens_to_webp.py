"""Resize app screenshots (home.png, trips.png, reports.png) to 640px wide WebP for the site.
Usage: python3 src/screens_to_webp.py <input-dir> <output-dir>   (needs Pillow)"""
import sys
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
for n in ['home', 'trips', 'reports']:
    im = Image.open(f'{src}/{n}.png').convert('RGB')
    im = im.resize((640, round(im.size[1] * 640 / im.size[0])), Image.LANCZOS)
    im.save(f'{dst}/screen-{n}.webp', 'WEBP', quality=84, method=6)
