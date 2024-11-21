from spm.__wrapper__ import Runtime


def spm_dcm_sparse_priors(*args, **kwargs):
    """
      Return Adjacency matrices for bidirectional coupling  
        FORMAT  [A,K,k] = spm_dcm_sparse_priors(n)  
         
        INPUT:  
           n         - number of nodes  
         
        OUTPUT:  
           A{:}      - adjacency matrices  
           K{1:K}{:} - adjacency matrices (for k - 1 edges)  
           k         - row vector of edge numbers (size)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dcm_sparse_priors.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dcm_sparse_priors", *args, **kwargs)
