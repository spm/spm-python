from spm.__wrap__ import _Runtime


def spm_est_V(*args, **kwargs):
  """  Test routine to evaluate non-sphericity correction (ReML Whitening)  
    FORMAT [h] = spm_est_V(SPM,c)  
    SPM    - structure containing generic analysis details  
    c      - number of contrasts to simulate (default = 4)  
     
    h      - hyperparameter estimates  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_est_V.m)
  """

  return _Runtime.call("spm_est_V", *args, **kwargs)
