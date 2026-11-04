from spm._runtime import Runtime


def spm_check_results(*args, **kwargs):
    r"""
      Display several MIPs in the same figure  
        FORMAT spm_check_results(SPMs,xSPM)  
        SPMs    - char or cell array of paths to SPM.mat[s]  
        xSPM    - structure containing thresholding details, see spm_getSPM.m  
         
        Beware: syntax and features of this function are likely to change.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_check_results.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_check_results", *args, **kwargs, nargout=0)
