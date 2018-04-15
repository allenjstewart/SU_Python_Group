def simpson(f,a, b, n):
    if n % 2:
        raise ValueError("n must be even (received n=%d)" % n)
    
    h = (b-a)/n
    s=f(a)+f(b)

    for i in range(1,n,2):
        s+= 4*f(a+i*h)
    for i in range(2,n,2):
        s+= 2*f(a+i*h)
    return s*h/3
