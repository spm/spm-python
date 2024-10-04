from spm.__wrap__ import _Runtime


def spm_eeg_lapmtx(*args, **kwargs):
  """  Laplace transform basis set for ERPs  
    FORMAT [T] = spm_eeg_lapmtx(pst)  
     
    pst - perstimulus time in ms  
     
    T   - Laplace transform basis set  
      
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_eeg_lapmtx.m)
  """

  return _Runtime.call("spm_eeg_lapmtx", *args, **kwargs)
