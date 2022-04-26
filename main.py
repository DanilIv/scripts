from PIL import Image, ImageEnhance

img2 = Image.open("\\\\dc\\users\\desktop\\d.antonov\\Desktop\\img\\benefit.png")
img = Image.open("\\\\dc\\users\\desktop\\d.antonov\\Desktop\\img\\Ulla_river.jpg").convert('RGBA')

img2 = img2.resize(img.size)


newImage = []
i = 1
good = 0
for item in img2.getdata():
    if i % img2.width == 1:
        if item[:3] == (255, 255, 255):
            good = 1
        else:
            good = 0
    if item[:3] == (255, 255, 255) and good == 1:
        newImage.append((255, 255, 255, 0))
    else:
        newImage.append(item)
    i= i + 1
img2.putdata(newImage)

img.paste(img2, (0, 0), img2)



img.save("\\\\dc\\users\\desktop\\d.antonov\\Desktop\\img\\2.png")
img.close()
img2.close()