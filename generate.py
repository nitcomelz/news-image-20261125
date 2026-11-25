#!/usr/bin/env python3
"""Render entry.png for make.fun bounty news-image-20261125 (MERGED).

A one-page newspaper front page summarising the world news of
Wednesday 25 November 2026, drawn entirely with Pillow from facts
verified against live reporting on 25-26 Nov 2026 (see MERGE.md).

Merged leads: Hormuz tankers hit by mines (CLAIM, from B) + Kospi
plunges 6.2% (from A/C) + Shenzhou-24 carrying Pakistan's first
astronaut to Tiangong (from B). Structure: B's generator (best map,
numbered 1-12, 6-box KPI, label chips) + A's DATE CHECK thoroughness
+ C's HOW SURE legend. Contested facts reconciled by live web checks
in MERGE.md: gold $3,527 (not $3,505 / $3,545), Panay quake 5.1
(not 5.3), Bangladesh wage 17,000 taka (not 17,500), Russia toll
490,334 (BBC), Dell Q3 dropped as Tue 24 and replaced by Merz
(Wed, Reuters).

FIX (26 Nov, post strict-review): gold corrected to $3,505.30 /
down 1.6% (COMEX close Wed — the $3,527 was a morning snapshot;
coder B had it right); docking time corrected to 03:56 UTC;
11 ALSO items that were Tue/Mon/Fri news replaced with
Wednesday-verified stories (see FIX.md); tariffs 16 → 14;
pin 10 (Sudan) moved to Darfur so it no longer collides with pin 8.

Deterministic: no network, no clock, no randomness. The image is
pre-rendered by this script; main.py only copies it to /output/entry.png
(the copy pattern the bounty rules explicitly allow).

Run:  python3 generate.py   (writes entry.png next to this file)
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")
W, H = 1024, 1024

PAPER = (247, 243, 232)
INK = (20, 20, 20)
NAVY = (20, 38, 74)
NAVY2 = (28, 52, 96)
RED = (176, 42, 32)
GOLD = (201, 162, 39)
TEAL = (31, 110, 107)
SLATE = (90, 100, 112)
LIGHT = (233, 228, 214)
SKY = (178, 205, 224)
SEA = (46, 111, 143)
OCEAN = (186, 214, 228)
LAND = (226, 214, 178)
LANDB = (150, 138, 105)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, lines, fnt, fill, leading=None):
    if leading is None:
        leading = int(fnt.size * 1.22)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def rule(draw, x0, y, x1, color=INK, width=2):
    draw.line([(x0, y), (x1, y)], fill=color, width=width)


def star(draw, cx, cy, r_out, r_in, fill, points=5):
    pts = []
    for i in range(points * 2):
        ang = -math.pi / 2 + i * math.pi / points
        r = r_out if i % 2 == 0 else r_in
        pts.append((cx + r * math.cos(ang), cy + r * math.sin(ang)))
    draw.polygon(pts, fill=fill)


# ---------------------------------------------------------------- scenes
def scene_hormuz(draw, x, y, w, h):
    """Strait of Hormuz at dawn: tanker, mine blast at the stern, jets."""
    draw.rectangle([x, y, x + w, y + h], fill=(223, 232, 234))
    # sun glow + distant shore
    draw.ellipse([x + w * 0.72, y + h * 0.06, x + w * 0.88, y + h * 0.34],
                 fill=(245, 214, 150))
    draw.rectangle([x, y + h * 0.52, x + w, y + h * 0.60], fill=(198, 178, 138))
    draw.rectangle([x, y + h * 0.60, x + w, y + h], fill=(38, 96, 122))
    # tanker hull, centre-left
    draw.rectangle([x + w * 0.06, y + h * 0.62, x + w * 0.58, y + h * 0.78],
                   fill=(40, 40, 46))
    for i in range(4):
        draw.rectangle([x + w * (0.10 + i * 0.11), y + h * 0.52,
                        x + w * (0.18 + i * 0.11), y + h * 0.62],
                       fill=(176, 42, 32) if i % 2 == 0 else (20, 38, 74))
    draw.rectangle([x + w * 0.60, y + h * 0.44, x + w * 0.70, y + h * 0.62],
                   fill=(230, 230, 225))
    draw.rectangle([x + w * 0.62, y + h * 0.48, x + w * 0.68, y + h * 0.54],
                   fill=(38, 96, 122))
    # mine blast at the stern (right end of hull)
    bx, by = x + w * 0.82, y + h * 0.42
    pts = []
    for i in range(16):
        ang = i * math.pi / 8
        r = 30 if i % 2 == 0 else 12
        pts.append((bx + r * math.cos(ang), by + r * math.sin(ang)))
    draw.polygon(pts, fill=(255, 170, 40))
    draw.ellipse([bx - 11, by - 11, bx + 11, by + 11], fill=(255, 220, 120))
    # smoke column
    for cx, cy, r in [(0.80, 0.30, 12), (0.84, 0.22, 15), (0.78, 0.14, 10)]:
        draw.ellipse([x + w * cx - r, y + h * cy - r, x + w * cx + r,
                      y + h * cy + r], fill=(110, 110, 110))
    # two jets upper left
    for jx, jy in [(0.08, 0.14), (0.26, 0.08)]:
        px, py = x + w * jx, y + h * jy
        draw.polygon([(px, py), (px + 32, py + 8), (px, py + 13)], fill=(30, 30, 34))
        draw.polygon([(px + 10, py + 2), (px + 15, py - 9), (px + 19, py + 4)],
                     fill=(30, 30, 34))
        draw.line([px - 24, py + 6, px - 2, py + 6], fill=(255, 255, 255), width=3)
    # waves
    for wy in (0.70, 0.84, 0.94):
        for k in range(4):
            draw.arc([x + 6 + k * 46, y + h * wy, x + 38 + k * 46,
                      y + h * wy + 12], start=180, end=360,
                     fill=(220, 235, 240), width=3)


def scene_refinery(draw, x, y, w, h):
    """Night refinery in Samara: two towers, flames, smoke, drone."""
    draw.rectangle([x, y, x + w, y + h], fill=(16, 24, 46))
    for sx, sy in [(0.08, 0.12), (0.22, 0.06), (0.42, 0.14), (0.60, 0.07),
                   (0.78, 0.12), (0.90, 0.05), (0.95, 0.20)]:
        draw.ellipse([x + w * sx, y + h * sy, x + w * sx + 3, y + h * sy + 3],
                     fill=(255, 255, 255))
    # ground
    draw.rectangle([x, y + h * 0.82, x + w, y + h], fill=(24, 20, 18))
    # towers
    for tx in (0.16, 0.52):
        draw.rectangle([x + w * tx, y + h * 0.34, x + w * (tx + 0.10),
                        y + h * 0.82], fill=(70, 74, 80))
        draw.rectangle([x + w * (tx - 0.02), y + h * 0.30,
                        x + w * (tx + 0.12), y + h * 0.34], fill=(90, 94, 100))
        # pipes
        draw.line([x + w * (tx + 0.05), y + h * 0.34, x + w * (tx + 0.05),
                   y + h * 0.82], fill=(120, 124, 130), width=2)
    # storage tanks
    for tx in (0.30, 0.68):
        draw.ellipse([x + w * tx, y + h * 0.66, x + w * (tx + 0.14),
                      y + h * 0.82], fill=(96, 100, 106))
        draw.rectangle([x + w * tx, y + h * 0.72, x + w * (tx + 0.14),
                        y + h * 0.82], fill=(96, 100, 106))
    # flames on both towers
    for fx in (0.21, 0.57):
        cx, cy = x + w * fx, y + h * 0.26
        draw.polygon([(cx - 12, cy + 14), (cx - 4, cy - 6), (cx, cy - 20),
                      (cx + 5, cy - 4), (cx + 13, cy + 14)], fill=(255, 170, 40))
        draw.polygon([(cx - 6, cy + 12), (cx - 2, cy - 2), (cx + 2, cy - 10),
                      (cx + 4, cy - 2), (cx + 7, cy + 12)], fill=(255, 220, 120))
    # smoke columns
    for cx, cy, r in [(0.21, 0.10, 13), (0.24, 0.04, 16), (0.57, 0.08, 13),
                      (0.60, 0.02, 15)]:
        draw.ellipse([x + w * cx - r, y + h * cy - r, x + w * cx + r,
                      y + h * cy + r], fill=(90, 90, 96))
    # small drone, upper right
    px, py = x + w * 0.84, y + h * 0.16
    draw.ellipse([px - 8, py - 3, px + 8, py + 3], fill=(200, 200, 205))
    draw.line([px - 16, py - 6, px + 16, py - 6], fill=(200, 200, 205), width=2)
    draw.line([px - 16, py + 6, px + 16, py + 6], fill=(200, 200, 205), width=2)


def scene_space(draw, x, y, w, h):
    """Tiangong station above the Earth, Shenzhou capsule docking."""
    draw.rectangle([x, y, x + w, y + h], fill=(8, 10, 24))
    for sx, sy in [(0.06, 0.10), (0.18, 0.05), (0.30, 0.14), (0.44, 0.06),
                   (0.58, 0.12), (0.70, 0.05), (0.84, 0.11), (0.94, 0.06),
                   (0.12, 0.26), (0.52, 0.24), (0.90, 0.26)]:
        draw.ellipse([x + w * sx, y + h * sy, x + w * sx + 3, y + h * sy + 3],
                     fill=(255, 255, 255))
    # Earth arc at the bottom
    draw.ellipse([x - w * 0.25, y + h * 0.78, x + w * 1.25, y + h * 1.75],
                 fill=(46, 111, 180))
    draw.ellipse([x - w * 0.25, y + h * 0.78, x + w * 1.25, y + h * 1.75],
                 outline=(220, 235, 245), width=2)
    for cx, cy, rw in [(0.22, 0.86, 46), (0.55, 0.92, 60), (0.82, 0.88, 40)]:
        draw.ellipse([x + w * cx - rw, y + h * cy - 7, x + w * cx + rw,
                      y + h * cy + 7], fill=(235, 242, 248))
    # station: core module + solar panels
    draw.rectangle([x + w * 0.34, y + h * 0.34, x + w * 0.62, y + h * 0.50],
                   fill=(225, 228, 232))
    draw.rectangle([x + w * 0.34, y + h * 0.34, x + w * 0.62, y + h * 0.50],
                   outline=(120, 124, 130), width=2)
    for px in (0.06, 0.66):
        draw.rectangle([x + w * px, y + h * 0.38, x + w * (px + 0.26),
                        y + h * 0.46], fill=(28, 68, 160))
        draw.line([x + w * (px + 0.13), y + h * 0.38, x + w * (px + 0.13),
                   y + h * 0.46], fill=(90, 130, 210), width=2)
    # docking capsule approaching from the right
    draw.ellipse([x + w * 0.70, y + h * 0.36, x + w * 0.80, y + h * 0.48],
                 fill=(240, 240, 238))
    draw.rectangle([x + w * 0.66, y + h * 0.40, x + w * 0.71, y + h * 0.44],
                   fill=(176, 42, 32))
    # small flags on the core module: China red, Pakistan green
    draw.rectangle([x + w * 0.40, y + h * 0.37, x + w * 0.46, y + h * 0.42],
                   fill=(222, 41, 16))
    star(draw, x + w * 0.43, y + h * 0.395, 4, 2, (255, 222, 0))
    draw.rectangle([x + w * 0.50, y + h * 0.37, x + w * 0.56, y + h * 0.42],
                   fill=(20, 120, 70))
    draw.ellipse([x + w * 0.515, y + h * 0.378, x + w * 0.535, y + h * 0.412],
                 fill=(255, 255, 255))
    draw.ellipse([x + w * 0.522, y + h * 0.378, x + w * 0.542, y + h * 0.412],
                 fill=(20, 120, 70))


def scene_kospi(draw, x, y, w, h):
    """Kospi plunges: dark market board, big -6.2%, falling chart."""
    draw.rectangle([x, y, x + w, y + h], fill=NAVY)
    f_small = font(SANS_B, 10)
    draw.text((x + 10, y + 6), "SK HYNIX  -11.1%", font=f_small,
              fill=(255, 255, 255))
    draw.text((x + 10, y + 20), "SAMSUNG  -9.9%", font=f_small,
              fill=(255, 255, 255))
    draw.text((x + w - 118, y + 28), "-6.2%", font=font(SANS_B, 34),
              fill=(255, 90, 60))
    pts = [(x + 12, y + 52), (x + w * 0.22, y + 46), (x + w * 0.38, y + 56),
           (x + w * 0.55, y + 50), (x + w * 0.70, y + 62),
           (x + w * 0.85, y + 74), (x + w - 14, y + 80)]
    draw.line(pts, fill=(255, 90, 60), width=3)
    for px, py in pts:
        draw.ellipse([px - 3, py - 3, px + 3, py + 3], fill=(255, 220, 120))
    draw.polygon([(x + w - 14, y + 80), (x + w - 26, y + 74),
                  (x + w - 26, y + 86)], fill=(255, 90, 60))
    draw.text((x + 10, y + h - 18), "KOSPI  ·  SEOUL", font=f_small,
              fill=(255, 255, 255))


# ---------------------------------------------------------------- pictograms
def pic_chart(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    for i, bh in enumerate((0.30, 0.45, 0.38, 0.60)):
        bx = x + 8 + i * 13
        draw.rectangle([bx, y + h - 10 - bh * (h - 18), bx + 9, y + h - 10],
                       fill=(31, 110, 107) if i < 2 else (176, 42, 32))
    draw.line([(x + 6, y + 14), (x + 22, y + 26), (x + 36, y + 20),
               (x + 54, y + 44)], fill=(176, 42, 32), width=3)
    draw.polygon([(x + 54, y + 44), (x + 46, y + 42), (x + 54, y + 52)],
                 fill=(176, 42, 32))


def pic_island(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(178, 205, 224))
    draw.ellipse([x + w * 0.68, y + 6, x + w * 0.68 + 14, y + 20],
                 fill=(245, 214, 150))
    draw.rectangle([x, y + h * 0.62, x + w, y + h], fill=(46, 111, 143))
    draw.polygon([(x + 8, y + h * 0.62), (x + w * 0.42, y + h * 0.38),
                  (x + w * 0.78, y + h * 0.62)], fill=(90, 160, 90))
    draw.line([x + w * 0.42, y + h * 0.38, x + w * 0.42, y + h * 0.22],
              fill=(120, 84, 50), width=3)
    draw.line([x + w * 0.42, y + h * 0.22, x + w * 0.26, y + h * 0.12],
              fill=(60, 140, 70), width=3)
    draw.line([x + w * 0.42, y + h * 0.22, x + w * 0.58, y + h * 0.12],
              fill=(60, 140, 70), width=3)


def pic_shield(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(20, 38, 74))
    cx = x + w / 2
    draw.polygon([(cx - 18, y + 10), (cx + 18, y + 10), (cx + 18, y + 32),
                  (cx, y + 52), (cx - 18, y + 32)], fill=(245, 243, 232))
    draw.line([cx - 9, y + 30, cx - 2, y + 38], fill=(176, 42, 32), width=3)
    draw.line([cx - 2, y + 38, cx + 11, y + 20], fill=(176, 42, 32), width=3)


def pic_mine(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(60, 48, 38))
    draw.ellipse([x + 8, y + 12, x + w - 8, y + h - 6], fill=(20, 16, 14))
    draw.rectangle([x + 8, y + h * 0.55, x + w - 8, y + h - 6], fill=(20, 16, 14))
    for wy in (0.68, 0.80, 0.92):
        for k in range(3):
            draw.arc([x + 8 + k * 18, y + h * wy, x + 26 + k * 18,
                      y + h * wy + 8], start=180, end=360,
                     fill=(120, 190, 230), width=2)
    draw.ellipse([x + w * 0.44, y + 6, x + w * 0.44 + 8, y + 14],
                 fill=(255, 220, 120))


def pic_ship(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(214, 226, 228))
    draw.rectangle([x, y + h * 0.60, x + w, y + h], fill=(46, 111, 143))
    draw.polygon([(x + 8, y + h * 0.62), (x + w - 8, y + h * 0.62),
                  (x + w - 16, y + h * 0.78), (x + 16, y + h * 0.78)],
                 fill=(40, 40, 46))
    draw.rectangle([x + 14, y + h * 0.44, x + 26, y + h * 0.62], fill=(176, 42, 32))
    draw.rectangle([x + 28, y + h * 0.44, x + 40, y + h * 0.62], fill=(20, 38, 74))
    draw.polygon([(x + 34, y + h * 0.36), (x + 30, y + h * 0.24),
                  (x + 34, y + h * 0.14), (x + 38, y + h * 0.24),
                  (x + 42, y + h * 0.36)], fill=(255, 170, 40))


def pic_smoke(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(233, 228, 214))
    draw.rectangle([x + 10, y + h * 0.42, x + 26, y + h - 6], fill=(90, 90, 96))
    draw.rectangle([x + 30, y + h * 0.54, x + 50, y + h - 6], fill=(120, 120, 126))
    for cx, cy, r in [(0.30, 0.30, 8), (0.38, 0.20, 10), (0.48, 0.28, 7)]:
        draw.ellipse([x + w * cx - r, y + h * cy - r, x + w * cx + r,
                      y + h * cy + r], fill=(110, 110, 110))


def pic_drone(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(20, 38, 74))
    cx, cy = x + w / 2, y + h / 2
    draw.ellipse([cx - 9, cy - 5, cx + 9, cy + 5], fill=(220, 220, 225))
    for dx, dy in [(-18, -12), (18, -12), (-18, 12), (18, 12)]:
        draw.line([cx, cy, cx + dx, cy + dy], fill=(160, 160, 165), width=2)
        draw.ellipse([cx + dx - 5, cy + dy - 2, cx + dx + 5, cy + dy + 2],
                     fill=(220, 220, 225))
    draw.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=(176, 42, 32))


def pic_bolt(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(20, 38, 74))
    cx = x + w / 2
    draw.polygon([(cx + 6, y + 8), (cx - 10, y + 34), (cx - 1, y + 34),
                  (cx - 6, y + 54), (cx + 12, y + 28), (cx + 2, y + 28)],
                 fill=(255, 214, 80))
    f = font(SANS_B, 15)
    draw.text((x + 8, y + h - 20), "£", font=f, fill=(255, 255, 255))


def pic_factory(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(233, 228, 214))
    draw.rectangle([x + 10, y + h * 0.48, x + w - 10, y + h - 6], fill=(90, 94, 100))
    draw.polygon([(x + 10, y + h * 0.48), (x + 18, y + h * 0.34),
                  (x + 26, y + h * 0.48), (x + 34, y + h * 0.34),
                  (x + 42, y + h * 0.48), (x + 50, y + h * 0.34),
                  (x + w - 10, y + h * 0.48)], fill=(70, 74, 80))
    draw.rectangle([x + w - 18, y + 10, x + w - 12, y + h * 0.48], fill=(70, 74, 80))
    draw.ellipse([x + w - 20, y + 4, x + w - 10, y + 14], fill=(150, 150, 155))
    draw.rectangle([x + 16, y + h * 0.62, x + 24, y + h * 0.74], fill=(255, 220, 120))
    draw.rectangle([x + 30, y + h * 0.62, x + 38, y + h * 0.74], fill=(255, 220, 120))


def pic_refinery(draw, x, y, w, h):
    """Mini night refinery: two towers, flames, small drone (from B's lead scene)."""
    draw.rectangle([x, y, x + w, y + h], fill=(16, 24, 46))
    draw.rectangle([x + 8, y + h * 0.30, x + 18, y + h - 6], fill=(70, 74, 80))
    draw.rectangle([x + 34, y + h * 0.42, x + 44, y + h - 6], fill=(70, 74, 80))
    draw.ellipse([x + 46, y + h * 0.62, x + w - 6, y + h - 6],
                 fill=(96, 100, 106))
    for fx, fy in [(13, 0.24), (39, 0.36)]:
        draw.polygon([(x + fx - 6, y + h * fy + 12), (x + fx - 2, y + h * fy - 2),
                      (x + fx + 2, y + h * fy - 8), (x + fx + 6, y + h * fy + 12)],
                     fill=(255, 170, 40))
    draw.ellipse([x + w - 14, y + 6, x + w - 6, y + 14], fill=(200, 200, 205))


PICS = {"chart": pic_chart, "island": pic_island, "shield": pic_shield,
        "mine": pic_mine, "ship": pic_ship, "smoke": pic_smoke,
        "drone": pic_drone, "bolt": pic_bolt, "factory": pic_factory,
        "refinery": pic_refinery}

# ---------------------------------------------------------------- world map
NA = [(-168, 66), (-150, 70), (-135, 69), (-125, 71), (-110, 68), (-95, 80),
      (-85, 76), (-75, 72), (-65, 60), (-55, 52), (-60, 46), (-65, 44),
      (-70, 42), (-75, 36), (-76, 34), (-80, 26), (-81, 25), (-87, 21),
      (-90, 21), (-94, 18), (-97, 16), (-92, 15), (-86, 13), (-83, 9),
      (-79, 9), (-83, 16), (-90, 21), (-97, 26), (-103, 23), (-108, 25),
      (-114, 29), (-120, 34), (-124, 40), (-124, 48), (-130, 55), (-140, 60),
      (-155, 58), (-162, 55), (-168, 66)]
SA = [(-79, 9), (-77, 4), (-80, -3), (-81, -6), (-77, -12), (-72, -18),
      (-70, -23), (-70, -30), (-72, -37), (-73, -44), (-71, -50), (-68, -55),
      (-65, -48), (-62, -41), (-58, -34), (-52, -32), (-48, -27), (-41, -23),
      (-39, -17), (-35, -8), (-35, -6), (-40, -3), (-44, -2), (-50, 0),
      (-53, 4), (-58, 6), (-62, 9), (-68, 11), (-72, 12), (-76, 10), (-79, 9)]
AF = [(-17, 15), (-16, 21), (-10, 29), (-6, 33), (0, 36), (10, 37), (11, 34),
      (20, 32), (25, 32), (30, 31), (33, 27), (35, 23), (37, 18), (39, 15),
      (43, 11), (48, 11), (51, 10), (48, 4), (44, -2), (40, -10), (36, -18),
      (33, -26), (28, -33), (20, -35), (17, -32), (14, -22), (12, -15),
      (13, -8), (12, -4), (9, 4), (4, 6), (-8, 5), (-13, 8), (-17, 12),
      (-17, 15)]
EU = [(-10, 36), (-9, 38), (-9, 43), (-2, 44), (-2, 48), (-4, 50), (0, 51),
      (3, 53), (5, 58), (8, 57), (10, 59), (13, 56), (18, 56), (21, 55),
      (24, 58), (24, 60), (28, 62), (25, 65), (22, 69), (18, 70), (14, 67),
      (12, 62), (6, 58), (5, 60), (0, 58), (-3, 54), (-5, 50), (-8, 48),
      (-9, 43), (-10, 36)]
AS = [(28, 62), (32, 68), (40, 67), (45, 68), (52, 69), (60, 69), (68, 70),
      (75, 72), (85, 74), (95, 76), (105, 77), (115, 73), (125, 71),
      (135, 71), (145, 72), (155, 70), (162, 68), (170, 67), (178, 65),
      (170, 60), (162, 56), (158, 52), (150, 59), (142, 52), (141, 45),
      (138, 38), (132, 33), (127, 35), (122, 32), (120, 28), (115, 23),
      (110, 20), (108, 15), (105, 10), (103, 8), (100, 7), (98, 10),
      (95, 15), (92, 21), (88, 22), (85, 19), (80, 15), (77, 8), (76, 10),
      (73, 16), (70, 20), (66, 25), (61, 25), (57, 26), (53, 27), (50, 29),
      (48, 30), (44, 29), (42, 25), (40, 20), (39, 16), (43, 12), (45, 12),
      (50, 15), (55, 17), (59, 22), (58, 25), (56, 27), (52, 28), (48, 29),
      (44, 31), (40, 35), (36, 36), (33, 38), (30, 36), (28, 62)]
AU = [(114, -22), (113, -26), (115, -32), (118, -35), (124, -33), (130, -32),
      (135, -35), (138, -35), (142, -38), (146, -39), (150, -37), (153, -32),
      (153, -27), (151, -24), (146, -19), (142, -11), (141, -13), (136, -12),
      (132, -12), (127, -14), (122, -17), (118, -20), (114, -22)]
NZ = [(167, -45), (170, -43), (173, -41), (175, -38), (177, -38), (174, -41),
      (172, -43), (168, -46), (167, -45)]
CONTINENTS = [NA, SA, AF, EU, AS, AU, NZ]

# (story number, longitude, latitude)
PINS = [(1, 56.5, 26.5), (2, 127.0, 37.5), (3, 100.3, 40.0), (4, 50.2, 53.2),
        (5, 149.1, -35.3), (6, -75.5, 10.4), (7, 106.8, -6.6),
        (8, 42.9, 14.8), (9, 34.5, 31.5), (10, 24.5, 13.5),
        (11, -0.1, 51.5), (12, 90.4, 23.8), (35, 122.5, 11.2)]


def draw_map(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=OCEAN)
    for poly in CONTINENTS:
        pts = [(x + (lon + 180) / 360 * w, y + (85 - lat) / 145 * h)
               for lon, lat in poly]
        draw.polygon(pts, fill=LAND, outline=LANDB)
    f_pin = font(SANS_B, 10)
    for num, lon, lat in PINS:
        px = x + (lon + 180) / 360 * w
        py = y + (85 - lat) / 145 * h
        r = 9
        draw.ellipse([px - r, py - r, px + r, py + r], fill=RED,
                     outline=(255, 255, 255), width=1)
        label = str(num)
        lw = draw.textlength(label, font=f_pin)
        draw.text((px - lw / 2, py - 7), label, font=f_pin,
                  fill=(255, 255, 255))


# ---------------------------------------------------------------- stories
LEADS = [
    ("MIDDLE EAST · STRAIT OF HORMUZ",
     "Two tankers burn after mine strikes",
     "Iran's Guard says two tankers hit naval mines and caught fire "
     "Wednesday, on an 'unauthorised route'. No independent confirmation.",
     "CLAIM · IRGC via Reuters", "hormuz"),
    ("MARKETS · SEOUL",
     "Kospi plunges 6.2% as AI rout sweeps Asia",
     "SK Hynix −11.1% and Samsung −9.9%; Nikkei −2.78%. Wall Street: "
     "Nasdaq −1.5%, S&P 500 −0.5%.",
     "REPORTED · Reuters · AP", "kospi"),
    ("SPACE · TIANGONG STATION",
     "Pakistan's first astronaut reaches orbit",
     "Shenzhou-24 docked with Tiangong, carrying Muhammad Zeeshan Ali, "
     "40 — first Pakistani in space, first foreigner on China's station.",
     "OFFICIAL · Xinhua / CMSA", "space"),
]

GRID = [
    ("UKRAINE · SAMARA", "Two Russian refineries ablaze",
     "Ukrainian drones hit Rosneft's Syzran and Kuibyshev plants; one "
     "killed.",
     "REPORTED · Kyiv Ind.", "refinery"),
    ("PACIFIC · CANBERRA", "Canberra bars foreign bases",
     "A$740m over 10 years; the treaty bars any foreign military base on "
     "the islands.",
     "OFFICIAL · AP", "island"),
    ("AMERICAS · CARTAGENA", "Hostages freed in dawn raid",
     "Forces stormed an Éxito supermarket; every hostage freed, one "
     "captor killed.",
     "REPORTED · AP", "shield"),
    ("ASIA · BOGOR", "Six dead in flooded gold mine",
     "Three more bodies found Wednesday; toll is six, ~20 miners still "
     "trapped.",
     "REPORTED · AP", "mine"),
    ("MIDEAST · RED SEA", "Houthis claim refinery hit",
     "Houthis claim a strike on Ras Tanura refinery; coalition hits "
     "Hodeidah port.",
     "CLAIM · Reuters", "ship"),
    ("MIDEAST · GAZA", "Hamas security chief killed",
     "Israel kills Hamas colonel Abuelouf, who headed interior security, "
     "with his family.",
     "REPORTED · AP", "smoke"),
    ("AFRICA · SUDAN", "RSF drones kill 19 civilians",
     "RSF drone strikes kill 19 civilians and wound 20 in two cities, "
     "monitors say.",
     "REPORTED · Reuters", "drone"),
    ("EUROPE · LONDON", "UK bills jump 26% in January",
     "Cap rises to £2,166 a year for a typical home — up £443.",
     "OFFICIAL · Reuters", "bolt"),
    ("ASIA · DHAKA", "Garment wage up 36%",
     "Minimum wage rises to 17,000 taka ($139) from 12,500.",
     "OFFICIAL · Reuters", "factory"),
]

# (number, beat, one-line story, outlet)
ALSO = [
    (13, "COP31", "Pope voices concern as climate talks fail", "AP"),
    (14, "UKRAINE AID", "Kyiv needs €115bn aid; US pauses Patriots", "Reuters"),
    (15, "INFLATION", "Eurozone 4.0%; Australia CPI 4.9%", "Eurostat"),
    (16, "AUSTRALIA", "Canberra says sorry to LGBTQ veterans", "Reuters"),
    (17, "TARIFFS", "Trump proposes tariffs on 14 economies", "Reuters"),
    (18, "GOLD", "Slides to $3,505/oz, down 1.6% on the day", "COMEX"),
    (19, "RUSSIA TOLL", "Leak: 490,334 Russian soldiers dead", "BBC"),
    (20, "ODESA & KYIV", "Overnight strikes kill 2 in Odesa; Kyiv flat hit", "Kyiv Ind."),
    (21, "N. KOREA", "Pyongyang expels Swiss envoy, shuts office", "Reuters"),
    (22, "LIBYA", "Two officers die of wounds from Sunday's sea-drone attack", "LNA"),
    (23, "MERZ", "Merz: Russia 'wants more than Ukraine', is escalating", "Reuters"),
    (24, "NVIDIA", "Falls again, −5% in premarket trade", "Reuters"),
    (25, "ANTHROPIC", "Slips further in premarket, near $78", "TipRanks"),
    (26, "ANKARA", "Haftar meets Turkish ministers on first visit", "Anadolu"),
    (27, "MISSISSIPPI", "Six found dead in plane off Horn Island", "USCG"),
    (28, "BOSNIA", "Statehood Day marked amid EU talks", "OpenChronicle"),
    (29, "EASYJET", "Profit falls 89% as fuel costs soar; £244m hit", "easyJet"),
    (30, "EU TECH", "Brussels unveils €50bn fund for AI and quantum", "FT"),
    (31, "KOREA", "Moscow defends Tu-160 flight as planned", "AJP"),
    (32, "IRAN", "Aref: Tehran unfazed by US blockade", "Reuters"),
    (33, "DR CONGO", "War spreads in South Kivu; 8.2m displaced", "Echo Harbor"),
    (34, "SUDAN", "Khartoum rejects Ethiopia as talks host", "Sudan Now"),
    (35, "PANAY QUAKE", "Magnitude 5.1 jolts Antique at 7:29 AM", "PHIVOLCS"),
    (36, "US ECONOMY", "US Q3 GDP revised up to 4.3%, fastest in 3 years", "BEA"),
]

KPIS = ["KOSPI −6.2%", "NIKKEI −2.78%", "DOW 50,018.70",
        "GOLD $3,505", "SUDAN: 19 KILLED", "BOGOR: 6 DEAD"]

TIMELINE = [
    ("03:56 UTC", "Shenzhou-24 docks with Tiangong"),
    ("OVERNIGHT", "Drones hit two Samara refineries"),
    ("MORNING", "Tankers burn in Hormuz · UK cap +26%"),
    ("MIDDAY", "Bangladesh wage +36% · Australia apologises"),
    ("AFTERNOON", "Solomons treaty · EU €50bn fund"),
    ("CLOSE", "Kospi −6.2% · Dow above 50,000"),
]

DATE_CHECK = ("DATE CHECK — LEFT OUT, NOT WEDNESDAY: Huawei convicted "
              "(Tue 24) · Riyadh tower drone (Tue 24) · Abrego Garcia to "
              "Spain (Tue 24) · WHO Akwe evacuation (Tue 24) · Senegal "
              "AFCON title (Tue 24) · Huang back at Nvidia (Mon 23) · "
              "COP31 collapse (Sun 22) · England heat toll (Tue 24) · "
              "Dell Q3 record (Tue 24) · CIA–ODNI breach: date disputed.")

FOOTER = ("Sources: Reuters · AP · AFP · Kyiv Independent · Xinhua · "
          "Eurostat · Ofgem · PHIVOLCS · BBC · FT · UN · Drawings original · "
          "36 stories · 9 regions · One image, one day.")

SCENES = {"hormuz": scene_hormuz, "refinery": scene_refinery,
          "space": scene_space, "kospi": scene_kospi}


# ---------------------------------------------------------------- page
def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 30
    R = W - M

    # ---- masthead
    d.rectangle([M, 14, R, 100], fill=NAVY)
    d.rectangle([M, 14, R, 22], fill=RED)
    f_title = font(SERIF_B, 52)
    title = "THE WORLD IN ONE DAY"
    tw = d.textlength(title, font=f_title)
    d.text(((W - tw) / 2, 26), title, font=f_title, fill=(255, 255, 255))
    f_sub = font(SANS_B, 16)
    sub = ("WEDNESDAY, 25 NOVEMBER 2026  ·  36 STORIES  ·  9 REGIONS  ·  "
           "EVERY ONE FIRST REPORTED TODAY")
    sw = d.textlength(sub, font=f_sub)
    d.text(((W - sw) / 2, 80), sub, font=f_sub, fill=GOLD)

    # ---- KPI strip
    ky = 108
    kw = (R - M - 5 * 6) // 6
    f_kpi = font(SANS_B, 12)
    for i, kpi in enumerate(KPIS):
        kx = M + i * (kw + 6)
        d.rectangle([kx, ky, kx + kw, ky + 28], fill=(255, 255, 255),
                    outline=INK, width=1)
        lw = d.textlength(kpi, font=f_kpi)
        d.text((kx + (kw - lw) / 2, ky + 6), kpi, font=f_kpi,
               fill=RED if i in (0, 1, 4, 5) else NAVY)

    # ---- 3 leads
    ly, lh = 144, 214
    cw = (R - M - 2 * 14) // 3
    for i, (kick, head, deck, tag, scene) in enumerate(LEADS):
        cx = M + i * (cw + 14)
        d.rectangle([cx, ly, cx + cw, ly + lh], fill=(255, 255, 255),
                    outline=INK, width=2)
        tmp = Image.new("RGB", (cw - 4, 88), PAPER)
        td = ImageDraw.Draw(tmp)
        SCENES[scene](td, 0, 0, cw - 4, 88)
        img.paste(tmp, (cx + 2, ly + 2))
        d.line([cx, ly + 90, cx + cw, ly + 90], fill=INK, width=2)
        tx = cx + 10
        tw_ = cx + cw - 10 - tx
        d.text((tx, ly + 96), f"{i + 1} · {kick}", font=font(SANS_B, 11),
               fill=RED)
        y = text_block(d, tx, ly + 112,
                       wrap(d, head, font(SERIF_B, 18), tw_)[:2],
                       font(SERIF_B, 18), INK, leading=20)
        text_block(d, tx, y + 2,
                   wrap(d, deck, font(SERIF, 11), tw_)[:3],
                   font(SERIF, 11), INK, leading=14)
        d.text((tx, ly + lh - 14), tag, font=font(SANS_B, 9), fill=SLATE)

    # ---- grid stories 4-12 (3 x 3)
    gy = 366
    gw, gh = (R - M - 2 * 12) // 3, 72
    chip_fill = {"REPORTED": RED, "OFFICIAL": NAVY, "CLAIM": GOLD}
    for i, (kick, head, deck, tag, pic) in enumerate(GRID):
        cx = M + (i % 3) * (gw + 12)
        cy = gy + (i // 3) * (gh + 6)
        d.rectangle([cx, cy, cx + gw, cy + gh], fill=(255, 255, 255),
                    outline=INK, width=1)
        PICS[pic](d, cx + 2, cy + 2, 58, gh - 4)
        d.line([cx + 60, cy, cx + 60, cy + gh], fill=INK, width=1)
        tx = cx + 68
        tw_ = cx + gw - 8 - tx
        label = tag.split(" · ")[0]
        f_chip = font(SANS_B, 8)
        chip_w = int(d.textlength(tag, font=f_chip)) + 10
        d.rectangle([cx + gw - 6 - chip_w, cy + 4, cx + gw - 6, cy + 17],
                    fill=chip_fill[label])
        d.text((cx + gw - 6 - chip_w + 5, cy + 5), tag, font=f_chip,
               fill=INK if label == "CLAIM" else (255, 255, 255))
        d.text((tx, cy + 4), f"{i + 4} · {kick}", font=font(SANS_B, 10),
               fill=RED)
        text_block(d, tx, cy + 18,
                   wrap(d, head, font(SERIF_B, 14), tw_)[:2],
                   font(SERIF_B, 14), INK, leading=16)
        text_block(d, tx, cy + 36,
                   wrap(d, deck, font(SERIF, 11), tw_)[:2],
                   font(SERIF, 11), INK, leading=13)

    # ---- map + ALSO list
    my = 602
    map_w, map_h = 452, 240
    d.rectangle([M, my, M + map_w, my + 330], fill=(255, 255, 255),
                outline=INK, width=1)
    d.text((M + 10, my + 6), "WHERE IT HAPPENED — PINS = STORY NUMBERS",
           font=font(SANS_B, 12), fill=NAVY)
    draw_map(d, M + 6, my + 28, map_w - 12, 228)
    d.text((M + 10, my + 262),
           "1 Hormuz · 2 Seoul · 3 Jiuquan · 4 Samara · 5 Canberra · 35 Panay",
           font=font(SANS, 10), fill=SLATE)
    d.text((M + 10, my + 276),
           "6 Cartagena · 7 Bogor · 8 Hodeidah · 9 Gaza · 10 Sudan · "
           "11 London · 12 Dhaka",
           font=font(SANS, 10), fill=SLATE)
    d.text((M + 10, my + 294),
           "HOW SURE: REPORTED — confirmed by outlets · OFFICIAL — "
           "governments",
           font=font(SANS, 9), fill=SLATE)
    d.text((M + 10, my + 307),
           "CLAIM — one side's claim, not confirmed · Pins = story numbers",
           font=font(SANS, 9), fill=SLATE)

    ax = M + map_w + 16
    aw = R - ax
    d.text((ax, my), "ALSO ON WEDNESDAY 25 NOVEMBER",
           font=font(SANS_B, 13), fill=NAVY)
    rule(d, ax, my + 20, R, color=RED, width=2)
    col_w = (aw - 14) // 2
    f_num = font(SANS_B, 11)
    f_txt = font(SERIF, 11)
    for j, (num, beat, text, outlet) in enumerate(ALSO):
        col = j // 12
        row = j % 12
        ix = ax + col * (col_w + 14)
        iy = my + 28 + row * 25
        d.text((ix, iy), f"{num}", font=f_num, fill=RED)
        lines = wrap(d, f"{beat} — {text} ({outlet})", f_txt, col_w - 22)
        text_block(d, ix + 20, iy, lines[:2], f_txt, INK, leading=13)

    # ---- timeline
    ty = 936
    d.rectangle([M, ty, R, ty + 32], fill=NAVY)
    f_tl = font(SANS_B, 10)
    line1 = "  ·  ".join(f"{t} — {s}" for t, s in TIMELINE[:3])
    line2 = "  ·  ".join(f"{t} — {s}" for t, s in TIMELINE[3:])
    d.text((M + 8, ty + 4), line1, font=f_tl, fill=(255, 255, 255))
    d.text((M + 8, ty + 18), line2, font=f_tl, fill=(255, 255, 255))

    # ---- date check
    f_dc = font(SANS, 10)
    text_block(d, M, 974, wrap(d, DATE_CHECK, f_dc, R - M), f_dc, RED,
               leading=13)

    # ---- footer
    f_f = font(SANS, 11)
    fw = d.textlength(FOOTER, font=f_f)
    d.text(((W - fw) / 2, 1006), FOOTER, font=f_f, fill=SLATE)

    img.save(OUT, format="PNG", optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
