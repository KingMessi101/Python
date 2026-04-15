import os, io, time, random, requests, mimetypes
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from config import HF_API_KEY

API = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
ALLOWED = {".jpg",".jpeg",".png",".webp",".bmp",".tiff"}

def get_image():
    while True:
        p = input("Image path: ").strip('"')
        if os.path.isfile(p) and os.path.splitext(p)[1].lower() in ALLOWED:
            return p
        print("⚠️ Invalid file.")

def infer(path, data):
    mime = mimetypes.guess_type(path)[0]
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    if mime and mime.startswith("image/"):
        headers["Content-Type"] = mime
        r = requests.post(API, headers=headers, data=data)
    else:
        r = requests.post(API, headers=headers,
                          files={"inputs": (os.path.basename(path), data)})
    if r.status_code != 200: raise Exception(r.text)
    return r.json()

def draw(img, dets):
    d = ImageDraw.Draw(img)
    f = ImageFont.load_default()
    for det in dets:
        if det["score"] < 0.5: continue
        b = det["box"]
        x1,y1,x2,y2 = map(int,[b["xmin"],b["ymin"],b["xmax"],b["ymax"]])
        color = tuple(random.randint(100,255) for _ in range(3))
        d.rectangle([x1,y1,x2,y2], outline=color, width=3)
        d.text((x1,y1), f"{det['label']} {det['score']:.2f}", fill=color, font=f)

def main():
    path = get_image()
    data = open(path,"rb").read()
    dets = infer(path, data)

    img = Image.open(io.BytesIO(data)).convert("RGB")
    draw(img, dets)

    out = f"out_{datetime.now().strftime('%H%M%S')}.png"
    img.save(out)
    print("✅ Saved:", out)

if __name__ == "__main__":
    main()