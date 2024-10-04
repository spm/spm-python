from spm.__wrap__ import _Runtime


def spm_MNpdf(*args, **kwargs):
  """  Evaluate a Multivariate Gaussian PDF  
    FORMAT [y] = spm_MNpdf (m, C, x)  
      
    m     [d x 1] mean  
    C     [d x d] covar  
    x     [n x d] points at which to evaluate  
     
    y     [n x 1] density at n points  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mixture/spm_MNpdf.m)
  """

  return _Runtime.call("spm_MNpdf", *args, **kwargs)
