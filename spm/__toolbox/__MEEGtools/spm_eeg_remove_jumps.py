from spm.__wrapper__ import Runtime


def spm_eeg_remove_jumps(*args, **kwargs):
    """
      Remove "jumps" (discontinuities) from the M/EEG raw signal  
        FORMAT [D, alljumps] = spm_eeg_remove_jumps(S)  
         
        INPUT:  
        S          - struct (optional)  
        fields of S:  
        D          - filename  
        channels          - cell array of channel names. Can include generic  
                                wildcards: 'All', 'EEG', 'MEG' etc.  
        threshold  - threshold, default = 3000 fT (3pT)  
        stdthreshold - if present overrides the threshold field and specifies the  
                      threshold in terms of standard deviation  
        prefix       - prefix for the output dataset (default - 'j')  
         
        OUTPUT:  
        D          - MEEG object  
       __________________________________________________________________________  
         
        This function removes "jumps" (discontinuities) from the EEG/MEG raw  
        signal, based on an absolute threshold, and filters the signal derivative  
        over 20 timepoints.  
        Such jumps occur with squid resetting and when acquisition is stopped  
        with the "abort" button.  
        This procedure is necessary before performing highpass filtering on the  
        continuous data.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_remove_jumps.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_remove_jumps", *args, **kwargs)
