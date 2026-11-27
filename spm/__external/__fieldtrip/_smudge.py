from spm._runtime import Runtime


def _smudge(*args, **kwargs):
    r"""
      SMUDGE(DATIN, TRI) computes a smudged version of the input data datain,  
        given a triangulation tri. The algorithm is according to what is in  
        MNE-Suite, documented in chapter 8.3  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/smudge.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("smudge", *args, **kwargs)
