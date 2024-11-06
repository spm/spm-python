from spm.__wrapper__ import Runtime


def fiff_pick_channels_evoked(*args, **kwargs):
    """
       
        [res] = fiff_pick_channels_evoked(orig,include,exclude)  
         
        Pick desired channels from evoked-response data  
         
        orig      - The original data  
        include   - Channels to include (if empty, include all available)  
        exclude   - Channels to exclude (if empty, do not exclude any)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_pick_channels_evoked.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_pick_channels_evoked", *args, **kwargs)
