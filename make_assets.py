# Membuat ikon dan splash screen Drakoo (dipakai oleh build-apk.yml)
import os
from PIL import Image, ImageDraw, ImageFont

BG = (26, 15, 31)
GOLD = (255, 178, 62)
CREAM = (251, 241, 234)
os.makedirs("assets", exist_ok=True)

def logo(size):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, size - 1, size - 1), radius=int(size * 0.25), fill=GOLD)
    s = size
    d.polygon([(s * 0.38, s * 0.28), (s * 0.38, s * 0.72), (s * 0.74, s * 0.5)], fill=BG)
    return im

# Ikon 1024x1024 (logo berada di area aman untuk ikon adaptif Android)
icon = Image.new("RGB", (1024, 1024), BG)
icon.paste(logo(580), (222, 222), logo(580))
icon.save("assets/icon-only.png")

# Splash 2732x2732
splash = Image.new("RGB", (2732, 2732), BG)
lg = logo(620)
splash.paste(lg, ((2732 - 620) // 2, 980), lg)
d = ImageDraw.Draw(splash)
font = None
for path in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
             "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"):
    if os.path.exists(path):
        font = ImageFont.truetype(path, 170)
        break
if font:
    w = d.textlength("Drakoo", font=font)
    d.text(((2732 - w) / 2, 1700), "Drakoo", font=font, fill=CREAM)
splash.save("assets/splash.png")
splash.save("assets/splash-dark.png")
print("ikon dan splash dibuat")
