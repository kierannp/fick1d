from numpy import exp,pi,sin,array,linspace, zeros

def mean(T, R, D, c1, c0, tol = .00001):
    ''' 
    T :list ints of times to sample
    R: Sphere Radius
    D: Diffusivity 
    c1: initial concentration
    c0: constant conentration at surface
    tol : .1% auto tolerance 
    '''
    total=zeros((len(T)))
    for count_t,t in enumerate(T):
        sum=0
        for n in range(1,N+1):
            sum += (exp(-D*t*((n*pi)/R)**2))/n**2
        total[count_t] = sum
    return (c0-c1)*(1 + 2*total) + c1

def sphere( T, R, D, c1, c0, tol = .00001, rstep = 1000):     
    ''' 
    T: list ints of times to sample
    R: Sphere Radius
    rstep: step size for r range
    D: Diffusivity 
    c1: initial concentration
    c0: constant conentration at surface
    tol : .1% auto tolerance 
    '''
    total = zeros((len(T),rstep))
    for count_t,t in enumerate(T):
        for count_x,x in enumerate(linspace(0,R,rstep)):
            n = 0
            term = ( (-1)**n/n ) * sin((n*pi*x)/R) * exp(-D*n**2*pi**2*t/R**2)
            curr_sum = term
            while( abs(term) > tol):
                n += 1
                term = ( (-1)**n/n ) * sin((n*pi*x)/R) * exp(-D*n**2*pi**2*t/R**2)
                curr_sum += term
            total[count_t,count_x] = curr_sum
    return linspace(0,R,rstep), (c0-c1)*(1+((2*R)/(pi*x))*total)+c1
