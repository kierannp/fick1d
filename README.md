# Fick2ndSimulate
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