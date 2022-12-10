import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from time import sleep
import cv2
from numpy import product
from pyzbar import pyzbar
from database import items
import difflib
def mainfunc():
    '''---------Cửa sổ chính---------'''
    window = Tk()   #Tạo cửa sổ window
    width_value=window.winfo_screenwidth()
    height_value=window.winfo_screenheight()
    window.geometry("%dx%d+0+0" % (width_value, height_value))  #Thiết lập kích thước cửa sổ
    window.title('Barcode Scanner')    #Tên cửa sổ

    # icon = PhotoImage(file='../pic/logospkt.png')  #icon của cửa sổ
    # window.iconphoto(True,icon)

    def inmain():
        '''---------Tạo canvas cho màn hình HOME---------'''
        mainCanvas = Canvas(window, width=width_value, height=height_value, bg='#f5f5f5') #Thiết lập canvas có kích thước 1920x1080
        mainCanvas.place(x=0, y=0)
        # Label(mainCanvas,text='Face Attendance',font=('Montserrat', 15),bg='#1C2A3A',fg='#f5f5f5').place(x=110,y=20)
        bg_photo=Image.open('E:/dang hoc/Do_An_PLC/barcode-scanner/src/images/banner.png') #Mở hình ảnh banner ở trang màn hình chính
        bg_photo=bg_photo.resize((1280,712),Image.BICUBIC)

        bg_photo = ImageTk.PhotoImage(bg_photo)
        bg = tkinter.Label(image=bg_photo,bd=0)
        bg.image=bg_photo
        bg.place(x=120,y=50)
        startBtn=Button(window,
                  text='Start',
                  command=barcodeScanner,
                  font=('Montserrat',15),
                  height='2',
                  width='15',
                  fg='#ffffff',
                  bg='#3700b3',
                  ).place(x=650,y=600)
    def barcodeScanner():
        barcodeCanvas = Canvas(window, width=width_value, height=height_value, bg='#f5f5f5') #Thiết lập canvas có kích thước 1920x1080
        barcodeCanvas.place(x=0, y=0)
        Label(barcodeCanvas,text='Barcode Reader',font=('Montserrat', 15) ,fg='#1C2A3A').place(x=680,y=30)
        camera = cv2.VideoCapture(0)
        while True:
            r, frame = camera.read() 
            barcodes = pyzbar.decode(frame)
            for barcode in barcodes:
                x,y,w,h = barcode.rect

                barcode_text=barcode.data.decode('utf-8')

                for item in items:           
                    if barcode_text==item[1]:
                        print("Day xylanh "+str(item[0]))
                        # client.write_register(0,i+1,unit=UNIT)
                        print(item[2])
                        Label(barcodeCanvas,text='Ho Chi Minh',font=('Montserrat', 15),bg='#f5f5f5',fg='#f5f5f5').place(x=700,y=700)
                        Label(barcodeCanvas,text=item[2],font=('Montserrat', 15),bg='#1C2A3A',fg='#f5f5f5').place(x=700,y=700)
                # sleep(1)
                
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                Label(barcodeCanvas,text=barcode_text,font=('Montserrat', 15),bg='#1C2A3A',fg='#f5f5f5').place(x=700,y=650)
            # cv2.imshow('Barcode reader',frame)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img_update = ImageTk.PhotoImage(image=Image.fromarray(cv2image))
            lable_image = Label(barcodeCanvas)
            lable_image.place(x=450, y=100)
            lable_image.configure(image=img_update)
            lable_image.image = img_update
            lable_image.update()
    inmain()
    window.mainloop()
mainfunc()
