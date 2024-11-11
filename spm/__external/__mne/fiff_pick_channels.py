from spm.__wrapper__ import Runtime


def fiff_pick_channels(*args, **kwargs):
    """
       
        [sel] = fiff_pick_channels(ch_names,include,exclude)  
         
        Make a selector to pick desired channels from data  
         
        ch_names  - The channel name list to consult  
        include   - Channels to include (if empty, include all available)  
        exclude   - Channels to exclude (if empty, do not exclude any)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_pick_channels.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_pick_channels", *args, **kwargs)
