from spm.__wrapper__ import Runtime


def spm_dcm_fnirs_specify(*args, **kwargs):
    """
      Specify inputs of a DCM for fNIRS  
        FORMAT [DCM] = spm_dcm_nirs_specify(SPMf)  
         
        SPMf - SPM filename(s)  
         
        DCM  - DCM structure (see spm_dcm_ui)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/dcm_fnirs/spm_dcm_fnirs_specify.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_fnirs_specify", *args, **kwargs)
