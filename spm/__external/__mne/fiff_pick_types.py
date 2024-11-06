from spm.__wrapper__ import Runtime


def fiff_pick_types(*args, **kwargs):
    """
       
        [sel] = fiff_pick_types(info,meg,eeg,stim,exclude)  
         
        Create a selector to pick desired channel types from data  
         
        info      - The measurement info  
        meg       - Include MEG channels  
        eeg       - Include EEG channels  
        stim      - Include stimulus channels  
        include   - Additional channels to include (if empty, do not add any)  
        exclude   - Channels to exclude (if empty, do not exclude any)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_pick_types.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_pick_types", *args, **kwargs)
