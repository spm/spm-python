from spm.__wrapper__ import Runtime


def spm_dot(*args, **kwargs):
    """
      Multidimensional dot (inner) product  
        FORMAT [Y] = spm_dot(X,x,[DIM])  
         
        X   - numeric array  
        x   - cell array of numeric vectors  
        DIM - dimensions to skip [assumes ndims(X) = numel(x)]  
         
        Y   - inner product obtained by summing the products of X and x  
         
        If DIM is not specified the leading dimensions of X are skipped. If x is  
        a vector the inner product is over the first matching dimension of X.  
        This means that if called with a vector valued x, the dot product will be  
        over the first (matching) dimension. Conversely, if called with {x} the  
        dot product will be over the last dimension of X.  
         
        This version calls tensorprod.m  
         
         
        See also: spm_cross  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_dot.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_dot", *args, **kwargs)
