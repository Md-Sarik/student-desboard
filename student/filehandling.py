import json
from .log.log import log_error
def getdata():
    try:
        with open("student/data/data.json","r") as f:
            data=json.load(f)
            return data
    except Exception as e:
        log_error(e)
        print("try again")

def putdata(data):
    try:
        with open("student/data/data.json","w") as f:
            json.dump(data,f,indent=2)
    except Exception as e:
        log_error(e)
        print("try again")
    else:
        print("sccessfully")
    finally:
        print("final done")
