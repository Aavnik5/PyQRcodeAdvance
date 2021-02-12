#  For Make qrcode in python you have to install these  things
# 1. pip install qrcode
# 2. pip install qrcode[pil]
# 3. pip install pillow


# for simple qrcode generate
'''
import qrcode
img = qrcode.make("Hello Aavnik yadav")
img.save("save.jpg") 
'''


# for Advance qrcode generate

import qrcode
from PIL import Image
logo = Image.open('instagram.jpg')
widthlogo = 70
persnt = (widthlogo/float(logo.size[0]))
hsize = int(float(logo.size[1])*float(persnt))
logo = logo.resize((widthlogo,hsize),Image.ANTIALIAS)
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data("Hello aavnik")
qr.make()
img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
pos = ((img.size[0]-logo.size[0])//2, (img.size[1]-logo.size[1]//2))
img.paste(logo,pos)
img.save("bshvgyuds.jpg")