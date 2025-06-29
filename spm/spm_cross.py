from spm._runtime import Runtime


def spm_cross(*args, **kwargs):
    """
      Multidimensional cross (outer) product  
        FORMAT [Y] = spm_cross(X,x)  
        FORMAT [Y] = spm_cross(X)  
         
        X  - numeric array  
        x  - numeric array  
         
        Y  - outer product  
         
        See also: spm_dot  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_cross.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cross", *args, **kwargs)
