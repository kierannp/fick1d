import numpy as np

def thin_film(T, X, D, c0, b, tnum, xnum, erf=False ):
    if erf:
        tCrit=((2/b)**-2)/(np.pi*D)
        total = np.zeros((tnum, xnum))
        for count_t, t in enumerate(np.linspace(0,T,tnum)):
            if t<tCrit:
                for count_x, x in enumerate(np.linspace(Xlow, Xhi, xnum)):
                    total[count_t, count_x] = (cb/2)*(1-erf((x-.05)/np.sqrt(4*D*t)))+yoff
            else:
                for count_x, x in enumerate(np.linspace(Xlow, Xhi, xnum)):
                    total[count_t, count_x] = c0 * (b/2)*np.exp(-x**2/(4*D*t))/np.sqrt(np.pi*D*t)+yoff

        return np.linspace(Xlow,Xhi,xnum), total,tCrit

    else:
        total = np.zeros((tnum, xnum))
        for count_t,t in enumerate(np.linspace(0,T,tnum)):
            for count_x,x in enumerate(np.linspace(-X,X,xnum)):
                total[count_t,count_x]=c0*(b/2)*np.exp(-x**2/(4*D*t))/np.sqrt(np.pi*D*t)
        return np.linspace(-X,X,xnum),total



    def early_thin_erf(T, Xlow, Xhi, cs,c0, D, xstep, tstep,Xoff):
        total = np.zeros((tstep, xstep))
        for count_t, t in enumerate(np.linspace(0, T, tstep)):
            for count_x, x in enumerate(np.linspace(Xlow, Xhi, xstep)):
                total[count_t, count_x] = (c0-cs)*(erf((x+1)/np.sqrt(4*D*t)))+cs
        
        total2 = np.zeros((tstep, xstep))
        for count_t, t in enumerate(np.linspace(0, T, tstep)):
            for count_x, x in enumerate(np.linspace(Xlow, Xhi, xstep)):
                total2[count_t, count_x] = -(c0-cs)*(erf((x-1)/np.sqrt(4*D*t)))+cs
        return np.linspace(Xlow, Xhi, xstep), total,total2
