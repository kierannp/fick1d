# Fick2ndSimulate
The purpose of this repo is to one day create a python library

Structure of module

fick2ndsim.slab

slab thin sphere

Ficks second law of diffusion in one-dimension is defined as:

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;C}{\partial&space;t}=D\frac{\partial^2&space;C}{\partial&space;x^2}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;C}{\partial&space;t}=D\frac{\partial^2&space;C}{\partial&space;x^2}" title="\frac{\partial C}{\partial t}=D\frac{\partial^2 C}{\partial x^2}" /></a>


<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{C_x-C_0}{C_0-C_b}=1-erf(\frac{x}{2&space;\sqrt{Dt}&space;})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{C_x-C_0}{C_0-C_b}=1-erf(\frac{x}{2&space;\sqrt{Dt}&space;})" title="\frac{C_x-C_0}{C_0-C_b}=1-erf(\frac{x}{2 \sqrt{Dt} })" /></a>

Thin Film:

<a href="https://www.codecogs.com/eqnedit.php?latex=\large&space;c(x,t)=\frac{N}{\sqrt{4\pi&space;Dt}&space;}&space;exp({\frac{-x^2}{4Dt}})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\large&space;c(x,t)=\frac{N}{\sqrt{4\pi&space;Dt}&space;}&space;exp({\frac{-x^2}{4Dt}})" title="\large c(x,t)=\frac{N}{\sqrt{4\pi Dt} } exp({\frac{-x^2}{4Dt}})" /></a>

