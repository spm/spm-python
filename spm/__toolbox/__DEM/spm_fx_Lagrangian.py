from spm.__wrap__ import _Runtime


def spm_fx_Lagrangian(*args, **kwargs):
  """  FORMAT [f] = spm_fx_Lagrangian(P,M,U)  
     
    flow subfunction for Langrangian demo  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DEM/spm_fx_Lagrangian.m)
  """

  return _Runtime.call("spm_fx_Lagrangian", *args, **kwargs)
