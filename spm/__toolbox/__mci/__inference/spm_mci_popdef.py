from spm.__wrapper__ import Runtime


def spm_mci_popdef(*args, **kwargs):
  """  Set default parameters for population MCMC  
    FORMAT [mh] = spm_mci_popdef (scale,tune,samp)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_popdef.m)
  """

  return Runtime.call("spm_mci_popdef", *args, **kwargs)
