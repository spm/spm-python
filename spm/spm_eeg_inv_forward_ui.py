from spm._runtime import Runtime


def spm_eeg_inv_forward_ui(*args, **kwargs):
    r"""
      Forward Solution user interface  
        FORMAT D = spm_eeg_inv_forward_ui(D,val)  
        D        - input data struct (optional)  
        val      - model of interest (optional)  
         
        D        - same data struct including the forward solution  
       __________________________________________________________________________  
         
        Call the forward computation for either EEG or MEG data using various  
        types of solutions using FieldTrip.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_inv_forward_ui.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_forward_ui", *args, **kwargs)
