import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread("tiger.png")

#a
plt.imshow(np.clip(img + 0.5, 0, 1))
plt.title("Posvijetljena slika")
plt.show()

#b
plt.imshow(np.rot90(img, k=-1))
plt.title("Rotirano u smijeru kazaljke na satu")
plt.show()

#c
plt.imshow(np.fliplr(img))
plt.title("Zrcaljena slika")
plt.show()

#d
plt.imshow(img[::10, ::10])
plt.title("Smanjena rezolucija")
plt.show()

#e
img_part = np.zeros_like(img)
sirina = img.shape[1]
pocetak= sirina // 4
kraj = pocetak * 2
img_part[:,pocetak:kraj] = img[:, pocetak:kraj]
plt.imshow (img_part[::10, ::10])
plt.title("Druga cetvrtina")
plt.show()
