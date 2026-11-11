from spm._runtime import Runtime


def fiff_pick_types(*args, **kwargs):
    r"""
       
        [sel] = fiff_pick_types(info,meg,eeg,stim,exclude)  
         
        Create a selector to pick desired channel types from data  
         
        info      - The measurement info  
        meg       - Include MEG channels  
        eeg       - Include EEG channels  
        stim      - Include stimulus channels  
        include   - Additional channels to include (if empty, do not add any)  
        exclude   - Channels to exclude (if empty, do not exclude any)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_pick_types.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_pick_types", *args, **kwargs)
