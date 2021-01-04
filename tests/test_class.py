import fick1d
import matplotlib.pyplot as plt
from numpy import exp,pi,sin,array,linspace, zeros
from seaborn import set
set()

d = 1.88e-5
x = .1
t = [0,10,50,100,1000]

def plot_results( result, fun, size, T, symx = False):
    if symx:
        for i in range(len(T)):
            plt.title(fun)
            plt.plot(linspace(-size,size,1000),result[i],label = str(T[i]) ) 
    else:
        for i in range(len(T)):
            plt.title(fun)
            plt.plot(linspace(0,size,1000),result[i],label = str(T[i]) ) 
    plt.legend()
    plt.xlabel("distance (meters)")
    plt.ylabel("conentration (wt%)")
    plt.savefig(fun + ".png")
    plt.close()

class TestClass:
    def test_sphere(self):
        results = fick1d.sphere.sphere( t, x, d, 0, 0.1)
        plot_results(results,"sphere.sphere", x, t)
        results = fick1d.sphere.mean(t, x, d, .1, 0)
    def test_slab(self):
        results = fick1d.slab.slab(t, x, d, .8, 0)
        plot_results(results,"slab.slab", x, t)
        results = fick1d.slab.mean(t, x, d, .8, 0)
    def test_cylinder(self):
        results = fick1d.cylinder.cylinder(t, x, d, 0, .5)
        plot_results(results, "cylinder.cylinder", x, t)
    def test_couple(self):
        results = fick1d.couple.couple(t, d, -.5, .5, x)
        plot_results(results, "couple.couple", .5, t, symx = True)
    def test_thin_film(self):
        results = fick1d.thin_film.thin_film(t, x, d, 1, .01)
        plot_results(results,"thin_film.thin_film", x, t, symx = True)
        # thin_film.early_thin_film([0,10,100,1000], -.5, .5, 1, .2, d)
        # thin_film.both_thin()