import cv2
import numpy as np 
from matplotlib import pyplot as plt

img1 = cv2.imread("bliss.jpg", cv2.IMREAD_GRAYSCALE)
imgt1 = np.fft.fft2(img1)
img2 = cv2.imread("yousa.jpg", cv2.IMREAD_GRAYSCALE)
imgt2 = np.fft.fft2(img2)

amp1 = np.log(abs(imgt1))
pha1 = np.angle(imgt1)
amp2 = np.log(abs(imgt2))
pha2 = np.angle(imgt2)

corr_amp = np.corrcoef(amp1, amp2)
corr_pha = np.corrcoef(pha1, pha2)
print(np.sum(corr_amp), np.sum(corr_pha))

imgs = ['img1', 'amp1', 'pha1', 'corr_amp', 'img2', 'amp2', 'pha2', 'corr_pha']
names = ['image 1', 'amplitude 1', 'phase 1', 'correlation coefficient of amplitude', 'image 2', 'amplitude 2', 'phase 2', 'correlation coefficient of phase']

plt.figure()
for i in range(len(imgs)):
    ax=plt.subplot(2, 4, i + 1, xticks=[], yticks=[])
    ax.set_title(names[i])
    ax.imshow(eval(imgs[i]), cmap='gray')
plt.show()
