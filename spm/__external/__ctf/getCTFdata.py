from spm._runtime import Runtime


def getCTFdata(*args, **kwargs):
    r"""
       getCTFdata.m   Reads specified trials from .meg4 files in CTF-format data set.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/ctf/getCTFdata.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("getCTFdata", *args, **kwargs)
