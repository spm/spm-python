from spm._runtime import Runtime


def spm_speye(*args, **kwargs):
    r"""
      Sparse leading diagonal matrix  
        FORMAT [D] = spm_speye(m,n,k,c,o)  
         
        Returns an m x n matrix with ones along the k-th leading diagonal. If  
        called with an optional fourth argument c = 1, a wraparound sparse matrix  
        is returned. If c = 2, then empty rows or columns are filled in on the  
        leading diagonal. The final (order) argument (o) returns D^o. The default  
        value is o = 1.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_speye.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_speye", *args, **kwargs)
