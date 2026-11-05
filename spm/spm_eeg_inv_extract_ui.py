from spm._runtime import Runtime


def spm_eeg_inv_extract_ui(*args, **kwargs):
    r"""
      GUI for contrast of evoked responses and power for an MEG-EEG model  
        FORMAT [D] = spm_eeg_inv_extract_ui(D, val, XYZ)  
        Sets:  
         
            D.contrast.woi   - time (ms) window of interest  
            D.contrast.fboi  - freq (Hz) window of interest  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_inv_extract_ui.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_extract_ui", *args, **kwargs)
