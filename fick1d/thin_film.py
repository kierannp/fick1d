from numpy import exp,pi,sin,array,linspace, zeros, sqrt
from scipy.special import erf
from warnings import filterwarnings

filterwarnings("error")

def thin_film(T, X, D, c0, b, xstep = 1000 ):
    ''' 
    T: list ints of times to sample
    X: 
    rstep: step size for r range
    D: Diffusivity 
    c1: initial concentration
    c0: constant conentration at surface
    '''
    total = zeros((len(T), xstep))
    for count_t,t in enumerate(T):
        if t == 0:
            b_size = int((b/(2*X)) * xstep)
            start = int(xstep/2 - b_size/2)
            stop = int(xstep/2 + b_size/2)
            total[0,start:stop] = c0
        else:
            for count_x,x in enumerate(linspace(-X,X,xstep)):
                total[count_t,count_x] = c0*(b/2)*exp(-x**2/(4*D*t))/sqrt(pi*D*t)
    return total
# def both_thin(T, Xlow, Xhi, D, c0, cb, b, xstep = 1000):
#     tCrit=((2/b)**-2)/(pi*D)
#     total = zeros((len(T), xstep))
#     for count_t, t in enumerate(T):
#         if t<tCrit:
#             for count_x, x in enumerate(linspace(Xlow, Xhi, xstep)):
#                 total[count_t, count_x] = (cb/2)*(1-erf((x-.05)/sqrt(4*D*t)))
#         else:
#             for count_x, x in enumerate(linspace(Xlow, Xhi, xstep)):
#                 total[count_t, count_x] = c0 * (b/2)*exp(-x**2/(4*D*t))/sqrt(pi*D*t)

#         return total,tCrit

def early_thin_film(T, D, X, cs, c0, xstep = 1000, Xoff = 0):
    total_pos = zeros((len(T), xstep))
    total_neg = total_pos
    for count_t, t in enumerate(T):
        for count_x, x in enumerate(linspace(-X, X, xstep)):
            total_pos[count_t, count_x] = (c0-cs)*(erf((x+1)/sqrt(4*D*t)))+cs
    for count_t, t in enumerate(T):
        for count_x, x in enumerate(linspace(-X, X, xstep)):
            total_neg[count_t, count_x] = -(c0-cs)*(erf((x-1)/sqrt(4*D*t)))+cs
    return total_pos, total_neg
