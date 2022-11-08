from tkinter import *
import tkinter as tk
from tkinter import ttk
import requests
import json
from tkinter import messagebox

chat=tk.Tk()
chat.geometry("500x500")

contactos=["Milagro","Vasni","Papi"]
numeros=["62440403","88667800","88925080"]

def accion(event):
    contacto=numlist.current()
    num.delete(0,END)
    num.insert(0,numeros[contacto])

def enviartexto():

    reqUrl = "http://51.222.14.197:3040/lead"

    headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)",
    "Content-Type": "application/json" 
    }

    payload = json.dumps({
    "message": message.get("1.0",END),
    "phone": "506"+num.get()
    })
    response = requests.request("POST", reqUrl, data=payload,  headers=headersList)
    messagebox.showinfo("Enviar","El mensaje ha sido enviado exitosamente")
    message.delete("1.0",END)
    num.delete(0,END)

def añadircontacto():
    contactos.append(numlist.get())
    numeros.append(num.get())
    numlist.config(values=contactos)
    messagebox.showinfo("Contactos","El contacto ha sido añadido exitosamente")
    
num=Entry(font=(12),width=10)
num.place(x=1,y=370)

message=Text(font=(12))
message.place(x=0,y=400,width=400,height=100)

send=Button(text="Enviar",command=enviartexto)
send.place(x=400,y=400,width=100,height=100)

numlist=ttk.Combobox(values=contactos)
numlist.place(x=1,y=300)
numlist.bind("<<ComboboxSelected>>", accion)

addcontact=Button(text="Añadir Contacto",command=añadircontacto)
addcontact.place(x=150,y=300)

chat.mainloop()