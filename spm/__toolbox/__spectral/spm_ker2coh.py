from spm.__wrap__ import _Runtime


def spm_ker2coh(*args, **kwargs):
  """  computes coherence from kernels  
    FORMAT [coh,fsd] = spm_ker2coh(ker,pst))  
     
    ker  - first-order (Volterra) kernels  
    pst  - time samples  
     
    coh  - coherence  
    fsd  - frequency specific delay (seconds)   
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/spectral/spm_ker2coh.m)
  """

  return _Runtime.call("spm_ker2coh", *args, **kwargs)
