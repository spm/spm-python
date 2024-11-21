from spm.__wrapper__ import Runtime


def _multivariate_decomp(*args, **kwargs):
    """
      MULTIVARIATE_DECOMP does a linear decomposition of multivariate time series,  
        based on the covariance matrix.  
         
        Use as:  
         [E, D] = multivariate_decomp(C,x,y,method)  
         
        Input arguments:  
          C = covariance matrix (or csd) between input time series   
          x = list of indices corresponding to group 1   
          y = list of indices corresponding to group 2   
          method = 'cca', or 'pls', 'mlr', decomposition method  
                   (canonical correlation partial least squares, or multivariate  
                    linear regression). In the case of mlr-like decompositions,  
                    the indices for x reflect the independent variable)  
          realflag = true (default) or false. Do the operation on the real part  
                     of the matrix if the input matrix is complex-valued  
          fastflag = true (default) or false. Compute the solution without an  
                     eigenvalue decomposition (only when numel(x)==1)  
         
        The implementation is based on Borga 2001, Canonical correlation, a  
        tutorial (can be found online).  
         
        Output arguments:  
          E = projection matrix (not necessarily normalized). to get the orientation,  
              do orix = E(x,1)./norm(E(x,1)), and oriy = E(y,1)./norm(E(y,1));  
          D = diagonal matrix with eigenvalues  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/private/multivariate_decomp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("multivariate_decomp", *args, **kwargs)
