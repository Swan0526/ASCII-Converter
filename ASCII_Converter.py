from PIL import Image,ImageFont,ImageDraw
import string
from random import randint
from math import ceil
from ASCII_Converter_function import ASCII_Conv

minu=string.ascii_lowercase
maj=string.ascii_uppercase

def Pic_converter():
    path=input("Drag and drop your picture here :")
    if path[0]=='"':
        path=path[1:]
    if path[len(path)-1]=='"':
        path=path[:(len(path)-1)]

    reducer=int(input("Enter the ammount of reduction, the greater the number the smaller the image"))
    if reducer < 1:
        reducer = 1
    ASCII_Conv(path,reducer)
    print("Done !")

while True:
    Pic_converter()            
