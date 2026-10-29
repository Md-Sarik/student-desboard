import datetime
from ..validation.validation import validation_email
from ..filehandling import *
from..course.course import course
from..log.log import log_error
import uuid
def singup():
    try:    
        dict={}
        # dict["id"]=input("enter your id: ")
        dict["id"]=uuid.uuid4().hex[:4]
        # print(studentsid)
        validation_email(dict)
        dict["mobile_number"]=input("enter your contect number")
        qualification = []
        while True:
            q = input("enter your qualification: ")
            qualification.append(q)
            choice = input("add qualification?(y/n): ")
            if choice.lower() == "n":
                break
        dict["qualification"] = qualification
        dict["course"] = course()
        now = datetime.datetime.now()
        date = now.strftime("%d/%m/%Y")
        dict["date"] = date
        data=getdata()
        data.append(dict)
        putdata(data)
    except Exception as e:
        log_error(e)   
        print("try again")
    else:
        print("succsesfull")
    finally:
        print("final done") 
        
    