from spm.__wrapper__ import Runtime


def spm_conv(*args, **kwargs):
  """  Gaussian convolution  
    FORMAT [X] = spm_conv(X,sx[,sy])  
    X    - matrix  
    sx   - kernel width (FWHM) in pixels  
    sy   - optional non-isomorphic smoothing  
   __________________________________________________________________________  
     
    spm_conv is a one or two dimensional convolution of a matrix variable in  
    working memory.  It capitalizes on the sparsity structure of the problem  
    and the separablity of multidimensional convolution with a Gaussian  
    kernel by using one-dimensional convolutions and kernels that are  
    restricted to non near-zero values.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_conv.m)
  """

  return Runtime.call("spm_conv", *args, **kwargs)
