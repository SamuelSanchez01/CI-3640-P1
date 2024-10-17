import math

def tribo(n):
    if n < 3:
        return n
    else: 
        return (tribo(n-1) + tribo(n-2) + tribo(n-3))
    

def naraLog(n):
    log = math.floor(math.log2(n))
    
    x = math.factorial(n) *  math.factorial(n) / (
        math.factorial(log) * math.factorial(n-log)
        * math.factorial(log-1) * math.factorial(n-log+1)
        * n
    )

    return tribo(math.floor(math.log2(x)) + 1)

for i in range(2,51):
    print(f'{i}: {naraLog(i)}')