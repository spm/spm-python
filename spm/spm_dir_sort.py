from spm.__wrapper__ import Runtime


def spm_dir_sort(*args, **kwargs):
    """
      sorts the rows and columns of a square matrix  
        FORMAT [A,i,j] = spm_dir_sort(A)  
         
        A    - matrix  
        i,j  - indices  
         
        Effectively, this reorders the rows and columns of A, so that the largest  
        elements are along the leading diagonal of A(i,j)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dir_sort.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dir_sort", *args, **kwargs)
