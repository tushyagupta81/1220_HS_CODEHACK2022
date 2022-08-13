from tkinter import *
from functools import partial
import ast
import json

jobs = []
with open('job_listings.txt') as f:
    data = f.read()
try:
    js = ast.literal_eval(data)
except:
    js = {}



root = Tk()
root.geometry("540x960")
root.title("callow")
root.configure(background = "beige")

def userLogin():
    def submit():
        def click(id_number):
            def take_job():
                del js[id_number]
                t = open('job_listings.txt','w')
                t.write(json.dumps(js))
                t.close()
                o.destroy()
                o2.destroy()
                Label(root,text="Job has been assigned").pack()

            listbox.destroy()
            scrollbar.destroy()
            o = Label(root,text=js[id_number])
            o.pack()
            o2 = Button(root,text="Take job",command=take_job)
            o2.pack()

        y = clicked.get()

        drop.destroy()
        sub.destroy()

        listbox = Listbox(root)
        
        listbox.pack(side = LEFT, fill = BOTH)
        scrollbar = Scrollbar(root)
        scrollbar.pack(side = RIGHT, fill = BOTH)
        for i in js.keys():
            if js[i]['for'] == y:
                listbox.insert(END, Button(listbox,text = str(js[i]),command=partial(click,i)).pack())
        listbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = listbox.yview)


    Employer.destroy()
    User.destroy()

    clicked = StringVar()
    clicked.set('Select your profession')
    drop = OptionMenu( root , clicked , 'painter','carpenter','plumber','gardener','leather worker','driver','construction worker','domestic worker','electrician','fisherman','sweeper','mason','rickshaw puller','weaver','tailor')
    drop.pack()
    sub = Button(root,text="Submit",padx=5,pady=3,command=submit)
    sub.pack()

def employerLogin():
    
    def click2():
        dect = {
            'form':a1.get(),
            'for':b1.get(),
            'price':c1.get(),
            'address':d1.get()
        }
        if len(js.keys()) > 0:
            n = int(list(js)[-1])
        else:
            n = 0
        js[n+1] = dect
        l = open('job_listings.txt','w')
        l.write(json.dumps(js))
        l.close()
        Label(root ,text="Order done").pack()
    Employer.destroy()
    User.destroy()
    a = Label(root ,text = "Name").pack()
    b = Label(root ,text = "Worker Type").pack()
    c = Label(root ,text = "Price per hour").pack()
    d = Label(root ,text = "Address").pack()
    a1 = Entry(root)
    b1 = Entry(root)
    c1 = Entry(root)
    d1 = Entry(root)
    a1.pack()
    b1.pack()
    c1.pack()
    d1.pack()
    sub2 = Button(root,text="Submit",padx=5,pady=3,command=click2)
    sub2.pack()

User = Button(root,text="Worker",padx=5,pady=3,command=userLogin,font=('Arial',25))
Employer = Button(root,text="Employer",padx=5,pady=3,command=employerLogin,font=('Arial',25))
User.pack()
Employer.pack()


root.mainloop()
