from spm._runtime import Runtime


def spm_perm_mtx(*args, **kwargs):
    r"""
      Return a matrix of indices permuted over n  
        FORMAT [K] = spm_perm_mtx(n)  
           n   - (scalar) number of indices  
           K   - (2^n x n) permutation matrix  
        or  
           n   - (vector) indices  
           K   - (length(n)! x n) permutation matrix  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_perm_mtx.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_perm_mtx", *args, **kwargs)
