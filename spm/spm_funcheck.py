from spm.__wrapper__ import Runtime


def spm_funcheck(*args, **kwargs):
    """
      Convert strings and inline objects to function handles  
        FORMAT [h] = spm_funcheck(f)  
         
        f   - filename, character expression or inline function  
        h   - corresponding function handle  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_funcheck.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_funcheck", *args, **kwargs)
