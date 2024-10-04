from spm.__wrap__ import _Runtime


def mci_nmm_r2_gx(*args, **kwargs):
  """  Observation function for 2-region NMM  
    FORMAT [y,L] = mci_nmm_r2_gx (x,u,P,M)  
     
    P         Parameters  
    M         Model structure  
    U         Inputs  
     
    y         Output  
    L         Lead field (dy/dx)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/nmm/mci_nmm_r2_gx.m)
  """

  return _Runtime.call("mci_nmm_r2_gx", *args, **kwargs)
