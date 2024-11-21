from spm.__wrapper__ import Runtime


def spm_interp(*args, **kwargs):
    """
      1 or 2-D array interpolation  
        FORMAT [x] = spm_interp(x,r)  
        x - array  
        r - interpolation rate  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_interp.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_interp", *args, **kwargs)
