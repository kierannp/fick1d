import numpy as np
from scipy.special import erf

def thin_film(T, X, D, c0, b, xstep = 1000 ):
    ''' 
    T: list ints of times to sample
    X: 
    rstep: step size for r range
    D: Diffusivity 
    c1: initial concentration
    c0: constant conentration at surface
    '''
    total = np.zeros((len(T), xstep))
    for count_t,t in enumerate(T):
        for count_x,x in enumerate(np.linspace(-X,X,xstep)):
            total[count_t,count_x]=c0*(b/2)*np.exp(-x**2/(4*D*t))/np.sqrt(np.pi*D*t)
    return total
# def both_thin(T, Xlow, Xhi, D, c0, cb, b, xstep = 1000):
#     tCrit=((2/b)**-2)/(np.pi*D)
#     total = np.zeros((len(T), xstep))
#     for count_t, t in enumerate(T):
#         if t<tCrit:
#             for count_x, x in enumerate(np.linspace(Xlow, Xhi, xstep)):
#                 total[count_t, count_x] = (cb/2)*(1-erf((x-.05)/np.sqrt(4*D*t)))
#         else:
#             for count_x, x in enumerate(np.linspace(Xlow, Xhi, xstep)):
#                 total[count_t, count_x] = c0 * (b/2)*np.exp(-x**2/(4*D*t))/np.sqrt(np.pi*D*t)

#         return total,tCrit

def early_thin_film(T, D, X, cs, c0, xstep = 1000, Xoff = 0):
    total_pos = np.zeros((len(T), xstep))
    total_neg = total_pos
    for count_t, t in enumerate(T):
        for count_x, x in enumerate(np.linspace(-X, X, xstep)):
            total_pos[count_t, count_x] = (c0-cs)*(erf((x+1)/np.sqrt(4*D*t)))+cs
    for count_t, t in enumerate(T):
        for count_x, x in enumerate(np.linspace(-X, X, xstep)):
            total_neg[count_t, count_x] = -(c0-cs)*(erf((x-1)/np.sqrt(4*D*t)))+cs
    return total_pos, total_neg
