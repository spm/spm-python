from spm.__wrapper__ import Runtime


def ft_preproc_online_downsample_init(*args, **kwargs):
    """
      FT_PREPROC_ONLINE_DOWNSAMPLE_INIT initializes an downsampling model with the given factor.  
          
        Use as  
         state = ft_preproc_online_downsample_init(factor)  
         
        See also PREPROC, FT_PREPROC_ONLINE_DOWNSAMPLE_APPLY  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/preproc/ft_preproc_online_downsample_init.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_preproc_online_downsample_init", *args, **kwargs)
