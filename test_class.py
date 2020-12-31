
import fick1d.slab as slab
import fick1d.couple as couple
import fick1d.sphere as sphere
import fick1d.thin_film as thin_film
import fick1d.cylinder as cylinder

d = 1.88e-6

class TestClass:
    def test_sphere(self):
        sphere.sphere( [500], 1, d, 0, .5)
        sphere.mean([500], 1, d, 0, .5)
    def test_slab(self):
        slab.slab([500], 0, 1, d, .1, 0, .5)
        slab.mean([500], d, .1, 0, .5)
    def test_cylinder(self):
        cylinder.cylinder([500], 1, d, 0, .5)
    def test_couple(self):
        couple.couple([500], -.5, .5, 1, d)
    def test_thin_film(self):
        thin_film.thin_film([500], .5, d, 1, .01)
        thin_film.early_thin_film([500], -.5, .5, 1, .2, d)
        # thin_film.both_thin()
