from spm.__wrap__ import _Runtime


def spm_ker2mtf(*args, **kwargs):
  """  computes modulation transfer function from kernels  
    FORMAT [mtf,Hz] = spm_ker2mtf(ker,dt)  
     
    ker  - first-order (Volterra) kernels  
    dt   - time bin  
     
    mtf  - modulation transfer function  
    Hz   - frequencies  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/spectral/spm_ker2mtf.m)
  """

  return _Runtime.call("spm_ker2mtf", *args, **kwargs)
