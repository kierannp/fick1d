from numpy import exp,pi,sin,array,linspace, zeros
from scipy.special import j0, j1, jn_zeros

def cylinder( T, R, D, c1, c0, tol = .00001, rstep = 1000):     
    ''' 
    T: list ints of times to sample
    R: Sphere Radius
    D: Diffusivity 
    c1: initial concentration
    c0: constant conentration at surface
    tol : .1% auto tolerance 
    rstep: step size for r range
    '''
    total = zeros((len(T),rstep))
    roots = jn_zeros(0, 50)
    for count_t,t in enumerate(T):
        for count_x,x in enumerate(linspace(0,R,rstep)):
            n = 0
            an = roots[n]
            term = ( exp(-D*an*t)*j0(x*an) ) / ( an*j1(R*an))
            curr_sum = term
            while( abs(term) > tol):
                n += 1
                an = roots[n]
                term = ( exp(-D*an**2*t)*j0(x*an) ) / ( an*j1(R*an))
                curr_sum += term
            total[count_t,count_x] = curr_sum
    return (c0-c1)*(1 - (2/R)*total)+c1