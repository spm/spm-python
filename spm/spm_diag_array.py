from spm._runtime import Runtime


def spm_diag_array(*args, **kwargs):
    r"""
      Extract diagonal from 3-D arrays  
        FORMAT D = spm_diag_array(X)  
         
        X(:,i,i) -> D(:,i);  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_diag_array.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_diag_array", *args, **kwargs)
