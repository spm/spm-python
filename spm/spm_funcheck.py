from spm._runtime import Runtime


def spm_funcheck(*args, **kwargs):
    r"""
      Convert strings and inline objects to function handles  
        FORMAT [h] = spm_funcheck(f)  
         
        f   - filename, character expression or inline function  
        h   - corresponding function handle  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_funcheck.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_funcheck", *args, **kwargs)
