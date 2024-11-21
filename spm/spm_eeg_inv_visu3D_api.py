from spm.__wrapper__ import Runtime


def spm_eeg_inv_visu3D_api(*args, **kwargs):
    """
      SPM_EEG_INV_VISU3D_API M-file for spm_eeg_inv_visu3D_api.fig  
        - FIG = SPM_EEG_INV_VISU3D_API launch spm_eeg_inv_visu3D_api GUI.  
        - D   = SPM_EEG_INV_VISU3D_API(D) open with D  
        - SPM_EEG_INV_VISU3D_API(filename) where filename is the eeg/meg .mat file  
        - SPM_EEG_INV_VISU3D_API('callback_name', ...) invoke the named callback.  
         
        Last Modified by GUIDE v2.5 18-Feb-2011 14:23:27  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_visu3D_api.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_eeg_inv_visu3D_api", *args, **kwargs)
