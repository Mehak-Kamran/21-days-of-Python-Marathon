# Password Manager + Encryption

masterpass=input("Enter your Master password:  ")

def add():
    name=input("Enter your name: ")
    paswd=input("Enter your password: ")
    with open("passwordManager/password.txt","a") as f:
        f.write(name +"|"+ paswd+"\n")

def view():
   




while True:
    mode=input("You want to view passwords or add a new password? (v/a) OR wanna quit? (q)")
    if mode=="q":
       break
    elif mode=="v":
       #view()
       pass
    elif mode=='a':
       add()
    else:
       print("Enter a valid mode please")
       continue
