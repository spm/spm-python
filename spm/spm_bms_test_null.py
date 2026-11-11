from spm._runtime import Runtime


def spm_bms_test_null(*args, **kwargs):
    r"""
      Plot PPM showing evidence for null  
        FORMAT spm_bms_test_null(logbf_file)  
         
        logbf_file  -  Log Bayes Factor file providing evidence against null  
         
        Call this function when SPM is already running  
        or set SPM to appropriate modality eg. spm('defaults','FMRI');  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_bms_test_null.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_bms_test_null", *args, **kwargs, nargout=0)
