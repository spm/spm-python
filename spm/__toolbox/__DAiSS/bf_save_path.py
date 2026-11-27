from spm._runtime import Runtime


def bf_save_path(*args, **kwargs):
    r"""
      Saves BF data in a MAT file  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_save_path.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_save_path", *args, **kwargs, nargout=0)
