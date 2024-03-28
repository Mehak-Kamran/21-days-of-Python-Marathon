# Password Manager + Encryption
#pip install cryptography

from cryptography.fernet import Fernet

'''def keydef():
   key = Fernet.generate_key()
   with open("passwordManager/key.key","wb") as f:#write in bytes
      f.write(key)'''

#keydef()


def loadkey():
  file= open("passwordManager/key.key","rb")
  key=file.read()
  file.close()
  return key



key=loadkey()
fer=Fernet(key)



def add():
    name=input("Enter your name: ")
    paswd=input("Enter your password: ")
    with open("passwordManager/password.txt","a") as f:
        f.write(name +"|"+ fer.encrypt(paswd.encode()).decode()+"\n")

def view():
   with open("passwordManager/password.txt","r") as f:
      for line in f.readlines():
         data=line.rstrip()
         name,paa=data.split("|")
         print("name:",name,"password:", fer.decrypt(paa.encode()).decode())



while True:
    mode=input("You want to view passwords or add a new password? (v/a) OR wanna quit? (q)")
    if mode=="q":
       break
    elif mode=="v":
       view()
       
    elif mode=='a':
       add()
    else:
       print("Enter a valid mode please")
       continue
