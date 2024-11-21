from spm.__wrapper__ import Runtime


def spm_eeg_inv_imag_api(*args, **kwargs):
    """
      API for EEG/MEG source reconstruction interface  
        FORMAT:  
           FIG = SPM_EEG_INV_IMAG_API launch spm_eeg_inv_imag_api GUI.  
           SPM_EEG_INV_IMAG_API('callback_name', ...) invoke the named callback.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_imag_api.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_imag_api", *args, **kwargs)
