from spm._runtime import Runtime


def cfg_callbuiltin(*args, **kwargs):
    r"""
    cfg_callbuiltin is a function.  
          varargout = cfg_callbuiltin(varargin)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/cfg_callbuiltin.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_callbuiltin", *args, **kwargs)
