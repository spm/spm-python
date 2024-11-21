from spm.__wrapper__ import Runtime


def cfg_callbuiltin(*args, **kwargs):
    """
    cfg_callbuiltin is a function.  
          varargout = cfg_callbuiltin(varargin)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_callbuiltin.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_callbuiltin", *args, **kwargs)
