from spm.__wrap__ import _Runtime


def spm_mci_glike_deriv(*args, **kwargs):
  """  Gradient of Gaussian Log-likelihood   
    FORMAT [dLdp,iCpY,st,L] = spm_mci_glike_deriv (P,M,U,Y)  
     
    P         Parameters  
    M         Model structure  
    U         Inputs  
    Y         Data  
      
    dLdP      Gradient of Log Likelihood wrt params, [1 x Np]  
    iCpY      Curvature (Fisher Information)  
    st        status flag (0 for OK, -1 for problem)  
    L         Log Likelihood  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_glike_deriv.m)
  """

  return _Runtime.call("spm_mci_glike_deriv", *args, **kwargs)
