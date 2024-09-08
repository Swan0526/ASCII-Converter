from ASCII_Converter_function import ASCII_Conv

def Pic_converter():
    path=input("Drag and drop your picture here : ")
    if path[0]=='"':
        path=path[1:]
    if path[len(path)-1]=='"':
        path=path[:(len(path)-1)]

    reducer = int(input("Enter the ammount of reduction, the greater the number the smaller the image (1 - 32): "))

    resolution = int(input("Choose the resolution (1 - 20) : "))

    if reducer < 1:
        reducer = 1
    if reducer > 32:
        reducer = 32

    if resolution < 1:
        resolution = 1
    if resolution > 20:
        resolution = 20

    ASCII_Conv(path,reducer,resolution)
    print("Done !")

while True:
    Pic_converter()            
