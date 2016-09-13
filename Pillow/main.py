from PIL import Image

imgOne = Image.open("1.png")
print(imgOne.size)
print(imgOne.format)

area = (10,10,30,38)
cropped_image = imgOne.crop(area)

#imgOne.show()
#cropped_image.show()

imgTwo = Image.open("2.png")

imgTwo.paste(imgOne, area)
imgTwo.show()