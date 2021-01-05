from numpy import exp,pi,sin,array,linspace, zeros

def sum_value(args, tol, fun):
    n = 1
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

def mean(T, R, D, c1, c0, tol = 1e-8):
    ''' 
    T :list ints of times to sample
    R: Sphere Radius
    D: Diffusivity 
    c1: initial concentration
    c0: constant conentration at surface
    tol : .1% auto tolerance 
    '''
    def sphere_mean(d):
        return  (exp(-d['D']*d['t']*((d['n']*pi)/d['R'])**2))/d['n']**2

    total = zeros((len(T)))
    for count_t,t in enumerate(T):
        dic = {'D' : D, 't' : t, 'R' : R}
        total[count_t] = sum_value(dic, tol = tol, fun = sphere_mean)
    return (c0-c1)*(1 + 2*total) + c1

def sphere( T, R, D, c1, c0, tol = 1e-8, rstep = 1000):     
    ''' 
    T: list ints of times to sample
    R: Sphere Radius
    rstep: step size for r range
    D: Diffusivity 
    c1: initial concentration
    c0: constant conentration at surface
    tol : .1% auto tolerance 
    '''
    def sphere_series(d):
        return ( ((-1)**d['n'])/d['n'] ) * sin((d['n']*pi*x)/d['R']) * exp((-d['D']*(d['n']**2)*(pi**2)*t)/(d['R']**2) )
    def sphere_center(d):
        return ((-1)**d['n'] * exp((-d['D']*(d['n']**2)*(pi**2)*t)/(d['R']**2) ))
    total = zeros((len(T),rstep))
    for count_t,t in enumerate(T):
        if t == 0:
            total[0,rstep-1] = c0
        else:
            for count_x,x in enumerate(linspace(0,R,rstep)):
                if x ==0:
                    dic = {'D' : D, 't' : t, 'x' : x, 'R' : R}
                    total[count_t,0] = (c0-c1)*(1 + 2*sum_value(dic, tol = tol, fun = sphere_center)) + c1
                else:
                    dic = {'D' : D, 't' : t, 'x' : x, 'R' : R}
                    total[count_t,count_x] = (c0-c1)*(1 + ((2*R)/(pi))*sum_value(dic, tol = tol, fun = sphere_series) / x) + c1
    return total
