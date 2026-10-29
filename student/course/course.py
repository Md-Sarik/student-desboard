def course():
    print("1. full stack web development")
    print("2. data science")
    print("3. mobile app development")
    print("4. cloud computing")
    print("5. artificial intelligence")
    print("6. course nahi hai")
    ch=int(input("enter your choice: "))
    # sab jeght course name return karna hai

    if ch==1:
        return "full stack web development"
    elif ch==2:
        return "data science"
    elif ch==3:
        return "mobile app development"
    elif ch==4:
        return "cloud computing"
    elif ch==5:
        return "artificial intelligence"
    elif ch==6:
        return "course nahi hai"
    
    