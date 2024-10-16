from spm.__wrapper__ import Runtime


def spm_diag_array(*args, **kwargs):
  """  Extract diagonal from 3-D arrays  
    FORMAT D = spm_diag_array(X)  
     
    X(:,i,i) -> D(:,i);  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_diag_array.m)
  """

  return Runtime.call("spm_diag_array", *args, **kwargs)
