from ..filehandling import*
def search():
    print("1:email search=")
    print("2:name search")
    print("3:course search")
    ch = int(input("enter your choice: "))

    if ch == 1:
        e = input("enter your email: ")
        data = getdata()
        for i in data:
            if i["email"] == e:
                print(i)
                break
        else:
            print("not found")
    elif ch == 2:
        n = input("enter your name: ")
        data = getdata()
        for i in data:
            if i ["name"] == n:
                print(i)
                break
        else:
            print("not found")
    if ch == 3:
        c = input("enter your course: ")
        data = getdata()
        for i in data:
            if i ["course"] == c:
                print(data)
                break
        else:
            print("not found")    
   