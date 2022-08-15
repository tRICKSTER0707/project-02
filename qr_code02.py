import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=20,
                 border=5,)
qr.add_data("https://www.linkedin.com/in/amit-kumar-yadav-5b34ba227")
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save("profile2.png")
# helloo