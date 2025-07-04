from spm._runtime import Runtime


def spm_cfg_eeg_momentfit(*args, **kwargs):
    """
      Configuration file for imaging source inversion reconstruction.  
        This version to supply position and orientation parameters idea is to  
        estimate dipole moments given priors and return a model evidence for  
        these priors.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_momentfit.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_eeg_momentfit", *args, **kwargs)
