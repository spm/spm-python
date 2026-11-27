from spm._runtime import Runtime


def spm_fileparts(*args, **kwargs):
    r"""
      Like fileparts, but separates off a comma separated list at the end  
        FORMAT [pth,nam,ext,num] = spm_fileparts(fname)  
        fname  - original filename  
         
        pth    - path  
        nam    - filename  
        ext    - extension  
        num    - comma separated list of values  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_fileparts.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_fileparts", *args, **kwargs)
