from numpy import exp,pi,sin,array,linspace, zeros
from scipy.special import j0, j1, jn_zeros


def sum_value(args, tol, fun, roots):
    n = 1
    curr_sum = 0
    an = roots[n]
    args['n'] = n
    args['an'] = an
    while(True):
        term = fun(args)
        prev_sum = curr_sum
        curr_sum += term
        n += 1
        an = roots[n]
        args['n'] = n
        args['an'] = an
        try:
            delta = abs(prev_sum - curr_sum) 
        except:
            break
        if (delta < tol or n > 98) :
            break
    return curr_sum


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
    def cylinder_series(d):
        return ( exp(-d['D']*(d['an']**2)*d['t'])*j0(d['x']*d['an']) ) / ( d['an']*j1(d['R']*d['an']))
    
    total = zeros((len(T),rstep))
    roots = jn_zeros(0, 100)
    for count_t,t in enumerate(T):
        for count_x,x in enumerate(linspace(0,R,rstep)):
            dic = {'D' : D, 't' : t, 'x' : x, 'R' : R}
            total[count_t,count_x] = sum_value(dic, tol = tol, fun = cylinder_series, roots = roots)
    return (c0-c1)*(1 - (2/R)*total)+c1