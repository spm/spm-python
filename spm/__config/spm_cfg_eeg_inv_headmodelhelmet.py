from spm._runtime import Runtime


def spm_cfg_eeg_inv_headmodelhelmet(*args, **kwargs):
    """
      Configuration file for specifying the head model for source reconstruction  
        This is for registration using new helmet design.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_inv_headmodelhelmet.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_eeg_inv_headmodelhelmet", *args, **kwargs)
