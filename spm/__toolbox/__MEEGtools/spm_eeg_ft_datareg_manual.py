from spm._runtime import Runtime


def spm_eeg_ft_datareg_manual(*args, **kwargs):
    r"""
      Data registration user-interface routine  
        commands the EEG/MEG data co-registration within original sMRI space  
         
        FORMAT D = spm_eeg_inv_datareg_ui(D,[val], modality)  
        Input:  
        Output:  
        D         - same data struct including the new required files and variables  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/MEEGtools/spm_eeg_ft_datareg_manual.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_ft_datareg_manual", *args, **kwargs)
