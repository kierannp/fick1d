
import fick1d.slab as slab
import fick1d.couple as couple
import fick1d.sphere as sphere
import fick1d.thin_film as thin_film
import fick1d.cylinder as cylinder
import matplotlib.pyplot as plt
from numpy import exp,pi,sin,array,linspace, zeros

d = 1.88e-5
x = .1
def plot_results(result,fun,size,symx = False):
    if symx:
        for i in range(4):
            plt.title(fun)
            plt.plot(linspace(-size,size,1000),result[i]) 
    else:
        for i in range(4):
            plt.title(fun)
            plt.plot(linspace(0,size,1000),result[i]) 
    plt.savefig(fun + ".png")
    plt.close()

class TestClass:
    def test_sphere(self):
        results = sphere.sphere( [0,10,100,1000], x, d, .10, 0)
        plot_results(results,"sphere.sphere", x)
        results = sphere.mean([0,10,100,1000], x, d, .1, 0)
    def test_slab(self):
        results = slab.slab([0,10,100,1000], x, d, .8, 0)
        plot_results(results,"slab.slab", x)
        results = slab.mean([0,10,100,1000], x, d, .8, 0)
    def test_cylinder(self):
        results = cylinder.cylinder([0,10,100,1000], x, d, 0, .5)
        plot_results(results, "cylinder.cylinder", x)
    def test_couple(self):
        results = couple.couple([0,10,100,1000], d, -.5, .5, x)
        plot_results(results, "cylinder.cylinder", .5, symx = True)
    def test_thin_film(self):
        results = thin_film.thin_film([0,10,100,1000], x, d, 1, .01)
        plot_results(results,"thin_film.thin_film", .5, symx = True)
        # thin_film.early_thin_film([0,10,100,1000], -.5, .5, 1, .2, d)
        # thin_film.both_thin()
