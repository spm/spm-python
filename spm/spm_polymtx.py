from spm.__wrapper__ import Runtime


def spm_polymtx(*args, **kwargs):
    """
      Create basis functions for polynomial expansion  
        FORMAT [b,D,H,o] = spm_polymtx(x,K,FUN)  
         
        x{i}   - domain of expansion (sample points): i = 1,...,N  
        b      - expansion b = [... x{i}.^p.*x{j}.^q ...]: p,q = 0,...,(K - 1)  
        D{i}   - first derivatives for each dimension: dx{i}/db  
        H{i,j} - second derivatives : dx{j}dx{i}/dbdb  
        o      - vector of expansion orders  
       __________________________________________________________________________  
         
        spm_polymtx creates a matrix for a polynomial expansion of order K - 1.  
        With a second output argument, spm_polymtx produces the derivatives.  
         
        b is a large prod(numel(x{i}) x K^N matrix corresponding to the Kroneckor  
        tensor product of each N-dimensional domain. This is useful for dealing  
        with vectorised N-arrays.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_polymtx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_polymtx", *args, **kwargs)
