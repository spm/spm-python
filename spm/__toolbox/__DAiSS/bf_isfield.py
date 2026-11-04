from spm._runtime import Runtime


def bf_isfield(*args, **kwargs):
    r"""
      Efficiently identify if a field is contained within a BF file  
        FORMAT bool = bf_isfield(BF,field)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_isfield.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_isfield", *args, **kwargs)
