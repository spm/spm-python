from spm._runtime import Runtime


def _keyval(*args, **kwargs):
    r"""
      KEYVAL returns the value that corresponds to the requested key in a  
        key-value pair list of variable input arguments  
         
        Use as  
          [val] = keyval(key, varargin)  
         
        See also VARARGIN  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/specest/private/keyval.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("keyval", *args, **kwargs)
