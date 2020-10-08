#pip3 install pyqrcode
#pip3 install png


import pyqrcode 
import png 
from pyqrcode import QRCode 
  
   
s = input("Web Adresse hier eingeben / Text")
  
url = pyqrcode.create(s)
  
url.svg("myqr.svg", scale = 8) 
  
url.png('myqr.png', scale = 6) 
