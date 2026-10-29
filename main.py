import student
while True:
    print("_______________student desboard_____________________")
    print("1:singup")
    print("2:login")  
    print("3:search")    
    print("4:exit")
    
    ch=int(input("enter your choice: "))

    if ch==1:
        student.singup()
    elif ch==2:
        student.login()  
    elif ch==3:
        student.search()
    elif ch==4:
        print("exit")
        break
    else:
        print("=======invalid==========")  