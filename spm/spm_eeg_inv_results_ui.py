from spm.__wrapper__ import Runtime


def spm_eeg_inv_results_ui(*args, **kwargs):
    """
      GUI for contrast of evoked responses and power for an MEG-EEG model  
        FORMAT [D] = spm_eeg_inv_results_ui(D,val)  
        Sets:  
         
            D.contrast.woi   - time (ms) window of interest  
            D.contrast.fboi  - freq (Hz) window of interest  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_results_ui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_results_ui", *args, **kwargs)
