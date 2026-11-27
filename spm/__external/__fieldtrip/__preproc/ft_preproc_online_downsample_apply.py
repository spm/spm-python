from spm._runtime import Runtime


def ft_preproc_online_downsample_apply(*args, **kwargs):
    r"""
      FT_PREPROC_ONLINE_DOWNSAMPLE_APPLY passes a signal through the online downsampler  
        and returns the downsampler state and the downsampled signal. The state keeps track  
        of the number of samples to be skipped in the next call.  
         
        Use as  
           [state, dat] = ft_preproc_online_downsample_apply(state, x)  
        where  
          dat   = Nchan x Ntime  
          state = downsampler state, see FT_PREPROC_ONLINE_DOWNSAMPLE_INIT  
         
        See also PREPROC  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/preproc/ft_preproc_online_downsample_apply.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_preproc_online_downsample_apply", *args, **kwargs)
