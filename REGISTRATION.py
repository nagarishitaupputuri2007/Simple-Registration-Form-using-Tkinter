import tkinter as tk
from tkinter import messagebox,PhotoImage
import os

R=tk.Tk()
R.geometry('420x520')
img=PhotoImage(file='cal.png')
R.iconphoto(False,img)
def Register():
    a=str(t1.get())
    b=str(t2.get())
    c=str(t3.get())
    # messagebox.showinfo('REGISTRATION','DETAILS ARE '+ 'Name:'+ a+b+ ' Mobileno:'+ c)
    if os.path.exists("first.csv"):
        file=open("first.csv","a")
        file.write("\n{},{},{}".format(a,b,c))
        messagebox.showinfo("New","New Record Added!")
    else:
        file=open("first.csv","x")
        file.write("{},{},{}".format("Fname","Lname","Mobile"))
        file.write("\n{},{},{}".format(a,b,c))
        messagebox.showinfo("New","New Record Added!")

        
L1=tk.Label(R,text='First Name')
L2=tk.Label(R,text='Last Name')
L3=tk.Label(R,text='Mobile')
t1=tk.Entry()
t2=tk.Entry()
t3=tk.Entry()
button=tk.Button(R,text='SUBMIT',command=Register)
L1.pack(pady=20)
t1.pack(pady=20)
L2.pack(pady=20)
t2.pack(pady=20)
L3.pack(pady=20)
t3.pack(pady=20)
button.pack(pady=20)
# def txtFile():
#     f=open('REGISTRATION.txt','w')
#     f.write("First Name")
#     f.write("Last Name")
#     f.write("Mobile NO")
# def csvfile():
#     # w=csv.writer(f,delimeter=',')
#     # import csv
#     # F=open("Registration.csv",'w',newline='')
#     # W=csv.writer(F)
#     # Data=[['Firstname','Lastname','Mobileno'],['Naga Rishita','Upputuri','9030134104,9848899244']]
#     # w.writerows(Data)
#     # F.close()
#     txtFile()
R.mainloop()