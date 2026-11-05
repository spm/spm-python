from spm._runtime import Runtime


def spm_eeg_montage_ui(*args, **kwargs):
    r"""
      GUI for EEG montage (rereference EEG data to new reference channel(s))  
        FORMAT montage = spm_eeg_montage_ui(montage)  
         
        montage     - structure with fields:  
          tra       - MxN matrix  
          labelnew  - Mx1 cell-array - new labels  
          labelorg  - Nx1 cell-array - original labels  
         
        Output is empty if the GUI is closed.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_montage_ui.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_montage_ui", *args, **kwargs)
