import qrcode

url = input("Enter your URL: ")
filename = input("Enter the file name to be saved as: ")
if not(filename.endswith('.png')):
    filename = filename + '.png'

img = qrcode.make(url)
img.save(filename)
