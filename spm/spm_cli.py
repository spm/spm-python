from spm._runtime import Runtime


def spm_cli(*args, **kwargs):
    r"""
      Command line interface for SPM  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_cli.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cli", *args, **kwargs, nargout=0)
