import cv2
import numpy as np
from PIL import Image
from glob import glob

W = 1920
H = 1080

listOfWallpapers = glob(r".\Wallpapers\**")

for i in listOfWallpapers:
    for j in listOfWallpapers:
        for k in listOfWallpapers:
            if i is not j and i is not k and j is not k :
                print(f"working on {i} & {j} & {k}")
                print()
                img1 = cv2.imread(i, -1)
                img1 = cv2.resize(img1, (W, H))

                img2 = cv2.imread(j, -1)
                img2 = cv2.resize(img2, (W, H))

                img3 = cv2.imread(k, -1)
                img3 = cv2.resize(img3, (W, H))

                imgN = np.concatenate((img1, img2, img3))
                imgN = imgN[:, :, ::-1]

                # imgN = np.sort(imgN)
                imgN = np.sort(imgN, axis=0)
                imgN = np.flip(imgN, axis=0)

                imgN = np.sort(imgN, axis=1)
                imgN = np.flip(imgN, axis=1)
                # imgN = np.sort(imgN,axis=2)

                # imgN = cv2.blur(imgN,(10,10))
                # imgN = cv2.GaussianBlur(imgN, (5,5),0)
                # imgN = cv2.medianBlur(imgN,5)
                imgN = cv2.dilate(imgN, np.ones((255,255), np.uint8), iterations=1)
                imgN = cv2.GaussianBlur(imgN, (255, 255), 0)

                imgN = cv2.resize(imgN, (int(W), int(H)))

                img = Image.fromarray(imgN)

                outputPath = f"{i}_WITH_{j}_WITH_{k}".replace(".\\Wallpapers\\","")
                img.save(f".\\Output6\\{outputPath}")
