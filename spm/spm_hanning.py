from spm.__wrapper__ import Runtime


def spm_hanning(*args, **kwargs):
    """
      Return the n-point Hanning window in a column vector  
        FORMAT H = spm_hanning(n)  
        n  -  length of hanning function  
        H  -  hanning function  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_hanning.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_hanning", *args, **kwargs)
