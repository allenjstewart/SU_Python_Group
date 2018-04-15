def trapezoid(f,a, b, n):
    h = (b-a)/n
    s=f(a)+f(b)

    for i in range(1,n):
        s+= 2*f(a+i*h)
    return s*h/2
