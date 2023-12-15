from PIL import Image,ImageFont,ImageDraw
from ASCII_Converter_function import ASCII_Conv
from moviepy.editor import *
import cv2
import os
import shutil

def vid_converter():
    global reducer, number_frame_exact
    path=input("Drag and drop your video here :")
    if path[0]=='"':
        path=path[1:]
    if path[len(path)-1]=='"':
        path=path[:(len(path)-1)]

    reducer=int(input("Enter the ammount of reduction, the greater the number the smaller the image"))
    if reducer < 1:
        reducer = 1
    frame_extractor(path)
    clip = VideoFileClip(path)
    current_fps=clip.fps
    duration=clip.duration
    frame_number=int(duration*current_fps)
    for i in range(frame_number-1):
        ASCII_Conv(path+"_temp/"+str(i)+".png",reducer)
        print("Frame "+str(i)+" / "+str(frame_number)+" Done")
        number_frame_exact=i
    compil(clip,path,current_fps)
    shutil.rmtree(path+"_temp")
    clip.close()
    print("Done !")

def frame_extractor(path):
    print("Extracting frame...")
    cap= cv2.VideoCapture(path)
    os.mkdir(path+"_temp")
    i=0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            break
        cv2.imwrite(path+"_temp/"+str(i)+'.png',frame)
        i+=1
    cap.release()
    print("Done !")

def compil(clip,path,fps):
    print("Start compiling... (please note that this process need a lot of free RAM)")
    duration=clip.duration
    frame_number=number_frame_exact
    all_image=[path+"_temp/"+str(i)+"_reducer-set-to_"+str(reducer)+".png" for i in range(frame_number-1)]
    clips = [ImageClip(i).set_duration(duration/len(all_image)) for i in all_image]
    concat_clip = concatenate_videoclips(clips,method="compose")
    export = concat_clip.set_audio(clip.audio)
    export.write_videofile(path+"_ASCII.mp4",fps=fps)

while True:
    vid_converter()
