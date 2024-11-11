from spm.__wrapper__ import Runtime


def spm_bms_against_null(*args, **kwargs):
    """
      Plot PPM showing evidence against null  
        FORMAT spm_bms_against_null(logbf_file)  
         
        logbf_file  -  Log Bayes Factor file providing evidence against null  
         
        Call this function when SPM is already running  
        or set SPM to appropriate modality eg. spm('defaults','FMRI');  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_bms_against_null.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_bms_against_null", *args, **kwargs, nargout=0)
