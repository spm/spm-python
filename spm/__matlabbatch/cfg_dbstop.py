from spm._runtime import Runtime


def cfg_dbstop(*args, **kwargs):
    r"""
    cfg_dbstop is a function.  
          cfg_dbstop(fh)  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/cfg_dbstop.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_dbstop", *args, **kwargs, nargout=0)
