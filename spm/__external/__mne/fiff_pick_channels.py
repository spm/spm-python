from spm._runtime import Runtime


def fiff_pick_channels(*args, **kwargs):
    r"""
       
        [sel] = fiff_pick_channels(ch_names,include,exclude)  
         
        Make a selector to pick desired channels from data  
         
        ch_names  - The channel name list to consult  
        include   - Channels to include (if empty, include all available)  
        exclude   - Channels to exclude (if empty, do not exclude any)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_pick_channels.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_pick_channels", *args, **kwargs)
