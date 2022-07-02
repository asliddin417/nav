from tkinter import *

dict1 = {'work': 'ish', 'individual': 'shaxsiy', 'project': 'loyixa'}


def tran():
    text = t.get('1.0', END)
    text = str(text).replace('\n', '')
    a = dict1[text]
    t1.delete('1.0', END)
    t1.insert('1.0', a)


root = Tk()
root.geometry('500x350')
root.title('Tarjimon')
root.resizable(width=False, height=False)
root['bg'] = 'white'

label = Label(root, fg='black', bg='white', font='Arial 15 bold', text='Ingiliz tilidagi atamani kiriting')
label.place(relx=0.5, y=30, anchor=CENTER)
t = Text(root, width=35, height=5, font='Arial 12 bold')
t.place(relx=0.5, y=100, anchor=CENTER)

btn = Button(root, width=45, text='Перевести', command=tran)
btn.place(relx=0.5, y=180, anchor=CENTER)

t1 = Text(root, width=35, height=5, font='Arial 12 bold')
t1.place(relx=0.5, y=260, anchor=CENTER)

root.mainloop()