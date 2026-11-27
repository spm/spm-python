from spm._runtime import Runtime


def spm_length(*args, **kwargs):
    r"""
      Length of a vectorised numeric, cell or structure array  
        FORMAT [n] = spm_length(X)  
        X    - numeric, cell or structure array[s]  
        n    - length(spm_vec(X))  
         
        See spm_vec, spm_unvec  
       __________________________________________________________________________  
         
        e.g.:  
        spm_length({eye(2) 3}) = 5  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_length.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_length", *args, **kwargs)
