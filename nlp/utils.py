import time

def print_help(res):
    if isinstance(res, list):
        for item in res[:min(10,len(res))]:
            print item
    elif isinstance(res, dict):
        for k, v in res:
            print k, v
    else:
        print res

def deco(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time)*1000
        print_help(res)
        print("time is %d ms" %execution_time)
    return wrapper

@deco
def f(a,b):
    print("be on")
    time.sleep(1)
    print("result is %d" %(a+b))

@deco
def f2(a,b,c):
    print("be on")
    time.sleep(1)
    print("result is %d" %(a+b+c))

if __name__ == '__main__':
    f2(3,4,5)
    f(3,4)
