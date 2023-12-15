from PIL import Image,ImageFont,ImageDraw
import string
from random import randint
from math import ceil


minu=string.ascii_lowercase
maj=string.ascii_uppercase
    
def ASCII_Conv(path,reducer):
        print("Opening image...")
        img=Image.open(path,"r")
        print("Image opened")
        print("Data acquisition...")
        pix_val = list(img.getdata())
        print("Data acquired")

        size = img.size

        vertical_reducer=ceil(size[0]/size[1])+2*ceil(size[1]/size[0])
        print("Creating txt file...")
        extention=len(path)-1
        while path[extention]!=".":
            path=path[:extention]
            extention-=1
        path=path[:extention]
        fichier = open(path+"_reducer-set-to_"+str(reducer)+".txt", "w")
        print("Txt file created")

        for y in range(0,size[1],vertical_reducer+(reducer//2)):
            for x in range(0,size[0],1*reducer):
                pixel=pix_val[y*size[0]+x][0]
                if pixel>230:
                    fichier.write("\u00a0")
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
                    
            fichier.write("\n")
            if y/size[1]==0.25:
                print("Stage : 25% Done")
            if y/size[1]==0.50:
                print("Stage : 50% Done")
            if y/size[1]==0.75:
                print("Stage : 75% Done")
        fichier.close()
        print("Creating image...")
        img = Image.new('RGB', (int(((size[0]+120)*10)/reducer), int(((size[1]+120)*10)/reducer)), color = (255,255,255))
        fnt = ImageFont.truetype("Consolas-Font/Consolas.ttf", 20)
        ascii_text=open(path+"_reducer-set-to_"+str(reducer)+".txt")

        ImageDraw.Draw(img).text((0,0), ascii_text.read(), font=fnt, fill=(0,0,0))
        img.save(path+"_reducer-set-to_"+str(reducer)+".png")
        
