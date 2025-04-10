# import qrcode 

# data = 'Don\'t forget to read my code '
# img = qrcode.make(data)
# qr = qrcode.QRCode(version = 1, box_size = 10, border = 4)
# qr.add_data(data) # Add data to the QR code
# qr.make(fit=True) # Fit the QR code to the data
# img = qr.make_image(fill_color='blue' , back_color='white') # Create the QR code image with specified colors


# img.save('C:/Users/user/Documents/qrcodeimg/myqrcode1.png') # Save the QR code as an image file

from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/user/Documents/qrcodeimg/myqrcode.png')
result = decode(img) # Decode the QR code image
print(result)

