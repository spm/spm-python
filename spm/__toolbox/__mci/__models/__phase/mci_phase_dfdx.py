from spm.__wrap__ import _Runtime


def mci_phase_dfdx(*args, **kwargs):
  """  State sensitivity for phase model  
    FORMAT [dfdx] = mci_phase_dfdx (x,u,P,M)  
     
    x      state vector  
    M      model structure  
    P      parameter vector  
     
    dfdx   Jacobian wrt states  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/phase/mci_phase_dfdx.m)
  """

  return _Runtime.call("mci_phase_dfdx", *args, **kwargs)
