from spm.__wrapper__ import Runtime


def spm_speye(*args, **kwargs):
    """
      Sparse leading diagonal matrix  
        FORMAT [D] = spm_speye(m,n,k,c)  
         
        returns an m x n matrix with ones along the k-th leading diagonal. If  
        called with an optional fourth argument c = 1, a wraparound sparse matrix  
        is returned. If c = 2, then empty rows or columns are filled in on the  
        leading diagonal.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_speye.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_speye", *args, **kwargs)
