from spm._runtime import Runtime


def mne_pick_channels_forward(*args, **kwargs):
    r"""
       
        [fwd] = mne_pick_channels_forward(orig,include,exclude)  
         
        Pick desired channels from a forward solution  
         
        orig      - The original forward solution  
        include   - Channels to include (if empty, include all available)  
        exclude   - Channels to exclude (if empty, do not exclude any)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/mne_pick_channels_forward.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mne_pick_channels_forward", *args, **kwargs)
