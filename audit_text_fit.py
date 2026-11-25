#!/usr/bin/env python3
"""Independent text-fit + pin-collision audit for the fixed entry.

Imports the story data from generate.py and re-wraps every rendered
block with the same fonts and widths main() uses. Fails (exit 1) if
any block needs more lines than the renderer allows (i.e. would be
silently truncated by the [:n] slices) or if any two map pins overlap.
"""
import sys
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, "/home/hatch/workspace/makefun/news-image-20261125/fix")
import generate as G

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

img = Image.new("RGB", (1024, 1024))
d = ImageDraw.Draw(img)
fails = []
notes = []


def check(name, text, font_path, size, max_w, max_lines=None):
    f = ImageFont.truetype(font_path, size)
    lines = G.wrap(d, text, f, max_w)
    w = d.textlength(text, font=f) if max_lines is None else None
    if max_lines is not None and len(lines) > max_lines:
        fails.append(f"{name}: {len(lines)} lines > {max_lines} allowed: {lines}")
    elif max_lines is None and w > max_w:
        fails.append(f"{name}: {w:.1f}px > {max_w}px")
    notes.append(f"{name}: {len(lines)} line(s)" + (f" (max {max_lines})" if max_lines else f", {w:.1f}px / {max_w}px"))


M, R = 30, 994
cw = (R - M - 2 * 14) // 3  # 312
gw = (R - M - 2 * 12) // 3  # 313

# Masthead subline + title
check("masthead subline",
      "WEDNESDAY, 25 NOVEMBER 2026  ·  36 STORIES  ·  9 REGIONS  ·  "
      "EVERY ONE FIRST REPORTED TODAY", SANS_B, 16, R - M)
check("masthead title", "THE WORLD IN ONE DAY", SERIF_B, 52, R - M)

# KPI strip
kw = (R - M - 5 * 6) // 6
for kpi in G.KPIS:
    check(f"KPI {kpi!r}", kpi, SANS_B, 12, kw)

# Leads
for i, (kick, head, deck, tag, scene) in enumerate(G.LEADS):
    check(f"lead{i+1} kicker", f"{i+1} · {kick}", SANS_B, 11, cw - 20)
    check(f"lead{i+1} headline", head, SERIF_B, 18, cw - 20, 2)
    check(f"lead{i+1} deck", deck, SERIF, 11, cw - 20, 3)
    check(f"lead{i+1} tag", tag, SANS_B, 9, cw - 20)

# Grid
for i, (kick, head, deck, tag, pic) in enumerate(G.GRID):
    tw_ = gw - 8 - 68
    check(f"grid{i+4} kicker", f"{i+4} · {kick}", SANS_B, 10, tw_)
    check(f"grid{i+4} headline", head, SERIF_B, 14, tw_, 2)
    check(f"grid{i+4} deck", deck, SERIF, 11, tw_, 2)

# ALSO (2 cols, 12 rows each)
aw = R - (M + 452 + 16)
col_w = (aw - 14) // 2
for num, beat, text, outlet in G.ALSO:
    check(f"ALSO #{num}", f"{beat} — {text} ({outlet})", SERIF, 11, col_w - 22, 2)

# Timeline
for t, s in G.TIMELINE:
    pass
line1 = "  ·  ".join(f"{t} — {s}" for t, s in G.TIMELINE[:3])
line2 = "  ·  ".join(f"{t} — {s}" for t, s in G.TIMELINE[3:])
check("timeline line1", line1, SANS_B, 10, R - M - 16)
check("timeline line2", line2, SANS_B, 10, R - M - 16)

# DATE CHECK + footer
check("DATE CHECK", G.DATE_CHECK, SANS, 10, R - M, 3)
check("footer", G.FOOTER, SANS, 11, R - M)
check("map legend 1",
      "1 Hormuz · 2 Seoul · 3 Jiuquan · 4 Samara · 5 Canberra · 35 Panay",
      SANS, 10, 452 - 20)
check("map legend 2",
      "6 Cartagena · 7 Bogor · 8 Hodeidah · 9 Gaza · 10 Sudan · "
      "11 London · 12 Dhaka", SANS, 10, 452 - 20)

# Pin collisions: map is drawn at (M+6, my+28) size (map_w-12)=440 x 228
map_w, map_h = 440, 228
pts = {}
for num, lon, lat in G.PINS:
    px = (lon + 180) / 360 * map_w
    py = (85 - lat) / 145 * map_h
    pts[num] = (px, py)
nums = sorted(pts)
for a in range(len(nums)):
    for b in range(a + 1, len(nums)):
        n1, n2 = nums[a], nums[b]
        dx = pts[n1][0] - pts[n2][0]
        dy = pts[n1][1] - pts[n2][1]
        dist = (dx * dx + dy * dy) ** 0.5
        if dist < 18:
            fails.append(f"pins {n1} & {n2} collide: {dist:.1f}px apart (< 18)")
        else:
            notes.append(f"pins {n1} & {n2}: {dist:.1f}px apart")

print(f"pins: {len(G.PINS)}, stories: {3 + len(G.GRID) + len(G.ALSO)}")
for n in notes:
    print("  ok", n)
if fails:
    print("FAILURES:")
    for f in fails:
        print("  FAIL", f)
    sys.exit(1)
print("AUDIT PASS: 0 overflow, 0 pin collisions")
