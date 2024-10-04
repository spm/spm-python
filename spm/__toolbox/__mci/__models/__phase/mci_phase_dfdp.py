from spm.__wrap__ import _Runtime


def mci_phase_dfdp(*args, **kwargs):
  """  Parameter sensitivity for phase model  
    FORMAT [dfdp] = mci_phase_dfdp (x,u,P,M)  
     
    x      State vector  
    u      inputs  
    P      parameter vector  
    M      model structure  
     
    dfdp   Jacobian wrt. parameters, df/dp  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/phase/mci_phase_dfdp.m)
  """

  return _Runtime.call("mci_phase_dfdp", *args, **kwargs)
