from spm._runtime import Runtime


def spm_permute_kron(*args, **kwargs):
    r"""
      Permutation of a Kronecker tensor product   
        FORMAT A = spm_permute_kron(A,dim,order)  
        A     - 2-dimensional array (A1 x A2 x ...  
        dim   - dimensions [length(A1), length(A2), ...  
        order - re-ordering; e.g., [2,1, ...  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_permute_kron.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_permute_kron", *args, **kwargs)
