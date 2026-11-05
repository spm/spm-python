from spm._runtime import Runtime


def ft_preproc_online_filter_apply(*args, **kwargs):
    r"""
      FT_PREPROC_ONLINE_FILTER_APPLY passes a signal through the online filter and  
        returns the updated filter model (delay states) and the filtered signal.  
         
        Use as  
          [state, dat] = ft_preproc_online_filter_apply(state, dat)  
        where  
          dat   = Nchan x Ntime  
          state = filter state, see FT_PREPROC_ONLINE_FILTER_INIT  
         
        See also PREPROC  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/preproc/ft_preproc_online_filter_apply.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_preproc_online_filter_apply", *args, **kwargs)
