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
        bg_photo=Image.open('images/banner.png') #Mở hình ảnh banner ở trang màn hình chính
        bg_photo=bg_photo.resize((1620,912),Image.BICUBIC)  #Thay đổi kích thước banner thành 1620x912 với bộ lọc BICUBIC
        bg_photo = ImageTk.PhotoImage(bg_photo)
        bg = tkinter.Label(image=bg_photo,bd=0) #Tạo lable cho banner với vị trí ơ305;60]
        bg.image=bg_photo
        bg.place(x=120,y=100)
        startBtn=Button(window,
                  text='Start',
                  command=barcodeScanner,
                  font=('Montserrat',15),
                  height='2',
                  width='15',
                  fg='#ffffff',
                  bg='#3700b3',
                  ).place(x=830,y=750)
    def barcodeScanner():
        barcodeCanvas = Canvas(window, width=width_value, height=height_value) #Thiết lập canvas có kích thước 1920x1080
        barcodeCanvas.place(x=0, y=0)
        Label(barcodeCanvas,text='Bacide',font=('Montserrat', 15),bg='#1C2A3A',fg='#ffffff').place(x=110,y=20)
        camera = cv2.VideoCapture(1)
        #HCM = 1, KH = 2, DN = 3
        xylanh=['','','']
        # xylanh[0]= product_name1
        # xylanh[1]= product_name2
        # xylanh[2]= product_name3
        xylanh[0]= 'hochiminh'
        xylanh[1]= 'DONGNAI'
        xylanh[2]= 'KHANH Hoa'
        while True:
            r, frame = camera.read() 
            barcodes = pyzbar.decode(frame)
            for barcode in barcodes:
                x,y,w,h = barcode.rect

                barcode_text=barcode.data.decode('utf-8')
                for item in items:           
                    if barcode_text==item[1]:
                        for i in range(len(xylanh)):
                            output = str(int(difflib.SequenceMatcher(None, xylanh[i].strip().lower(), item[2].strip().lower()).ratio()*100))
                            if int(output)>70:
                                print("Day xylanh"+str(i+1))
                                # client.write_register(0,i+1,unit=UNIT)
                                print(item[2])
                sleep(1)
                
                # cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.imshow('Barcode reader',frame)
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            img_update = ImageTk.PhotoImage(image=Image.fromarray(cv2image))
            lable_image = Label(barcodeCanvas)
            lable_image.place(x=770, y=250)
            lable_image.configure(image=img_update)
            lable_image.image = img_update
            lable_image.update()
            if cv2.waitKey(1) & 0xFF == ord('q'): 
                break
        camera.release()
        cv2.destroyAllWindows()
    inmain()
    window.mainloop()
mainfunc()
