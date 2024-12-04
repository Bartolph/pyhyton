from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
from random import *
def hello():
    res = "Привет, {}!".format(hie.get())  
    higol.configure(text=res)
    
    
def summ():
    n1 = int(sum1.get())
    n2 = int(sum2.get())
    if n2 != 0:
        delen = n1/n2
    else:
        delen = "на 0 нельзя!!!!!!!"
    res = "Сложение: {}\nВычитание: {}\nУмножение: {}\nДеление: {}".format(n1+n2, n1-n2, n1*n2, str(delen))  
    results.configure(text=res)
    
    
def viborfaila():
    textz = askopenfilename()
    openz = open(textz, "w")
    for i in range(10):
        openz.write(str(randint(1, 10))+" ")
    openz.close()
    openz = open(textz, "r")
    arithmetic = openz.read().split(" ")
    arithmetic.pop()
    xz= map(int, arithmetic)
    srednee = sum(xz)/(len(arithmetic))
    with open(textz, "a") as openz:
        openz.write("\nСреднее арифметическое - " + str(srednee))
    openz.close()
    sred.configure(text="Числа: {}\nСреднее арифметическое: {}".format(' '.join(arithmetic) ,srednee))
    
    
window = Tk()
window.title("Выберите заданя")
window.geometry('800x800')

tonk = Image.open("Tonk.png")
tonk = tonk.resize((90, 90)) 
photo = ImageTk.PhotoImage(tonk)
image_label = Label(window, image=photo, bg="#B2DFDB")
image_label.pack(pady=10)

imegor = Label(window, text="TOOONK", font=20, bg="lightgreen")#Здесь измененияefrh,.l,hnfedswdgtul;/.lkhgrfeswdfghjklk455
imegor.pack(ipady=10, pady=10)
hi = Label(window, text="Задание привет", bg="lightgreen")
hi.pack(ipady=10, pady=10)
hie = Entry(window)
hie.pack(ipady=10, pady=10)
hib = Button(window, text="ПРИВЕТ", command=hello, bg="white", borderwidth=0, height=1, width=15, fg="darkgreen")
hib.pack(ipady=10, pady=10)
higol = Label(window, bg="lightgreen")
higol.pack(ipady=10, pady=10)

suma = Label(window, text="Задание математика", bg="lightgreen")
suma.pack(ipady=10, pady=10)
sum1 = Entry(window, width=30)
sum1.pack(ipady=10, pady=10)
sum2 = Entry(window, width=30)
sum2.pack(ipady=10, pady=10)
summirovat = Button(window, text="Математека", command=summ, bg="white", borderwidth=0, height=2, width=15, fg="darkgreen")
summirovat.pack(ipady=10, pady=10)
results = Label(window, bg="lightgreen")
results.pack(ipady=10, pady=10)

vibor = Label(window, text="Задание выбрать файл", bg="lightgreen")
vibor.pack(ipady=10, pady=10)
summirovat = Button(window, text="Выбрать", command=viborfaila, bg="white", borderwidth=0, height=2, width=15, fg="darkgreen")
summirovat.pack(ipady=10, pady=10)
sred = Label(window, bg="lightgreen")
sred.pack(ipady=10, pady=10)

window.configure(bg="lightgreen")
window.mainloop()