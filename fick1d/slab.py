from numpy import exp,pi,sin,array,linspace, zeros
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('error')

def sum_value(args, tol, fun):
    n = 0
    curr_sum = 0
    args['n'] = n
    while(True):
        term = fun(args)
        prev_sum = curr_sum
        curr_sum += term
        n += 1
        args['n'] = n
        try:
            delta = abs(prev_sum - curr_sum) 
        except:
            break
        if (delta < tol) :
            break
    return curr_sum

def slab( T, h, D, ci, cf, Xoffset = 0, tol = 1e-8, xstep = 1000):    
    ''' 
    T :list ints of times to sample
    xstep: step size for x range
    D: Diffusivity 
    h: Plate Thickness
    ci: initial concentration
    cf: constant conentration at interface
    Xoffset: Staggering of x values
    tol : .1% auto tolerance 
    '''
    def series_slab(d):
        return  exp((-d['D']*t*((((2*d['n']+1)*pi)/d['h'])**2)))*(sin(((2*d['n']+1)*pi*(d['x']-d['Xoffset']))/d['h'])/(2*d['n']+1)) 

    total = zeros((len(T),xstep))
    for count_t,t in enumerate(T):
        for count_x,x in enumerate(linspace(0,h,xstep)):
            dic = {'D' : D, 't' : t, 'x' : x, 'h' : h, 'Xoffset' : Xoffset}
            total[count_t,count_x] = sum_value(dic, tol = tol, fun = series_slab)
    return (cf-ci)*(1-(4/pi)*total)+ci

def mean( T, h, D, ci, cf, tol = 1e-8): 
    ''' 
    T :list ints of times to sample in seconds
    D: Diffusivity in m^2/sec
    h: Plate Thickness in m
    ci: initial concentration in wt% i.e. 8% would be entered as 8
    cf: constant concentration in wt% i.e. 8% would be entered as 8
    tol : .1% auto tolerance 
    '''
    def slab_mean(d):
        return exp((-d['D']*d['t']*((((2*d['n']+1)*pi)/d['h'])**2)))*((2*d['n']+1)**-2)

    total = []
    for count_t,t in enumerate(T):
        dic = {'D' : D, 't' : t, 'h' : h}
        total.append(sum_value(dic, tol = tol, fun = slab_mean))
    total = array(total)
    return  (ci-cf)*(1-(8/pi**2)*total)+cf
