from spm._runtime import Runtime


def spm_pinv(*args, **kwargs):
    r"""
      Pseudo-inverse for sparse matrices  
        FORMAT X = spm_pinv(A,TOL)  
         
        A   - matrix  
        TOL - Tolerance to force singular value decomposition  
        X   - generalised inverse  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_pinv.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_pinv", *args, **kwargs)
