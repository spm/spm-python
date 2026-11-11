from spm._runtime import Runtime


def spm_dcm_identify(*args, **kwargs):
    r"""
      Identify the type of DCM. Return an empty string if unknown  
         
        DCM   - the model to evaluate  
         
        model - a string identifying the modality  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_dcm_identify.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_identify", *args, **kwargs)
