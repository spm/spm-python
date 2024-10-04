from spm.__wrap__ import _Runtime


def ft_warp_error(*args, **kwargs):
  """  FT_WARP_ERROR computes the mean distance after linear or non-linear warping  
    and can be used as the goalfunction in a 3D warping minimalisation  
     
    Use as  
      dist = ft_warp_error(M, input, target, 'method')  
     
    It returns the mean Euclidean distance (i.e. the residual) for an interactive  
    optimalization to transform the input towards the target using the  
    transformation M with the specified warping method.  
     
    See also FT_WARP_OPTIM, FT_WARP_APPLY  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_warp_error.m)
  """

  return _Runtime.call("ft_warp_error", *args, **kwargs)
