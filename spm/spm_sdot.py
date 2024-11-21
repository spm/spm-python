from spm.__wrapper__ import Runtime


def spm_sdot(*args, **kwargs):
    """
      Sparse multidimensional dot (inner) product  
        FORMAT [Y] = spm_sdot(X,x,[DIM])  
         
        X   - numeric array  
        x   - cell array of numeric vectors  
        DIM - dimension to omit (assumes ndims(X) = numel(x))  
         
        Y  - inner product obtained by summing the products of X and x along DIM  
         
        If DIM is not specified the leading dimensions of X are omitted. This  
        routine assumes X is sparse  
         
        See also: spm_dot, spm_cross  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_sdot.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_sdot", *args, **kwargs)
