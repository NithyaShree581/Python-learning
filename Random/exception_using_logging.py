import logging 
logging.basicConfig(level=logging.INFO)
a=10
b=0
try: 
    res=a/b
    print(res)
    logging.info("Division Successful")
except ZeroDivisionError:
    logging.exception("The error has been occured")

    

