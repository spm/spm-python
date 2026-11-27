from spm._runtime import Runtime


def _common_size(*args, **kwargs):
    r"""
    common_size is a function.  
          [errorcode, varargout] = common_size(varargin)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/stats/private/common_size.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("common_size", *args, **kwargs)
