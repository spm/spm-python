from spm._runtime import Runtime


def ft_inverse_montage(*args, **kwargs):
    r"""
      FT_INVERSE_MONTAGE constructs an inverse of the input montage matrix,  
        allowing a linear projection of the channel timeseries to be undone.  
         
        Use as  
          montage = ft_inverse_montage(montage)  
         
        See also FT_APPLY_MONTAGE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/ft_inverse_montage.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_inverse_montage", *args, **kwargs)
