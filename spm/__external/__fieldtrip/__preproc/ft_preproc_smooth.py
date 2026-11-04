from spm._runtime import Runtime


def ft_preproc_smooth(*args, **kwargs):
    r"""
      FT_PREPROC_SMOOTH performs boxcar smoothing with specified length.  
        Edge behavior is improved by implicit padding with the mean over  
        half the boxcar length at the edges of the data segment.  
         
        Use as  
          [dat] = ft_preproc_smooth(dat, n)  
         
        Where dat is an Nchan x Ntime data matrix, and n is the length  
        of the boxcar smoothing kernel  
         
        If the data contains NaNs, these are ignored for the computation, but  
        retained in the output.  
         
        See also PREPROC  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/preproc/ft_preproc_smooth.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_preproc_smooth", *args, **kwargs)
