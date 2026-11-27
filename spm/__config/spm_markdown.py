from spm._runtime import Runtime


def spm_markdown(*args, **kwargs):
    r"""
      Convert a job configuration tree into a series of markdown documents  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/config/spm_markdown.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_markdown", *args, **kwargs, nargout=0)
