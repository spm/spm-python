from spm.__wrapper__ import Runtime


def spm_inline2func(*args, **kwargs):
    """
      Convert an inline object to a function handle  
        FORMAT [h] = spm_inline2func(f)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_inline2func.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_inline2func", *args, **kwargs)
