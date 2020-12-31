# Fick1d
The purpose of this repo is to one day create a python module for simulating diffusion in solid state.


Usage:

import ficks1D

ficks1D.sphere
ficks1D.slab
ficks1D.cylinder


slab thin sphere

Ficks second law of diffusion in one-dimension is defined as:

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;C}{\partial&space;t}=D\frac{\partial^2&space;C}{\partial&space;x^2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;C}{\partial&space;t}=D\frac{\partial^2&space;C}{\partial&space;x^2}" title="\frac{\partial C}{\partial t}=D\frac{\partial^2 C}{\partial x^2}" /></a>


<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{C_x-C_0}{C_0-C_b}=1-erf(\frac{x}{2&space;\sqrt{Dt}&space;})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{C_x-C_0}{C_0-C_b}=1-erf(\frac{x}{2&space;\sqrt{Dt}&space;})" title="\frac{C_x-C_0}{C_0-C_b}=1-erf(\frac{x}{2 \sqrt{Dt} })" /></a>

Thin Film:

<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;c(x,t)=\frac{N}{\sqrt{4\pi&space;Dt}&space;}&space;exp({\frac{-x^2}{4Dt}})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\large&space;c(x,t)=\frac{N}{\sqrt{4\pi&space;Dt}&space;}&space;exp({\frac{-x^2}{4Dt}})" title="\large c(x,t)=\frac{N}{\sqrt{4\pi Dt} } exp({\frac{-x^2}{4Dt}})" /></a>


<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;\frac{c(x,t)-c_i}{c_f-c_i}=1-\frac{4}{\pi}&space;\sum_{n=0}^{&space;\infty}exp\left&space;(&space;-Dt(\frac{(2n&plus;1)\pi}{h})^2&space;\right&space;)\left&space;(&space;\frac{sin((2n&plus;1)\pi&space;x/h)}{2n&plus;1}&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\large&space;\frac{c(x,t)-c_i}{c_f-c_i}=1-\frac{4}{\pi}&space;\sum_{n=0}^{&space;\infty}exp\left&space;(&space;-Dt(\frac{(2n&plus;1)\pi}{h})^2&space;\right&space;)\left&space;(&space;\frac{sin((2n&plus;1)\pi&space;x/h)}{2n&plus;1}&space;\right&space;)" title="\large \frac{c(x,t)-c_i}{c_f-c_i}=1-\frac{4}{\pi} \sum_{n=0}^{ \infty}exp\left ( -Dt(\frac{(2n+1)\pi}{h})^2 \right )\left ( \frac{sin((2n+1)\pi x/h)}{2n+1} \right )" /></a>

If we restrict ourselves to cases in which the diffusion is radial, the diffusion
equation for a constant diffusion coefficient takes the form

Sphere:

<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;\frac{\partial&space;C}{\partial&space;t}=D\left&space;(&space;\frac{\partial^2&space;C}{\partial&space;r^2}&plus;\frac{2}{r}&space;\frac{\partial&space;C}{\partial&space;r}\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\large&space;\frac{\partial&space;C}{\partial&space;t}=D\left&space;(&space;\frac{\partial^2&space;C}{\partial&space;r^2}&plus;\frac{2}{r}&space;\frac{\partial&space;C}{\partial&space;r}\right&space;)" title="\large \frac{\partial C}{\partial t}=D\left ( \frac{\partial^2 C}{\partial r^2}+\frac{2}{r} \frac{\partial C}{\partial r}\right )" /></a>

Non-steady state diffusion with conditions where u = Cr and f(r) is the is the intitial distribution

u = 0, r = 0, t > 0
u = aC_0, r = a, t > 0
u = rf(r), t = 0, 0 < r < a




<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{C-C_1}{C_0-C_1}=1&plus;\frac{2a}{r\pi}\sum_{n=1}^{\infty}\frac{(-1)^n}{n}sin(\frac{n\pi&space;r}{a})exp(-Dn^2\pi^2&space;t/a^2)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{C-C_1}{C_0-C_1}=1&plus;\frac{2a}{r\pi}\sum_{n=1}^{\infty}\frac{(-1)^n}{n}sin(\frac{n\pi&space;r}{a})exp(-Dn^2\pi^2&space;t/a^2)" title="\frac{C-C_1}{C_0-C_1}=1+\frac{2a}{r\pi}\sum_{n=1}^{\infty}\frac{(-1)^n}{n}sin(\frac{n\pi r}{a})exp(-Dn^2\pi^2 t/a^2)" /></a>

Where,
C_1: intital uniform concentration
C_0: constant surface concentration
a: is radius of sphere

With the limit as r->0 i.e. the concentration at the center of the sphere

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{C-C_1}{C_0-C_1}=1&plus;2\sum_{n=1}^{\infty}(-1)^nexp(-Dn^2\pi^2&space;t/a^2)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{C-C_1}{C_0-C_1}=1&plus;2\sum_{n=1}^{\infty}(-1)^nexp(-Dn^2\pi^2&space;t/a^2)" title="\frac{C-C_1}{C_0-C_1}=1+2\sum_{n=1}^{\infty}(-1)^nexp(-Dn^2\pi^2 t/a^2)" /></a>


Cylinder:
With radial diffusion,

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;C}{\partial&space;t}=\frac{1}{r}\frac{\partial&space;}{\partial&space;r}\left&space;(&space;rD\frac{\partial&space;C}{\partial&space;r}&space;\right&space;)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;C}{\partial&space;t}=\frac{1}{r}\frac{\partial&space;}{\partial&space;r}\left&space;(&space;rD\frac{\partial&space;C}{\partial&space;r}&space;\right&space;)" title="\frac{\partial C}{\partial t}=\frac{1}{r}\frac{\partial }{\partial r}\left ( rD\frac{\partial C}{\partial r} \right )" /></a>

C = C_0, r = a, t >= 0 
C = f(r), 0 < r < a, t = 0,

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{C-C_1}{C_0-C_1}=1-\frac{2}{a}\sum_{n=1}^{\infty}\frac{exp(-D&space;\alpha_n^2&space;t)J_0(r&space;\alpha_n)}{\alpha_n&space;J_1(a&space;\alpha_n)}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{C-C_1}{C_0-C_1}=1-\frac{2}{a}\sum_{n=1}^{\infty}\frac{exp(-D&space;\alpha_n^2&space;t)J_0(r&space;\alpha_n)}{\alpha_n&space;J_1(a&space;\alpha_n)}" title="\frac{C-C_1}{C_0-C_1}=1-\frac{2}{a}\sum_{n=1}^{\infty}\frac{exp(-D \alpha_n^2 t)J_0(r \alpha_n)}{\alpha_n J_1(a \alpha_n)}" /></a>

Sources:
http://www-eng.lbl.gov/~shuman/NEXT/MATERIALS&COMPONENTS/Xe_damage/Crank-The-Mathematics-of-Diffusion.pdf
