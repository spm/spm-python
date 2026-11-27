from spm._runtime import Runtime


def spm_dot(*args, **kwargs):
    r"""
      Multidimensional dot (inner) product  
        FORMAT [Y] = spm_dot(X,x,[DIM])  
         
        X   - numeric array  
        x   - numeric vector or cell array of vectors  
        DIM - dimensions to skip [assumes ndims(X) = numel(x)]  
         
        Y   - inner product obtained by summing the products of X and x  
         
        If DIM is not specified the leading dimensions of X are skipped. If x is  
        a vector, the inner product is over the first (matching) dimension of X.  
        This means that if called with a vector valued x, the dot product will be  
        over the first (matching) dimension. Conversely, if called with {x} the  
        dot product will be over the last (matching) dimension of X.  
         
        This version calls tensorprod.m  
         
        See also: spm_cross  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_dot.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dot", *args, **kwargs)
