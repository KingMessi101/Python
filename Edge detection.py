import cv2, numpy as np, matplotlib.pyplot as plt

def display(title, img, cmap=None):
    plt.figure(figsize=(6,6))
    plt.imshow(img if cmap is None else cv2.cvtColor(img, cmap))
    plt.title(title); plt.axis("off"); plt.show()

def edge_Activity(path):
    img = cv2.imread(path)
    if img is None: return print("image not found")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    display("original", img, cv2.COLOR_BGR2RGB)
    display("grayscale", gray)

    def sobel():
     sx, sy = cv2.Sobel(gray, cv2.CV_64F, 1,0, ksize=3), cv2.Sobel(gray, cv2.CV_64F, 0,1, ksize=3)
     return cv2.bitwise_or(sx.astype(np.uint8), sy.astype(np.uint8))

    def anny():
     l, u = map(int,(input("lower (default 100):") or 100, input("upper (default 200):") or 200))
     return cv2.Canny(gray, l, u)

def laplacian (): return cv2.Laplacian(gray, cv2.CV_64F) .astype(np.uint8)

def blur(): return cv2.GaussianBlur(img,(int(input("Kernel (odd, default 5):") or 5),)*2,0)

def median(): return cv2.medianBlur(img,int(input("Kernel (odd, default 5):") or 5))