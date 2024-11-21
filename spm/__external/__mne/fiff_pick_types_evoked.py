from spm.__wrapper__ import Runtime


def fiff_pick_types_evoked(*args, **kwargs):
    """
       
        [res] = fiff_pick_types_evoked(orig,meg,eeg,stim,include,exclude)  
         
        Pick desired channels types from evoked-response data  
         
        orig      - The original data  
        meg       - Include MEG channels  
        eeg       - Include EEG channels  
        stim      - Include stimulus channels  
        include   - Additional channels to include (if empty, do not add any)  
        exclude   - Channels to exclude (if empty, do not exclude any)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/mne/fiff_pick_types_evoked.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fiff_pick_types_evoked", *args, **kwargs)
