import numpy as np
from scipy.special import erf



def erf_sol(T,Xlow,Xhi,cb,D,xstep,tstep,yoff = 0):
    total = np.zeros((tstep, xstep))
    for count_t,t in enumerate(np.linspace(0,T,tstep)):
        for count_x,x in enumerate(np.linspace(Xlow,Xhi,xstep)):
            total[count_t,count_x]=(cb/2)*(1+erf(x/np.sqrt(4*D*t)))+yoff
    return np.linspace(Xlow, Xhi, xstep),total
