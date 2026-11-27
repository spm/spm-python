from spm._runtime import Runtime


def spm_eeg_inv_imag_api(*args, **kwargs):
    r"""
      API for EEG/MEG source reconstruction interface  
        FORMAT:  
           FIG = SPM_EEG_INV_IMAG_API launch spm_eeg_inv_imag_api GUI.  
           SPM_EEG_INV_IMAG_API('callback_name', ...) invoke the named callback.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_eeg_inv_imag_api.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_imag_api", *args, **kwargs)
