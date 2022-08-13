def trace(fn):
    def traced(x):
            print("calling", fn, "on argument", x)
            return fn(x)
    return traced
 
@trace
def square(x):
    return(x*x)
