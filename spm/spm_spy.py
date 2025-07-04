from spm._runtime import Runtime


def spm_spy(*args, **kwargs):
    """
      Pretty version of spy  
        FORMAT spm_spy(X,Markersize,m)  
        X    - sparse {m x n} matrix  
         
        See also: spy  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_spy.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_spy", *args, **kwargs, nargout=0)
