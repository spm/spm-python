from spm.__wrapper__ import Runtime


def spm_cond_units(*args, **kwargs):
    """
      Scale numeric arrays by a multiple of 10^n to avoid numerical overflow  
        FORMAT [y,scale] = spm_cond_units(y,n)  
          y - y*scale;  
          n - default 3  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_cond_units.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cond_units", *args, **kwargs)
