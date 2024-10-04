from spm.__wrap__ import _Runtime


def spm_fx_adem_salience(*args, **kwargs):
  """  returns the flow for oculomotor search  
    FORMAT [f]= spm_fx_adem_salience(x,v,a,P)  
     
    x    - hidden states:  
      x(1) - oculomotor angle  
      x(2) - oculomotor angle  
     
    v    - hidden cause  
    P    - parameters  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_fx_adem_salience.m)
  """

  return _Runtime.call("spm_fx_adem_salience", *args, **kwargs)
