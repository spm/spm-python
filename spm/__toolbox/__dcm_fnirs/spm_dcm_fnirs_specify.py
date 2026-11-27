from spm._runtime import Runtime


def spm_dcm_fnirs_specify(*args, **kwargs):
    r"""
      Specify inputs of a DCM for fNIRS  
        FORMAT [DCM] = spm_dcm_nirs_specify(SPMf)  
         
        SPMf - SPM filename(s)  
         
        DCM  - DCM structure (see spm_dcm_ui)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_fnirs/spm_dcm_fnirs_specify.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_fnirs_specify", *args, **kwargs)
