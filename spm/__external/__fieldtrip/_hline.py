from spm._runtime import Runtime


def _hline(*args, **kwargs):
    r"""
      HLINE plot a horizontal line in the current graph  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/hline.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("hline", *args, **kwargs, nargout=0)
