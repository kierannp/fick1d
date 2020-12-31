from numpy import exp,pi,sin,array,linspace, zeros

def slab( T, Xlow, Xhi, D, h, ci, cf, Xoffset = 0, tol = .00001, xstep = 1000):     
    ''' 
    T :list ints of times to sample
    Xlow: x start
    Xhi: x end
    xstep: step size for x range
    D: Diffusivity 
    h: Plate Thickness
    ci: initial concentration
    cf: constant conentration at interface
    Xoffset: Staggering of x values
    tol : .1% auto tolerance 
    '''

    total = zeros((len(T),xstep))
    for count_t,t in enumerate(T):
        for count_x,x in enumerate(linspace(Xlow,Xhi,xstep)):
            n = 0
            term = exp((-D*t*((((2*n+1)*pi)/h)**2)))*(sin(((2*n+1)*pi*(x-Xoffset))/h)/(2*n+1))
            curr_sum = term
            while( abs(term) > tol and curr_sum < ci):
                n += 1
                term = exp((-D*t*((((2*n+1)*pi)/h)**2)))*(sin(((2*n+1)*pi*(x-Xoffset))/h)/(2*n+1))
                curr_sum += term
            total[count_t,count_x] = curr_sum
    return (cf-ci)*(1-(4/pi)*total)+ci

def mean( T, D, h, ci, cf, tol = .001): 
    ''' 
    T :list ints of times to sample in seconds
    D: Diffusivity in m^2/sec
    h: Plate Thickness in m
    ci: initial concentration in m^2/sec
    cf: constant conentration at interface in m^2/sec
    tol : .1% auto tolerance 
    '''

    total = []
    for count_t,t in enumerate(T):
        n = 0
        term = exp((-D*t*((((2*n+1)*pi)/h)**2)))*((2*n+1)**-2)
        first_term = term
        sum = first_term
        while (term/first_term) > tol:
            n += 1
            term = exp((-D*t*((((2*n+1)*pi)/h)**2)))*((2*n+1)**-2)
            sum += term
        total.append(sum)
    total = array(total)
    return  (cf-ci)*(1-(8/pi**2)*total)+ci
