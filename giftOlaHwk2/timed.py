import time

def timeme(func):
    def wrapper():
       t1 = time.time()
       func()
       t2 = time.time()
       print ("Total time X",(t2-t1))
    return wrapper


