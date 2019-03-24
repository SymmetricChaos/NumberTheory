## Generator that returns the fibonacci numbers
def fibonacci(n=0):
    a = 0
    b = 1
    
    # If 0 numbers are requested just go forever
    if n == 0:
        while True:
            a, b = b, a+b
            yield a
    
    # Otherwise return that many
    else:
        for i in range(n):
            a, b = b, a+b
            yield a
