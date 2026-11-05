from spm._runtime import Runtime


def spm_eeg_inv_datareg_ui(*args, **kwargs):
    r"""
      User interface for EEG/MEG data coregistration within original sMRI space  
        FORMAT D = spm_eeg_inv_datareg_ui(D,[val], [meegfid, newmrifid, useheadshape])  
        D            - M/EEG dataset  
         
        meegfid      - M/EEG fiducials  
        mrifid       - MRI fiducials  
        useheadshape - use headshape points (1)  
         
        D            - same data struct including the new required files and variables  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_inv_datareg_ui.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_datareg_ui", *args, **kwargs)
