from spm._runtime import Runtime


def spm_eeg_ft_datareg_manual(*args, **kwargs):
    """
      Data registration user-interface routine  
        commands the EEG/MEG data co-registration within original sMRI space  
         
        FORMAT D = spm_eeg_inv_datareg_ui(D,[val], modality)  
        Input:  
        Output:  
        D         - same data struct including the new required files and variables  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/MEEGtools/spm_eeg_ft_datareg_manual.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_ft_datareg_manual", *args, **kwargs)
