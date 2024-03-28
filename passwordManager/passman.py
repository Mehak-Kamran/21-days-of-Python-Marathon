# Password Manager + Encryption
#pip install cryptography

from cryptography.fernet import  Fernet

masterpass=input("Enter your Master password:  ")

def keydef():
   key = Fernet.generate_key()
   with open("key.key","wb") as f:#write in bytes
      f.write(key)


def add():
    name=input("Enter your name: ")
    paswd=input("Enter your password: ")
    with open("passwordManager/password.txt","a") as f:
        f.write(name +"|"+ paswd+"\n")

def view():
   with open("passwordManager/password.txt","r") as f:
      for line in f.readlines():
         data=line.rstrip()
         name,paswd=data.split("|")
         print("name:",name,"password:",paswd)

         
         

       





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
