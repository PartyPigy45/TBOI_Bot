from PIL import Image
import os

LENGTH = len("achievement_")

for img in os.listdir("raw_images"):
    if ".png" == img[-4::]:
        background = Image.open("paper.png")
        foreground = Image.open("./raw_images/" + img)

        background.paste(foreground, (0, 0), foreground)
        background.save("./images/"+img[LENGTH::], "PNG")