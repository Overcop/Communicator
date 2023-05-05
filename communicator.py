from tkinter import *
from tkinter.filedialog import *
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
class msg: #create a message class
    def __init__(self,message,path ,private=None,pripass=None,pub=None):
        self.message = message #message to decrypt or encrypt
        self.mpath = path #saves the path to the file
        self.prikey = private #store private key
        self.pripass = pripass #private key password
        self.pubkey = pub #store public key
        self.abort = False #tool to detect abortion of an operation
        self.end = False #are the operations finished?
    def menu(self): #simple menu
        while True: #loops the menu until the operation is finished
            self.abort = False #reset the abort condition
            if self.end == True:#end communicator to return to the menu
                return
            print("what operation you want to execute?")
            print("1.encrypt a message")
            print("2.decrypt file")
            print("3.go back")
            rep = input("$> ")
            print("")
            if int(rep) == 1:
                self.prtclencrypt()
            elif int(rep) == 2:
                self.prtcldecrypt()
            elif int(rep) == 3:
                return
    def getkey(self,type):
        #ask the user to select a key with a dialog window the arguments are:
        # or "pub" for a public key
        # or "pri" for a private key
        Tk().withdraw()
        filename = askopenfilename()
        if type=="pub":
            f = open(filename,"rb")
            self.pubkey = f.read()
            self.load_public()
        elif type=="pri":
            f = open(filename,"rb")
            self.prikey = f.read()
            self.load_private()
    def load_public(self): # loads the public key
        try:
            self.pubkey = serialization.load_pem_public_key(self.pubkey)
        except ValueError: #check if the given key is valid if not abort and return to de menu
            print("invalid key!\n")
            self.abort = True
            return
        print("public key successfully loaded!\n")
    def load_private(self):
        try: self.prikey = serialization.load_pem_private_key(self.prikey,password=None) #cheks if the key have a password
        except TypeError: #the key have a password
            while True:
                print("the selected key require a password")
                print("1. enter the password")
                print("2. select an other key")
                print("3. abort")
                rep = input("$> ")
                print("")
                if rep == "" or int(rep) == 1: #window to enter the password
                    root = Tk()
                    root.title("Private key encryption password")
                    Label(root, text="enter private key password:").grid(row=0, column=0)
                    ent = Entry(root, show="*", width=50)
                    ent.bind('<Control-c>', lambda e: 'break')
                    ent.grid(row=0, column=1)

                    def getinput(): # action of the buton to get the input
                        self.pripass = bytes(ent.get(), 'utf-8')
                        print(self.pripass)
                        root.quit() #note root.destroy() frezze the code.
                    b = Button(root, text="submit", command=lambda: getinput())
                    b.grid(row=0, column=2)
                    ent.bind('<Return>', lambda e:getinput())
                    root.mainloop()
                    root.destroy() #after quiting the loop we can safely destroy the window
                    try:
                        self.prikey = serialization.load_pem_private_key(self.prikey,password=self.pripass)#check if the given password is correct
                    except ValueError:
                        print("incorrect password\n")
                    else:
                        break
                elif int(rep) == 2:
                    return self.getkey("pri")#ask for another key
                elif int(rep) == 3:
                    self.abort = True #option 3 abort and return to the menu
                    return
        except ValueError: #cheks if the given file is valid
            print("invalid key!")
            self.abort = True
        print("private key successfully loaded!\n")
    def prtcldecrypt(self): #protocol to decrypt
        print("to decrypt a message please select a private key")
        input("ready for selection press enter to continue\n")
        self.getkey("pri")#ask for a private key
        if self.abort:
            return self.menu() # goes back to the menu
        try:#check try to decrypt the file
            plaintext = self.prikey.decrypt(
                self.message,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
        except ValueError: #the given file is not ecrypted or the key is not the right one
            print("decryption failed\n")
            return self.menu() #goses back to the menu
        else: #if the decryption is a succes
            plaintext = plaintext.decode()
            print("decryption success!")
            print("what do you want to do with the decrypted message\n")
            while True:
                while True: #menu to ask what the user want to do with the message
                    print("1. display the message")
                    print("2. save as txt")
                    print("3.overwrite the file")
                    rep = input("$> ")
                    print("")
                    if int(rep) == 1:
                        print(plaintext,'\n') # dispay the message
                        self.end = True
                        return
                    elif int(rep) == 2:
                        Tk().withdraw()
                        f = asksaveasfile(mode='w', defaultextension=".txt") #open a dialog window to ask where he wants to save the file
                        f.write(plaintext) #write in the file
                        f.close() #closes the file
                        print("done!\n")
                        self.end = True
                        return
                    elif int(rep) == 3:
                        while True:
                            print("are you sure? (y/n)")#ask if the user is sure to overwrite the file
                            rep = input("$> ")
                            if rep == "y" or rep == "Y":
                                with open(self.mpath, "w") as f: f.write(plaintext) #overwite the file
                                print("done!\n")
                                self.end = True
                                return
                            elif rep == "n" or rep == "N":
                                break
    def prtclencrypt(self): #protocol for decryption
        print("to encrypt a message please select a public key")
        input("ready for selection press enter to continue\n")
        self.getkey("pub")#ask for a public key
        if self.abort:
            return
        ciphertext = self.pubkey.encrypt(
            self.message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        print("encryption success!")
        while True:
            print("what do you want to do?")
            print("1. save as")
            print("2. overwrite")
            rep = input("$> ")
            print("")
            if int(rep)== 1:
                Tk().withdraw()
                f=asksaveasfile(mode="wb",defaultextension=".txt")#ask where the user whant to save the file
                f.write(ciphertext)
                f.close()
                print("done!")
                self.end = True
                return
            elif int(rep) == 2:
                while True:
                    print("are you sure? (y/n)")#ask if the user is sure to overwrite
                    rep = input("$> ")
                    if rep == "Y" or rep == "y":
                        with open(self.mpath, "wb") as f: f.write(ciphertext)#ovewrite the file
                        print("done!\n")
                        self.end = True
                        return
                    elif rep == "N" or rep == "n":
                        break
def start():#starting function
    print("please select a file that you want to encrypt/decrypt")
    input("ready for selection press enter to open the window! \n")
    Tk().withdraw()
    filename = askopenfilename()#ask a file to operate to the user
    with open(filename, "rb") as f : message = f.read()#read the bites of the files
    decrypt = msg(message,filename)#create the class
    decrypt.menu()#call the menu