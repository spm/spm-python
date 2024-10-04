from spm.__wrap__ import _Runtime


def spm_ker2csd(*args, **kwargs):
  """  computes cross spectral density from kernels  
    FORMAT [csd,Hz] = spm_ker2csd(ker,pst)  
     
    ker  - first-order (Volterra) kernels  
    pst  - time samples  
     
    csd  - cross spectral density  
    Hz   - frequencies  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/spectral/spm_ker2csd.m)
  """

  return _Runtime.call("spm_ker2csd", *args, **kwargs)
