from spm.__wrapper__ import Runtime


def spm_detrend(*args, **kwargs):
    """
      Polynomial detrending over columns  
        FORMAT y = spm_detrend(x,p)  
        x   - data matrix  
        p   - order of polynomial [default: 0]  
          
        y   - detrended data matrix  
       __________________________________________________________________________  
         
        spm_detrend removes linear and nonlinear trends from column-wise data  
        matrices.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_detrend.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_detrend", *args, **kwargs)
