from spm._runtime import Runtime


def spm_dir_sort(*args, **kwargs):
    r"""
      sorts the rows and columns of a square matrix  
        FORMAT [A,i,j] = spm_dir_sort(A)  
         
        A    - matrix  
        i,j  - indices  
         
        Effectively, this reorders the rows and columns of A, so that the largest  
        elements are along the leading diagonal of A(i,j)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_dir_sort.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dir_sort", *args, **kwargs)
