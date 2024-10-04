from spm.__wrap__ import _Runtime


def spm_en(*args, **kwargs):
  """  Euclidean normalization  
    FORMAT [X] = spm_en(X,[p])  
    X   - matrix  
    p   - optional polynomial detrend [default: []]  
   __________________________________________________________________________  
     
    spm_en performs a Euclidean normalization setting the column-wise sum of  
    squares to unity (leaving columns of zeros as zeros).  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_en.m)
  """

  return _Runtime.call("spm_en", *args, **kwargs)
