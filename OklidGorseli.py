import matplotlib.pyplot as plt  # matplotlib kütüphanesi import edildi.
import matplotlib.image as mpimg

img = mpimg.imread('OklidMesafesi.jpeg') # jpeg dosyasını okumasını sağladım.

plt.imshow(img)
plt.axis('on') # Eksenleri göstermesini istedim.
plt.show()