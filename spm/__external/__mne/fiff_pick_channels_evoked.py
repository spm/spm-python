from spm._runtime import Runtime


def fiff_pick_channels_evoked(*args, **kwargs):
    r"""
       
        [res] = fiff_pick_channels_evoked(orig,include,exclude)  
         
        Pick desired channels from evoked-response data  
         
        orig      - The original data  
        include   - Channels to include (if empty, include all available)  
        exclude   - Channels to exclude (if empty, do not exclude any)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_pick_channels_evoked.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_pick_channels_evoked", *args, **kwargs)
