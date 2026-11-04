from spm._runtime import Runtime


def ft_preproc_online_downsample_init(*args, **kwargs):
    r"""
      FT_PREPROC_ONLINE_DOWNSAMPLE_INIT initializes an downsampling model with the given factor.  
          
        Use as  
         state = ft_preproc_online_downsample_init(factor)  
         
        See also PREPROC, FT_PREPROC_ONLINE_DOWNSAMPLE_APPLY  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/preproc/ft_preproc_online_downsample_init.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_preproc_online_downsample_init", *args, **kwargs)
