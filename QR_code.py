#qrcode library to handle the generation
import qrcode 

#Define the string or URL to be encoded
data = "https://www.python.org"

#Use the make() shortcut to create a QR code image object
#The library automatically determines the version and size based on the data
img = qrcode.make(data)

#Save the image object to a file in the current directory
img.save("python_qr.png")

#Print a confirmation message to the console
print("QR code generated and saved as python_qr.png")