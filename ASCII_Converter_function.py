from PIL import Image,ImageFont,ImageDraw
from tqdm import tqdm
from math import ceil
import string
from random import randint

minu=string.ascii_lowercase
maj=string.ascii_uppercase
    
def ASCII_Conv(path,reducer,resolution):
        print("Opening image...")
        img=Image.open(path,"r")
        print("Image opened")
        print("Data acquisition...")
        pix_val = list(img.getdata())
        print("Data acquired")

        size = img.size

        print("Creating txt file...")
        extention=len(path)-1
        while path[extention]!=".":
            path=path[:extention]
            extention-=1
        path=path[:extention]
        fichier = open(path+"_reducer-set-to_"+str(reducer)+".txt", "w")
        print("Txt file created")

        fnt = ImageFont.truetype("Consolas-Font/Consolas.ttf", resolution)
        char_bbox = fnt.getbbox("a")
        font_width = char_bbox[2] - char_bbox[0]
        font_height = char_bbox[3] - char_bbox[1]  

        for y in tqdm(range(0,size[1],reducer)):
            for x in range(0,size[0],reducer):
                pixel=pix_val[y*size[0]+x][0]
                if pixel>230:
                    fichier.write(" ")
                elif pixel>199:
                    fichier.write(".")
                elif pixel>180:
                    fichier.write("-")
                elif pixel>150:
                    fichier.write(minu[randint(0,len(minu)-1)])
                elif pixel>100:
                    fichier.write(maj[randint(0,len(maj)-1)])
                elif pixel>50:
                    fichier.write("#")
                else:
                    fichier.write("@")
                fichier.write(" ")
                    
            fichier.write("\n")

        print(font_height)
        print(font_width)

        fichier.close()
        print("Creating image...")
        img = Image.new('RGB', (ceil(size[0]/reducer*font_width*2) , ceil(size[1]/reducer*font_height*1.9)), color = (255,255,255))
        ascii_text=open(path+"_reducer-set-to_"+str(reducer)+".txt")

        ImageDraw.Draw(img).text((0,0), ascii_text.read(), font=fnt, fill=(0,0,0))
        img.save(path+"_reducer-set-to_"+str(reducer)+".png")
        
