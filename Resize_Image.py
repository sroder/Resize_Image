from PIL import Image

basewidth = 500
img = Image.open('sample_image.jpeg')
#wpercent = (basewidth/float(img.size[0]))
#hsize = int((float(img.size[1])*float(wpercent)))
horizontal = 500
img = img.resize((basewidth,horizontal), Image.ANTIALIAS)
img.save('Resized_sample_image.jpeg')
