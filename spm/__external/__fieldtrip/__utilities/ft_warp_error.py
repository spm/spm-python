from spm._runtime import Runtime


def ft_warp_error(*args, **kwargs):
    r"""
      FT_WARP_ERROR computes the mean distance after linear or non-linear warping  
        and can be used as the goalfunction in a 3D warping minimalisation  
         
        Use as  
          dist = ft_warp_error(M, input, target, 'method')  
         
        It returns the mean Euclidean distance (i.e. the residual) for an interactive  
        optimalization to transform the input towards the target using the  
        transformation M with the specified warping method.  
         
        See also FT_WARP_OPTIM, FT_WARP_APPLY  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/ft_warp_error.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_warp_error", *args, **kwargs)
