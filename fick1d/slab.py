import numpy as np

def slab( T, Xlow, Xhi, D, h, ci, cf, Xoff = 0, tol = .00001, xstep = 1000):     
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
            curr_sum = term
            while( abs(term) > tol and curr_sum < ci):
                n += 1
                term = np.exp((-D*t*((((2*n+1)*np.pi)/h)**2)))*(np.sin(((2*n+1)*np.pi*(x-Xoff))/h)/(2*n+1))
                curr_sum += term
            total[count_t,count_x] = curr_sum
    return np.linspace(Xlow,Xhi,xstep), (cf-ci)*(1-(4/np.pi)*total)+ci


def slab_mean( T, D, h, ci, cf, tol = .001): 
    ''' T :list ints of times to sample in seconds
    D: Diffusivity in m^2/sec
    h: Plate Thickness in m
    ci: initial concentration in m^2/sec
    cf: constant conentration at interface in m^2/sec
    tol : .1% auto tolerance '''

    total = []
    for count_t,t in enumerate(T):
        n = 0
        term = np.exp((-D*t*((((2*n+1)*np.pi)/h)**2)))*((2*n+1)**-2)
        first_term = term
        sum = first_term
        while (term/first_term) > tol:
            n += 1
            term = np.exp((-D*t*((((2*n+1)*np.pi)/h)**2)))*((2*n+1)**-2)
            sum += term
        total.append(sum)
    total = np.array(total)
    return  (cf-ci)*(1-(8/np.pi**2)*total)+ci



if __name__ == "__main__":
    import matplotlib.pyplot as plt
    results = slab(T = list(range(500)), Xlow = 0,Xhi = 1, D = 1.88e-5, h = 1, ci = .8, cf = 0.0)
    plt.plot(results[0],results[1][0])
    plt.show()
