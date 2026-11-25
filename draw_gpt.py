#!/usr/bin/env python3
"""Render the news-image-20261124 final image per the GPT-6.2 layout spec
(gpt-layout-spec.md). Deterministic PIL rendering: every coordinate, string,
size and colour below is copied verbatim from the spec. Nothing is invented.

Fonts: real Inter TTF files (InterDisplay-Bold, Inter-Bold, Inter-Medium),
downloaded once at build time to /tmp/inter; the shipped entry needs no
network and no fonts at all (main.ts just copies entry.png).
"""
import hashlib
import os
from PIL import Image, ImageDraw, ImageFont

ENTRY_DIR = "/home/hatch/workspace/makefun/news-image-entry"
FONT_DIR = "/tmp/inter/extras/ttf"
OUT = os.path.join(ENTRY_DIR, "entry-gpt.png")

W, H = 1024, 1024

# ---- palette (spec) ----
IVORY = (245, 242, 235)   # #F5F2EB canvas
NAVY = (23, 38, 49)       # #172631 main type + lead background
SLATE = (64, 80, 91)      # #40505B secondary summaries
BRONZE = (145, 96, 45)    # #91602D category labels + secondary accents
GOLD = (213, 172, 112)    # #D5AC70 lead label + lead accent
WHITE = (255, 255, 255)   # #FFFFFF lead headline
SOFT = (233, 237, 240)    # #E9EDF0 lead summary
WARM = (208, 204, 195)    # #D0CCC3 dividers

# ---- fonts (spec: real Inter files) ----
def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)

F_TITLE = font("InterDisplay-Bold.ttf", 50)   # main title
F_DAY = font("Inter-Bold.ttf", 28)            # day
F_LEAD_CAT = font("Inter-Bold.ttf", 27)       # lead category
F_LEAD_HEAD = font("InterDisplay-Bold.ttf", 52)  # lead headline
F_LEAD_SUM = font("Inter-Medium.ttf", 32)     # lead summary
F_HEAD = font("Inter-Bold.ttf", 36)           # secondary headlines
F_SUM = font("Inter-Medium.ttf", 32)          # secondary summaries
F_CAT = font("Inter-Bold.ttf", 24)            # secondary categories

# ---- copy (spec, verbatim — do not change a word, number or date) ----
DAY = "TUESDAY"
TITLE = "World News \u2014 24 November 2026"
LEAD_LABEL = "TOP STORY / MIDDLE EAST"
LEAD_HEAD = "Iran says 4 oil tankers hit mines"
LEAD_SUM = "Tankers caught fire in the Strait of Hormuz, Iran says."
STORIES = [
    ("LAW", "US jury convicts Huawei",
     "Guilty on 10 of 12 counts; acquitted on racketeering."),
    ("SPORT", "CAS restores Senegal's title",
     "Senegal reinstated as Africa Cup of Nations champions."),
    ("SECURITY", "25 hostages in Cartagena",
     "Gunman takes hostages at a supermarket."),
    ("LABOUR", "Bangladesh garment workers protest",
     "Workers demand higher pay and clash with police."),
    ("BUSINESS", "Sanofi to buy Insmed for $40bn",
     "Sanofi to acquire US biotech Insmed."),
    ("SCIENCE", "Euclid finds most distant quasar",
     "630 million years after the Big Bang; redshift 8.13."),
]
BLOCK_Y = [348, 452, 556, 660, 764, 868]

img = Image.new("RGB", (W, H), IVORY)
d = ImageDraw.Draw(img)


def draw_tracked(x, baseline_y, text, f, tracking, fill):
    """Draw text with explicit letter-spacing (spec: Day tracking +2 px)."""
    cx = x
    for ch in text:
        d.text((cx, baseline_y), ch, font=f, fill=fill, anchor="ls")
        cx += d.textlength(ch, font=f) + tracking
    return cx - tracking


def check(name, value, limit):
    status = "OK " if value <= limit else "FAIL"
    print(f"  [{status}] {name}: {value:.1f} px (limit {limit})")
    assert value <= limit, f"{name} {value} exceeds {limit}"


print("== measurements (must all fit on one line) ==")
check("title width", d.textlength(TITLE, font=F_TITLE), 928)
check("lead label width", d.textlength(LEAD_LABEL, font=F_LEAD_CAT), 880)
check("lead headline width", d.textlength(LEAD_HEAD, font=F_LEAD_HEAD), 880)
check("lead summary width", d.textlength(LEAD_SUM, font=F_LEAD_SUM), 880)
for i, (cat, head, summ) in enumerate(STORIES, start=2):
    hw = d.textlength(head, font=F_HEAD)
    cw = d.textlength(cat, font=F_CAT)
    sw = d.textlength(summ, font=F_SUM)
    check(f"story {i} summary width", sw, 888)
    check(f"story {i} headline+16+category", hw + 16 + cw, 888)

# ---- header (X 48, Y 32, W 928, H 106) ----
draw_tracked(48, 54, DAY, F_DAY, 2, NAVY)
d.text((48, 113), TITLE, font=F_TITLE, fill=NAVY, anchor="ls")
d.rectangle([48, 135, 48 + 928, 135 + 3], fill=NAVY)

# ---- lead story (X 48, Y 148, W 928, H 188) ----
d.rectangle([48, 148, 48 + 928, 148 + 188], fill=NAVY)
d.rectangle([48, 148, 48 + 6, 148 + 188], fill=GOLD)
d.text((72, 193), LEAD_LABEL, font=F_LEAD_CAT, fill=GOLD, anchor="ls")
d.text((72, 254), LEAD_HEAD, font=F_LEAD_HEAD, fill=WHITE, anchor="ls")
d.text((72, 305), LEAD_SUM, font=F_LEAD_SUM, fill=SOFT, anchor="ls")

# ---- secondary stories (Y = block top; identical internal layout) ----
for (cat, head, summ), y in zip(STORIES, BLOCK_Y):
    d.rectangle([48, y, 48 + 4, y + 92], fill=BRONZE)
    d.text((68, y + 43), head, font=F_HEAD, fill=NAVY, anchor="ls")
    d.text((956, y + 38), cat, font=F_CAT, fill=BRONZE, anchor="rs")
    d.text((68, y + 82), summ, font=F_SUM, fill=SLATE, anchor="ls")
    d.rectangle([48, y + 100, 48 + 928, y + 102], fill=WARM)

img.save(OUT, "PNG", optimize=True)
data = open(OUT, "rb").read()
print("saved", OUT)
print("size:", img.size, "bytes:", len(data),
      "sha256:", hashlib.sha256(data).hexdigest())
print("limit 1048576 bytes:", "OK" if len(data) <= 1048576 else "FAIL")
assert img.size == (1024, 1024)
assert len(data) <= 1048576
