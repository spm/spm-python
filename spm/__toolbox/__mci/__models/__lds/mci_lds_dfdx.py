from spm.__wrap__ import _Runtime


def mci_lds_dfdx(*args, **kwargs):
  """  Jacobian for linear system, dx/dt=Ax, with constrained connectivity  
    FORMAT [A,Pt] = mci_lds_dfdx (x,u,P,M)  
     
    x     State vector  
    u     input  
    P     parameters (vectorised)  
    M     model structure  
     
    A     f=Ax  
    Pt    Parameters (transformed from latent pars)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/lds/mci_lds_dfdx.m)
  """

  return _Runtime.call("mci_lds_dfdx", *args, **kwargs)
