import numpy as np

def sphere_mean(T,N,R,tstep,D,cf,ci):
    total=np.zeros((tstep))
    for count_t,t in enumerate(np.linspace(T/tstep,T+T/tstep,tstep)):
        sum=0
        for n in range(1,N+1):
            sum += (np.exp(-D*t*((n*np.pi)/R)**2))/n**2
        total[count_t]=sum
    return np.linspace(T/tstep,T+T/tstep,tstep), (cf-ci)*(1-(6/np.pi**2)*total)+ci
