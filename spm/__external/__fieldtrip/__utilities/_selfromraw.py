from spm._runtime import Runtime


def _selfromraw(*args, **kwargs):
    r"""
      FIXME this function is not documented  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/selfromraw.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("selfromraw", *args, **kwargs)
