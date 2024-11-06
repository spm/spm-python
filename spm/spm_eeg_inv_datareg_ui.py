from spm.__wrapper__ import Runtime


def spm_eeg_inv_datareg_ui(*args, **kwargs):
    """
      User interface for EEG/MEG data coregistration within original sMRI space  
        FORMAT D = spm_eeg_inv_datareg_ui(D,[val], [meegfid, newmrifid, useheadshape])  
        D            - M/EEG dataset  
         
        meegfid      - M/EEG fiducials  
        mrifid       - MRI fiducials  
        useheadshape - use headshape points (1)  
         
        D            - same data struct including the new required files and variables  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_datareg_ui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_datareg_ui", *args, **kwargs)
