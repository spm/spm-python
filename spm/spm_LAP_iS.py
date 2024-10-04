from spm.__wrap__ import _Runtime


def spm_LAP_iS(*args, **kwargs):
  """  Default precision function for LAP models (hidden states)  
    FORMAT [iS] = spm_LAP_iS(p,R)  
     
    p{1} - vector of precisions for causal states (v)  
    p{2} - vector of precisions for hidden states (v)  
    R    - generalised precision matrix  
     
    iS   - precision matrix for generalised states (causal and then hidden)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_LAP_iS.m)
  """

  return _Runtime.call("spm_LAP_iS", *args, **kwargs)
