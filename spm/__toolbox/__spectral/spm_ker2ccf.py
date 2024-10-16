from spm.__wrapper__ import Runtime


def spm_ker2ccf(*args, **kwargs):
  """  computes cross covariance function from kernels  
    FORMAT [ccf,pst] = spm_ker2ccf(ker,dt)  
     
    ker  - first-order (Volterra) kernels  
    dt   - time bin (sec)  
     
    ccf  - cross covariance functions  
    pst  - time samples  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/spectral/spm_ker2ccf.m)
  """

  return Runtime.call("spm_ker2ccf", *args, **kwargs)
