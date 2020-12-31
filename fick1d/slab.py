import numpy as np

def slab( T, Xlow, Xhi, D, h, ci, cf, Xoff = 0, tol = .001, xstep = 1000):     
    ''' 
    T :list ints of times to sample
    Xlow: x start
    Xhi: x end
    xstep: step size for x range
    D: Diffusivity 
    h: Plate Thickness
    ci: initial concentration
    cf: constant conentration at interface
    tol : .1% auto tolerance 
    '''

    total = np.zeros((len(T),xstep))
    for count_t,t in enumerate(T):
        for count_x,x in enumerate(np.linspace(Xlow,Xhi,xstep)):
            n = 0
            term = np.exp((-D*t*((((2*n+1)*np.pi)/h)**2)))*(np.sin(((2*n+1)*np.pi*(x-Xoff))/h)/(2*n+1))
            first_term = term
            sum = first_term
            while (term/first_term) > tol:
                n += 1
                term = np.exp((-D*t*((((2*n+1)*np.pi)/h)**2)))*(np.sin(((2*n+1)*np.pi*(x-Xoff))/h)/(2*n+1))
                sum += term
            total[count_t,count_x] = sum
    return np.linspace(Xlow,Xhi,xstep), (cf-ci)*(1-(4/np.pi)*total)+ci


def slab_mean( T, D, h, ci, cf, tol = .001): 
    ''' T :list ints of times to sample
    D: Diffusivity 
    h: Plate Thickness
    ci: initial concentration
    cf: constant conentration at interface
    tol : .1% auto tolerance '''

    total = []
    for count_t,t in enumerate(T):
        n = 0
        term = np.exp((-D*t*((((2*n+1)*np.pi)/h)**2)))*((2*n+1)**-2)
        first_term = term
        sum = first_term
        while (term/first_term) > tol:
            n += 1
            term = np.exp((-D*t*((((2*n+1)*np.pi)/h)**2)))*(np.sin(((2*n+1)*np.pi*(x-Xoff))/h)/(2*n+1))
            sum += term
        total.append(sum)
    total = np.array(total)
    return  (cf-ci)*(1-(8/np.pi**2)*total)+ci
