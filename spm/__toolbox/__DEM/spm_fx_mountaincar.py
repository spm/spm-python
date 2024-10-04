from spm.__wrap__ import _Runtime


def spm_fx_mountaincar(*args, **kwargs):
  """  state equations for mountain car problem  
    FORMAT f = spm_fx_mountaincar(x,v,P)  
    FORMAT f = spm_fx_mountaincar(x,v,a,P)  
    FORMAT f = spm_fx_mountaincar(x,v,P,M)  
    x    - [x, x']  
    v    - exogenous force  
    a    - action  
     
    P.a  - 0th order coefficients of force  
    P.b  - 1st order coefficients of force  
    P.c  - 2nd order coefficients of force  
    P.d  - action coefficient  
     
    M    - model structure  
     
    f    - flow dx/dt  
     
    see:  
    Gaussian Processes in Reinforcement Learning  
    Carl Edward Rasmussen and Malte Kuss  
    Max Planck Institute for Biological Cybernetics  
    Spemannstraße 38, 72076 T¨ubingen, Germany  
    {carl,malte.kuss}@tuebingen.mpg.de  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_fx_mountaincar.m)
  """

  return _Runtime.call("spm_fx_mountaincar", *args, **kwargs)
