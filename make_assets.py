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

# Splash bawaan Android: layar hitam polos.
# Logo muncul perlahan di dalam aplikasi (lihat #intro di www/index.html).
splash = Image.new("RGB", (2732, 2732), (0, 0, 0))
splash.save("assets/splash.png")
splash.save("assets/splash-dark.png")
print("ikon dan splash dibuat")
