from spm.__wrapper__ import Runtime


def spm_perm_mtx(*args, **kwargs):
    """
      Return a matrix of indices permuted over n  
        FORMAT [K] = spm_perm_mtx(n)  
           n   - (scalar) number of indices  
           K   - (2^n x n) permutation matrix  
        or  
           n   - (vector) indices  
           K   - (length(n)! x n) permutation matrix  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_perm_mtx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_perm_mtx", *args, **kwargs)
