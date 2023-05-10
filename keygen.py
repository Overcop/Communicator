from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox
import  scripttools as st
def main():
    print("before generating keys please select a dir to do so")
    print("ready to select press enter")
    input()
    dir = askdirectory()#ask a derectory to save the keys in
    private_key = rsa.generate_private_key(# generate a private key
            public_exponent=65537,
            key_size=2048,
        )
    while True:
        rep = st.Ilist(["question"], ["Do you want to put a password on the private key?"], [["Yes", "No"]])
        if rep == 0:
            root = Tk()#create a window to enter the password
            root.title("Set private key encryption password")
            Label(root, text="enter private key password:").grid(row=0, column=0)
            Label(root, text="repeat password:").grid(row=1, column=0)
            ent = Entry(root, show="*", width=50)
            ent2 = Entry(root, show="*", width=50)
            ent.grid(row=0, column=1)
            ent2.grid(row=1, column=1)


            def getinput():#funcntion linked to the button
                if ent.get() == ent2.get():#check if the two passwords are the same
                    global passw
                    passw = bytes(ent.get(), 'utf-8')#put the password into bytes
                    root.destroy()#kill the window
                else:
                    tkinter.messagebox.showerror(message="The passswords do not match!", title="Error")#create a dialog window to tell that the password doses not match


            b = Button(root, text="submit", command=lambda: getinput())
            b.grid(row=3, column=1)
            root.mainloop()
            public_key = private_key.public_key()#get the public key from the private key
            serial_private = private_key.private_bytes(#put private the key into bytes and encode it with the given password
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.BestAvailableEncryption(passw)
            )
            serial_pub = public_key.public_bytes(#put the public key into bites
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
            # create the file and write them
            with open(dir+"/public.pem", "wb") as f: f.write(serial_pub)
            with open(dir+"/private.pem", "wb") as f: f.write(serial_private)
            print("done!\n")
            return
        elif rep == 1:
            public_key = private_key.public_key()#get the public key
            serial_private = private_key.private_bytes(#put the private key into bytes without a password
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
            serial_pub = public_key.public_bytes(#put the public key into bytes
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
            #write the files
            with open(dir + "/public.pem", "wb") as f:
                f.write(serial_pub)
            with open(dir + "/private.pem", "wb") as f:
                f.write(serial_private)
            print("done!\n")
            return
