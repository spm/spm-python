from spm.__wrapper__ import Runtime


def spm_permute_kron(*args, **kwargs):
    """
      Permutation of a Kronecker tensor product   
        FORMAT A = spm_permute_kron(A,dim,order)  
        A     - 2-dimensional array (A1 x A2 x ...  
        dim   - dimensions [length(A1), length(A2), ...  
        order - re-ordering; e.g., [2,1, ...  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_permute_kron.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_permute_kron", *args, **kwargs)
