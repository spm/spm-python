from spm._runtime import Runtime


def fiff_pick_types_evoked(*args, **kwargs):
    r"""
       
        [res] = fiff_pick_types_evoked(orig,meg,eeg,stim,include,exclude)  
         
        Pick desired channels types from evoked-response data  
         
        orig      - The original data  
        meg       - Include MEG channels  
        eeg       - Include EEG channels  
        stim      - Include stimulus channels  
        include   - Additional channels to include (if empty, do not add any)  
        exclude   - Channels to exclude (if empty, do not exclude any)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/mne/fiff_pick_types_evoked.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fiff_pick_types_evoked", *args, **kwargs)
