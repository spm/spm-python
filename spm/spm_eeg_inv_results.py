from spm.__wrapper__ import Runtime


def spm_eeg_inv_results(*args, **kwargs):
    """
      Contrast of evoked responses and power for an MEG-EEG model  
        FORMAT [D] = spm_eeg_inv_results(D)  
        Requires:  
         
            D.inv{i}.contrast.woi   - (n x 2) time (ms) window[s] of interest  
            D.inv{i}.contrast.fboi  - frequency window of interest  
            D.inv{i}.contrast.type  - 'evoked' or 'induced'  
         
        This routine will create a contrast for each trial type and will compute  
        induced responses in terms of power (over trials) if requested; otherwise  
        the power in D.inv{i}.contrast.GW corresponds to the evoked power.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_results.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_results", *args, **kwargs)
