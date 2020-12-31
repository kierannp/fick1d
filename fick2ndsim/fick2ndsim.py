import matplotlib.patches as mpatches
import numpy as np
import matplotlib.pyplot as plt
from seaborn import set
import scipy.special
set()


def thin_film(T,X,D,c0,b,tnum,xnum):
    total = np.zeros((tnum, xnum))
    for count_t,t in enumerate(np.linspace(0,T,tnum)):
        for count_x,x in enumerate(np.linspace(-X,X,xnum)):
            total[count_t,count_x]=c0*(b/2)*np.exp(-x**2/(4*D*t))/np.sqrt(np.pi*D*t)
    return np.linspace(-X,X,xnum),total

def erf_sol(T,Xlow,Xhi,cb,D,xstep,tstep,yoff):
    total = np.zeros((tstep, xstep))
    for count_t,t in enumerate(np.linspace(0,T,tstep)):
        for count_x,x in enumerate(np.linspace(Xlow,Xhi,xstep)):
            total[count_t,count_x]=(cb/2)*(1+scipy.special.erf(x/np.sqrt(4*D*t)))+yoff
    return np.linspace(Xlow, Xhi, xstep),total

def series_sphere_mean(T,N,R,tstep,D,cf,ci):
    total=np.zeros((tstep))
    for count_t,t in enumerate(np.linspace(T/tstep,T+T/tstep,tstep)):
        sum=0
        for n in range(1,N+1):
            sum += (np.exp(-D*t*((n*np.pi)/R)**2))/n**2
        total[count_t]=sum
    return np.linspace(T/tstep,T+T/tstep,tstep), (cf-ci)*(1-(6/np.pi**2)*total)+ci

def erf_thin(T, Xlow,Xhi, D, c0, b, tnum, xnum,cb,yoff):
    
    tCrit=((2/b)**-2)/(np.pi*D)
    
    total = np.zeros((tnum, xnum))

    for count_t, t in enumerate(np.linspace(0,T,tnum)):
        if t<tCrit:
            for count_x, x in enumerate(np.linspace(Xlow, Xhi, xnum)):
                total[count_t, count_x] = (cb/2)*(1-scipy.special.erf((x-.05)/np.sqrt(4*D*t)))+yoff
        else:
            for count_x, x in enumerate(np.linspace(Xlow, Xhi, xnum)):
                total[count_t, count_x] = c0 * (b/2)*np.exp(-x**2/(4*D*t))/np.sqrt(np.pi*D*t)+yoff

    return np.linspace(Xlow,Xhi,xnum), total,tCrit

def erf_sol_series(T, Xlow, Xhi, cs,c0, D, xstep, tstep,Xoff):
    total = np.zeros((tstep, xstep))
    for count_t, t in enumerate(np.linspace(0, T, tstep)):
        for count_x, x in enumerate(np.linspace(Xlow, Xhi, xstep)):
            total[count_t, count_x] = (c0-cs)*(scipy.special.erf((x+1)/np.sqrt(4*D*t)))+cs
    
    total2 = np.zeros((tstep, xstep))
    for count_t, t in enumerate(np.linspace(0, T, tstep)):
        for count_x, x in enumerate(np.linspace(Xlow, Xhi, xstep)):
            total2[count_t, count_x] = -(c0-cs)*(scipy.special.erf((x-1)/np.sqrt(4*D*t)))+cs
    return np.linspace(Xlow, Xhi, xstep), total,total2

def series_slab(T,N,Xlow,Xhi,xstep,tstep,D,h,ci,cf,Xoff):
    total=np.zeros((tstep,xstep))
    for count_t,t in enumerate(np.linspace(0,T,tstep)):
        for count_x,x in enumerate(np.linspace(Xlow,Xhi,xstep)):
            sum=0
            for n in range(N):
                sum += np.exp((-D*t*((((2*n+1)*np.pi)/h)**2)))*(np.sin(((2*n+1)*np.pi*(x-Xoff))/h)/(2*n+1))
            total[count_t,count_x]=sum
    return np.linspace(Xlow,Xhi,xstep), (cf-ci)*(1-(4/np.pi)*total)+ci
