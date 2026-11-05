from spm._runtime import Runtime


def _istrue(*args, **kwargs):
    r"""
      ISTRUE converts an input argument like "yes/no", "true/false" or "on/off" into a  
        boolean. If the input is boolean, then it will remain like that.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/statfun/private/istrue.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("istrue", *args, **kwargs)
