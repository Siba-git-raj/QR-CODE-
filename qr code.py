import pyqrcode
content = input("enter your name :-")
QR = pyqrcode.create(content)
QR.png("my.png",scale=5)
print("success")
