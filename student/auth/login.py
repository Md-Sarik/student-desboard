from ..filehandling import *
def login():
    data=getdata()
    e=input("enter your email: ")
    p=input("enter your password: ")

    count=1
    for i in data:
        if e==i["email"] and p==i["password"]:
            count=0
            break
    if count==0:    
        print("__________login succesful______________")
        print(i)
    else:
        print("________invalid____________")
 