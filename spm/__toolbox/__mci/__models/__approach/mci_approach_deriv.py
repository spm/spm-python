from spm.__wrapper__ import Runtime


def mci_approach_deriv(*args, **kwargs):
  """  Gradient of log-likelihood for approach model  
    FORMAT [dLdp,iCpY,L] = mci_approach_deriv (P,M,U,Y)  
     
    dLdp      gradient of log joint  
    iCpY      curvature (Fisher Information)  
    L         log joint  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/models/approach/mci_approach_deriv.m)
  """

  return Runtime.call("mci_approach_deriv", *args, **kwargs)
