from spm._runtime import Runtime


def spm_dcm_identify(*args, **kwargs):
    """
      Identify the type of DCM. Return an empty string if unknown  
         
        DCM   - the model to evaluate  
         
        model - a string identifying the modality  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_identify.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dcm_identify", *args, **kwargs)
