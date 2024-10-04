from spm.__wrap__ import _Runtime


def spm_minmax(*args, **kwargs):
  """  Compute a suitable range of intensities for VBM preprocessing stuff  
    FORMAT [mnv,mxv] = spm_minmax(g)  
    g    - array of data  
    mnv  - minimum value  
    mxv  - maximum value  
     
    A MOG with two Gaussians is fitted to the intensities.  The lower  
    Gaussian is assumed to represent background.  The lower value is  
    where there is a 50% probability of being above background.  The  
    upper value is one that encompases 99.5% of the values.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_minmax.m)
  """

  return _Runtime.call("spm_minmax", *args, **kwargs)
