from spm.__wrapper__ import Runtime


def mci_linear_deriv(*args, **kwargs):
  """  Gradient of likelihood for linear regression  
    FORMAT [dLdp,iCpY,L] = mci_linear_deriv (P,M,U,Y)  
     
    P         parameters  
    M         model  
    U         inputs  
    Y         data  
     
    dLdp      gradient of log joint  
    iCpY      curvature (Fisher Information)  
    L         log joint  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/linear/mci_linear_deriv.m)
  """

  return Runtime.call("mci_linear_deriv", *args, **kwargs)
