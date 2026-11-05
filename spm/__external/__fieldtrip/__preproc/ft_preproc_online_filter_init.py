from spm._runtime import Runtime


def ft_preproc_online_filter_init(*args, **kwargs):
    r"""
      FT_PREPROC_ONLINE_FILTER_INIT initialize an IIR filter model with coefficients B  
        and A, as used in filter and butter etc. The most recent sample of the signal must  
        be given as a column vector.  
         
        Use as  
          state = ft_preproc_online_filter_init(B, A, dat)  
         
        This function will calculate the filter delay states such that the initial response  
        will be as if the filter already have been applied forever.  
         
        See also PREPROC, FT_PREPROC_ONLINE_FILTER_APPLY  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/preproc/ft_preproc_online_filter_init.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_preproc_online_filter_init", *args, **kwargs)
